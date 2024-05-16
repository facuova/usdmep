"""
    Created on Tue May 14 23:42:51 2024
    Script para generar cálculo de USD mep en Argentina
    @author: Facu
"""

import pandas as pd
import openpyxl

AL30_FILE_PATH = './data/AL30.xlsx' 
AL30D_FILE_PATH = './data/AL30D.xlsx'

al30_libro = openpyxl.load_workbook(filename=AL30_FILE_PATH)
al30d_libro = openpyxl.load_workbook(filename=AL30D_FILE_PATH)

hoja_al30 = al30_libro.active
hoja_al30d = al30d_libro.active

#Obbtener titulos
titulos_al30 = next(hoja_al30.values)[0:]
titulos_al30d = next(hoja_al30d.values)[0:]

#Crear dataframe
al30_df = pd.DataFrame(hoja_al30.values,columns=titulos_al30)
al30d_df = pd.DataFrame(hoja_al30d.values,columns=titulos_al30d)

#Borrar primera fila
al30_df = al30_df.drop(al30_df.index[0])
al30d_df = al30d_df.drop(al30d_df.index[0])

al30_df['fechaHora'] = pd.to_datetime(al30_df['fechaHora'], 
                                      errors='coerce', format='%Y-%m-%dT%H:%M:%S.%f')
al30d_df['fechaHora'] = pd.to_datetime(al30d_df['fechaHora'], 
                                       errors='coerce', format='%Y-%m-%dT%H:%M:%S.%f')

print(al30d_df)