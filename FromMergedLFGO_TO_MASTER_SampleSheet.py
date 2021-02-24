# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:07:41 2021

@author: jabra
"""

import os
os.getcwd()


import pandas as pd
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width',100) #Para que se vean todas las columnas que quepan en IPython console

# Load Data
Merged = pd.read_csv('D:\\Dropbox\\SharedWithLuciaLIIGH\\OriginalesMetadatos\\ParaLuisfer\\DeLFparaAA\\merged_files_LFGO_v1.0.txt', sep="\t")
Merged.columns = Merged.columns.str.replace("-", "_")
Cluster = pd.read_csv('D:\\Dropbox\\SharedWithLuciaLIIGH\\OriginalesMetadatos\\20210127_UnificarDB\\MASTER_SampleSheet_Downloaded20210222.csv')

# Cuáles de Merged están en Cluster?
isin_col = Cluster.ID.isin(Merged.SampleName_BGI)
Cluster[isin_col][["ID", "ID_SeqProvider", 'Especie..MALDI.TOF.',"Secuenciación", "Estado"] ]
#Cuántos son?
Cluster[isin_col].count()# 133
#Hay repetidos?
Cluster[isin_col][["ID","Especie..MALDI.TOF."]].groupby("ID").count().plot() # NO
# de qué especie dice que son por maldi? De muchas 
Cluster[isin_col][["ID", "ID_SeqProvider", 'Especie..MALDI.TOF.',"Secuenciación", "Estado"] ].groupby("Especie..MALDI.TOF.").count()

# Cuáles de Cluster están en Merged?
isin_col2=Merged.LabeltoBGI_BGI.isin(Cluster[isin_col].ID)
Merged[isin_col2][["Pos_Placa_AisLev", "ID_criovial_AisLev", "Especie_AisLev", "Estado_AisLev","SampleName_BGI" ]]
# Cuántos son? 
Merged[isin_col2].count() #133
# Qué especie dice que son? 120Scer, 10Ckef+2CKru=12KlMa, 1Kaz.humilis
Merged[isin_col2][["Especie_AisLev", "Estado_AisLev","SampleName_BGI" ]].groupby("Especie_AisLev").count()

# Unir ambas tablas por sus coincidencias en IDs
merged_in = pd.merge(left=Merged, right=Cluster, how='inner', left_on='SampleName_BGI', right_on='ID')
# ¿Cuáles tienen distinto Estado? Solo 1 cambió y en el árbol ya está la correcta, que es XA251c2
merged_in[merged_in.Estado_AisLev != merged_in.Estado][["Pos_Placa_AisLev","Estado_AisLev", "Palenque_AisLev", "SampleName_BGI", "ID", "Estado", "Palenque" ]]


# Revisar el archivo que ya tiene asignada especie por secuenciación
Sequenced=pd.read_csv('D:\\Dropbox\\SharedWithLuciaLIIGH\\OriginalesMetadatos\\20210127_UnificarDB\\Q20_perRef_ByCases.csv')
# Unir la tabla merged_in con las Sequenced
merged_inSeq = pd.merge(left=merged_in, right=Sequenced, how='inner', left_on='SampleName_BGI', right_on='Sample')
merged_inSeq[["Pos_Placa_AisLev","Estado_AisLev","SampleName_BGI", "ID", "Estado", "Cat","Especie..MALDI.TOF." ]]
merged_inSeq[merged_inSeq.Estado_AisLev != merged_in.Estado][["Pos_Placa_AisLev","Estado_AisLev", "Palenque_AisLev", "SampleName_BGI", "ID", "Estado", "Palenque", "Cat" ]]

# Cuántas son? 133
merged_inSeq[["Pos_Placa_AisLev","Estado_AisLev","SampleName_BGI", "ID", "Estado", "Cat","Especie..MALDI.TOF." ]].count()
# Ver asignación de especie por ITS, Sequencing, MaldiTof y el de la colección AisladosLevaduras
merged_inSeq[["ID", "Estado", "Cat","Especie..MALDI.TOF.", "Especie..ITS."]]

# Cargar datos de Ivan
ClusterIvan=pd.read_csv('D:\\Dropbox\\SharedWithLuciaLIIGH\\OriginalesMetadatos\\20210127_UnificarDB\\MASTER_SampleSheet_IVAN_210223.csv')
ClusterIvan = ClusterIvan.add_suffix("Iv")

# El archivo de ivan tiene 337x31 y el del Cluster 332x31
merged_inCluster=pd.merge(left=Cluster, right=ClusterIvan, how='inner', left_on='ID', right_on='IDIv')
# No entiendo porque el merged tiene 333x62

merged_inCluster["Estado_AisLev","Estado","EstadoIv"]


