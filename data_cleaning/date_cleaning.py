"""
    Esta función trasnforma los datos de la columa 'fecha' de una lista de DataFrames
"""

def convert_date_list(lista_df):
    
    """
        Esta funcion recorre una lista de DataFrames y en cada uno de ellos convierte el tipo 
        de datos en la columna 'fecha' transformándolos a tipo DateTime64 
        Parámetros: 
            Lista_df (lista): lista con dataframes
        Returns:
            lista_df (lista): lista con DataFrames con la columna 'fecha' en formato DateTime64
    """

    for df in lista_df:
        
        df['fechaHora'] = df['fechaHora'].dt.strftime('%Y-%m-%d')
        #Organizamos el df por la columna fechaHora de forma ascendente
        df.sort_values(by='fechaHora', ascending=True, inplace=True)
        #eliminamos las filas que tienen la fecha duplicada y sólo dejamos el último
        df.drop_duplicates(subset='fechaHora', keep='last', inplace=True)
        #Reseteamos el los indices
        df.reset_index(drop=True, inplace=True)
              
    return lista_df