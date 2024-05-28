"""
    En este módulo se encontrar las funciones que se utilizarán para realizar el análisis correspondiente
    medias móviles
    retorno diario
    volatilidad histórica
"""

import numpy as np

def moving_averge(df,columna,numero):
    """
        Esta función calcula el promedio móvil en un dataframe y lo agrega en una nueva columna
        Parámetros:
            df (dataframe): DataFrame que contará con los datos
            columna(str) : Nombre de la columa que se utilizará para el promedio
            numero(int): cantidad de días que queremos que tome para el cálculo
        Returns:
            df(dataframe): DataFrame con cálculo de promediio móvil incorporado
    """
    df[f'mm{numero}p']  = df[columna].rolling(window=numero).mean()    
    return df


def quotes_return(df, columna):
    """
        Esta función calcula el promedio móvil en un dataframe y lo agrega en una nueva columna
        Parámetros:
            df (dataframe): DataFrame que contará con los datos
            columna(str) : Nombre de la columa que se utilizará para calcular los retornos
        Returns:
            df(dataframe): DataFrame con cálculo de retornos incorporado
    """
    df['retorno'] = np.log(df[columna] / df[columna].shift(1))
    
    return df


def historic_valotility(df, numero, columna, anio):
    """
        Esta función calcula la volatilidad historica en un dataframe y lo agrega en una nueva columna
        Parámetros:
            df (dataframe): DataFrame que contará con los datos
            numero(int): Cantidad de días que queremos que tome para el cálculo
            columna(str) : Nombre de la columa que se utilizará para el promedio
            anio(int) : Cantidad de días que se toman el año operativo (Dependerá del activo
            en cuestión)
        Returns:
            df(dataframe): DataFrame con cálculo de volatilidad histórica incorporado
    """
    df[f'volHis{numero}'] = df[columna].rolling(window=numero).std() * np.sqrt(anio)
    return df
