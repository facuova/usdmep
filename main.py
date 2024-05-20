"""
    Created on Tue May 14 23:42:51 2024
    Script para generar cálculo de USD mep en Argentina
    @author: Facu
"""

import pandas as pd
import openpyxl
from data_cleaning.date_cleaning import convert_date_list

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

#Formato la columna fechaHora a tipo datetime
al30_df['fechaHora'] = pd.to_datetime(
    al30_df['fechaHora'],
    errors='coerce',
    format='%Y-%m-%dT%H:%M:%S.%f')

al30d_df['fechaHora'] = pd.to_datetime(
    al30d_df['fechaHora'],
    errors='coerce',
    format='%Y-%m-%dT%H:%M:%S.%f')

#Agrupo df en una lista
lista_df = [al30_df,al30d_df]

#Ejecuto función de limpieza de fecha, para eliminar los datos intradiarios
convert_date_list(lista_df)

#Realizo merge
merge_df = pd.merge(lista_df[0], lista_df[1], how='left', on='fechaHora')
#Elimino datos Nan
merge_df = merge_df.dropna(subset='fechaHora')
#Filtro merge_df con columnas que necesito
df_final = merge_df[['fechaHora','ultimoPrecio_x','ultimoPrecio_y']]
#Realizo cálculo para obtener cotización de dólar mep
df_final['usd_mep'] = round(df_final['ultimoPrecio_x'] / df_final['ultimoPrecio_y'] ,2)
#Renomabramos la columnas
df_final = df_final.rename(columns={
        'fechaHora': 'fecha',
        'ultimoPrecio_x': 'al30',
        'ultimoPrecio_y': 'al30d',
        })
