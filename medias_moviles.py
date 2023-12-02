import matplotlib.pyplot as plt
import numpy as np
from descargar_datos import descargar_datos

def calcular_medias_moviles(datos, nombre_empresa, activo):
    datos['SMA_50'] = datos['Close'].rolling(window=50).mean()
    datos['EMA_20'] = datos['Close'].ewm(span=20, adjust=False).mean()
    datos['EMA_100'] = datos['Close'].ewm(span=100, adjust=False).mean()
    datos['EMA_200'] = datos['Close'].ewm(span=200, adjust=False).mean()

    datos['Signal'] = 0
    datos['Signal'][50:] = np.where(datos['SMA_50'][50:] > datos['EMA_200'][50:], 1, 0)
    datos['Position'] = datos['Signal'].diff()

    datos['ShortEMA'] = datos['Close'].ewm(span=12, adjust=False).mean()
    datos['LongEMA'] = datos['Close'].ewm(span=26, adjust=False).mean()
    datos['MACD'] = datos['ShortEMA'] - datos['LongEMA']
    datos['Signal_Line'] = datos['MACD'].ewm(span=9, adjust=False).mean()

    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    ax1.plot(datos['Close'], label='Precio de Cierre', alpha=0.7)
    ax1.plot(datos['SMA_50'], label='SMA 50', linestyle='-', color='orange')
    ax1.plot(datos['EMA_20'], label='EMA 20', linestyle='-', color='red')
    ax1.plot(datos['EMA_100'], label='EMA 100', linestyle='-', color='aqua')
    ax1.plot(datos['EMA_200'], label='EMA 200', linestyle='--', color='white')

    golden_cross_points = datos[datos['Position'] == 1].index
    death_cross_points = datos[datos['Position'] == -1].index

    ax1.plot(golden_cross_points, datos['SMA_50'].loc[golden_cross_points], '^', markersize=8, color='g', label='Golden Cross')
    ax1.plot(death_cross_points, datos['SMA_50'].loc[death_cross_points], 'v', markersize=8, color='r', label='Death Cross')

    ax1.set_title(f'Gráfico de {nombre_empresa} ({activo})')
    ax1.set_ylabel('Precio', color='white')
    ax1.legend(loc='upper left')

    ax2.plot(datos['MACD'], label='MACD', color='blue')
    ax2.plot(datos['Signal_Line'], label='Signal Line', color='red')

    ax2.fill_between(datos.index, 0, datos['MACD'] - datos['Signal_Line'], where=(datos['MACD'] > datos['Signal_Line']), facecolor='green', alpha=0.3)
    ax2.fill_between(datos.index, 0, datos['MACD'] - datos['Signal_Line'], where=(datos['MACD'] <= datos['Signal_Line']), facecolor='red', alpha=0.3)

    ax2.set_xlabel('Fecha')
    ax2.set_ylabel('MACD', color='white')
    ax2.legend(loc='upper left')

    plt.tight_layout()
    plt.show()

fscope = open("scope.txt", "r")
scope = fscope.read().splitlines()
fscope.close()

for linea in scope:
    activo, nombre_empresa = map(str.strip, linea.split('/'))
    
    datos = descargar_datos(activo)
    calcular_medias_moviles(datos, nombre_empresa, activo)
