"""
    Created on Tue May 14 23:42:51 2024
    Script para generar cálculo de USD mep en Argentina
    @author: Facu
"""

import pandas as pd
import openpyxl
import numpy as np
import matplotlib.pyplot as plt
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

#Filtro merge_df con columnas que necesito y elimino datos Nan
usdmep = merge_df[['fechaHora','ultimoPrecio_x','ultimoPrecio_y']]
usdmep = usdmep.dropna(subset='ultimoPrecio_y')

#Realizo cálculo para obtener cotización de dólar mep
usdmep['usdmep'] = round(usdmep['ultimoPrecio_x'] / usdmep['ultimoPrecio_y'] ,2)

#Renomabro la columnas y transformo los datos a su formato correcto
usdmep = usdmep.rename(columns={
        'fechaHora': 'fecha',
        'ultimoPrecio_x': 'al30',
        'ultimoPrecio_y': 'al30d',
        })

usdmep['fecha'] = pd.to_datetime(usdmep['fecha'])
usdmep['usdmep'] = usdmep['usdmep'].astype(float)

#Calculo promedios moviles 5 y 20 períodos
usdmep['mm5p'] = usdmep['usdmep'].rolling(window=5).mean()
usdmep['mm20p'] = usdmep['usdmep'].rolling(window=20).mean()
#Calculo los retornos
usdmep['retorno'] = np.log(usdmep['usdmep'] / usdmep['usdmep'].shift(1))
usdmep = usdmep.drop(usdmep.index[0])
#Calculo la volatilidad de 5 y 20 períodos
usdmep['volHis5'] = usdmep['retorno'].rolling(window=5).std() * np.sqrt(260)
usdmep['volHis20'] = usdmep['retorno'].rolling(window=20).std() * np.sqrt(260)

# Configuración del gráfico
plt.figure(figsize=(10, 5))  # Tamaño del gráfico en pulgadas (800x400 píxeles)
plt.plot(usdmep['fecha'],usdmep['usdmep'], linestyle='-')  # Graficar los datos
plt.title('Gráfico de Precios')  # Título del gráfico
plt.xlabel('Fecha')  # Etiqueta del eje x
plt.ylabel('Precio')  # Etiqueta del eje y
plt.xticks(rotation=45)  # Rotar las etiquetas del eje x para que sean legibles
plt.grid(True)  # Mostrar cuadrícula en el gráfico

# Ajustar diseño del gráfico
plt.tight_layout()

plt.savefig('./data/final/usd-mep_plot.png', dpi=300)
