"""
    Función ploteo 
"""
import matplotlib.pyplot as plt

def plot_close(df,name):
    """
        Función para realizar gráfico de precios de cierre completo
        Parámetros:
            df (dataframe) : dataframe que debe contar con las columnas 'fecha' y 'usdmep'
            name (str) : nombre de titulo y con el que se desea guardar el archivo
    """
    # Configuración del gráfico
    plt.figure(figsize=(10, 5))
    plt.plot(df['fecha'],df['usdmep'], linestyle='-', label=name)
    plt.title(f'{name}')
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.xticks(rotation=45)
    plt.grid(True)  # Mostrar cuadrícula en el gráfico
    plt.legend(loc='upper left', fontsize='small')
    plt.xlim(df['fecha'].min(),df['fecha'].max())
    # Ajustar diseño del gráfico
    plt.tight_layout()

    plt.savefig(f'./data/final/{name}_plot.png', dpi=300)

def plot_line(df,columns, name):
    """
        Función para realizar gráfico de línea de los últimos 126 peridos(medio año) 
        Parámetros:
            df (dataframe) : DataFrame
            columns (str): Debe indicar las columnas a graficar
            name (str): Nombre de título y de archivo con el que queremos que se guarde
        Return:
            plot.png: Archivo .png con el gráfico realizado en 
    """

    # Configuración del gráfico
    plt.figure(figsize=(10, 5))
    plt.plot(df['fecha'].tail(126),df[columns].tail(126), linestyle='-', label=columns)
    plt.title(f'{name}')
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.xticks(rotation=45)
    plt.grid(True)  # Mostrar cuadrícula en el gráfico
    plt.legend(loc='upper left', fontsize='small')
    plt.xlim(df['fecha'].tail(126).min(),df['fecha'].tail(126).max())
    # Ajustar diseño del gráfico
    plt.tight_layout()

    plt.savefig(f'./data/final/{name}_plot.png', dpi=300)