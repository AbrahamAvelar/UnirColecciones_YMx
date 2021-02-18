# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 19:58:50 2021

@author: jabra
"""
import os
os.getcwd()
os.chdir("D:\Dropbox\SharedWithLuciaLIIGH\OriginalesMetadatos\20210127_UnificarDB")

import pandas as pd
pd.set_option('display.max_columns', None)
SamplesTPFS = pd.read_csv("20200129_SamplesToPrepareForSequencing.csv")
Merged = pd.read_csv('D:\\Dropbox\\SharedWithLuciaLIIGH\\OriginalesMetadatos\\ParaLuisfer\\DeLFparaAA\\merged_files_LFGO_v1.0.txt', sep="\t")

Merged.columns = Merged.columns.str.replace("-", "_")
SamplesTPFS.columns = SamplesTPFS.columns.str.replace(" ", "_")
SamplesTPFS.columns = SamplesTPFS.columns.str.replace(".", "")

import numpy as np
comparison_column = np.where(Merged["SampleName_BGI"] == Merged["LabeltoBGI_BGI"], True, False).asint()
print(comparison_column)


# CUÁLES ESTÁN EN SamplesToPrepareForSequencing that are not in Merged_LFGO
isin_col = SamplesTPFS.Label_to_BGI.isin(Merged.LabeltoBGI_BGI)
sub_SamplesTPF = SamplesTPFS[~isin_col]
sub_SamplesTPF[["ID_PG", "ID_nuevo_PG","ID_nuevo_PGc","Label_to_BGI"]]

# Cuáles están en Merged_LFGO that are not in SamplesToPrepareForSequencing
isin_col2 = Merged.LabeltoBGI_BGI.isin(SamplesTPFS.Label_to_BGI)
sub_Merged = Merged[~isin_col2]
sub_Merged


import matplotlib.pyplot as plt
Merged["LabeltoBGI_BGI"].value_counts().plot(y="Repeticiones") # cuantas veces hay cada elemento de esta columna
plt.hold(True)
plt.xticks(range(1,246), Merged["LabeltoBGI_BGI"], rotation=45)
SamplesTPFS.Sample_Name.value_counts().plot(y="Repeticiones")# cuantas veces hay cada elemento de esta columna

# Cuántas hay en el archivo de merged de LF? 246 
Merged.LabeltoBGI_BGI.count() 
# Según el archivo de LF, de esas 246 cuántas se mandaron a secuenciar? 222
Merged.SampleName_BGI.count()  
# Cuántas hay en el archivo de SamplesToPrepareForSequencing? 248
SamplesTPFS.Label_to_BGI.count()

# Cuál es la diferencia entre los dos archivos? M3 y M6 no entraron al mergedLFGO
sub_SamplesTPF[["ID_PG", "ID_nuevo_PG","ID_nuevo_PGc","Label_to_BGI"]]
