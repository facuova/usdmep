"""
    Función ploteo 
"""
import matplotlib.pyplot as plt

def plot_close(df,name):
    """
        Función para graficar los precios del cierre
        Parámetros:
            df (dataframe) : dataframe que debe contar con las columnas 'fecha' y 'usdmep'
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

    # Ajustar diseño del gráfico
    plt.tight_layout()

    plt.savefig(f'./data/final/{name}_plot.png', dpi=300)

def plot_line(df,columns, name):
    """
        Función para graficar los precios del 
        Parámetros:
            df (dataframe) : dataframe que debe contar con las columnas 'fecha' y 'usdmep'
    """
    # Configuración del gráfico
    plt.figure(figsize=(10, 5))
    plt.plot(df['fecha'].tail(126),df[columns].tail(126), linestyle='-', label=columns)
    plt.title(f'{name} cierre ')
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.xticks(rotation=45)
    plt.grid(True)  # Mostrar cuadrícula en el gráfico
    plt.legend(loc='upper left', fontsize='small')

    # Ajustar diseño del gráfico
    plt.tight_layout()

    plt.savefig(f'./data/final/{name}_plot.png', dpi=300)