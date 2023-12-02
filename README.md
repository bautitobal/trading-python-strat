# Trading: Medias Móviles y Análisis Técnico

Este proyecto utiliza medias móviles e indicadores como el MACD (Moving Average Convergence Divergence), para visualizar y analizar datos históricos de precios de activos financieros. La aplicación descarga datos de Yahoo Finance, calcula medias móviles simples y exponenciales, y genera gráficos con señales de Golden Cross y Death Cross.

**Atención: la información brindada NO debe ser tomada como recomendación de Trading, asesoramiento financiero, estímulo a invertir en instrumentos financieros tales como acciones, divisas, futuros, cripto, entre otras o como guía a seguir de la misma.** 

## Requisitos

- Python 3.x
- Bibliotecas requeridas: [`matplotlib`](https://matplotlib.org/), [`numpy`](https://numpy.org/), [`yfinance`](https://pypi.org/project/yfinance/)

## Instalación de Dependencias

```bash
pip install matplotlib numpy yfinance 
```
# 
# Estructura del Proyecto
- [`descargar_datos.py`](descargar_datos.py): Módulo para la descarga de datos históricos de Yahoo Finance.
- [`medias_moviles.py`](medias_moviles.py): Módulo principal que realiza el cálculo de medias móviles y genera gráficos.
- [`main.py`](main.py): Archivo de entrada que ejecuta el análisis para los activos especificados en [`scope.txt`](scope.txt). 

# Uso
1. Modifica el archivo [scope.txt](scope.txt) para incluir los activos financieros deseados. Cada línea debe seguir el formato "`ticker` / `nombre_empresa`".
2. Ejecuta [main.py](main.py) para realizar el análisis y generar gráficos.

# Personalización 
- Puedes ajustar las fechas de inicio y fin en el archivo [descargar_datos.py](descargar_datos.py) según tus necesidades.
- Personaliza las medias móviles y otros parámetros en [medias_moviles.py](medias_moviles.py) según tus preferencias.

# Contribuciones
Las contribuciones son bienvenidas, si encuentras algún problema o tenés ideas de mejora, no dudes en abrir una solicitud de extracción o hacer un commit!
También me puedes apoyar con un [Ko-Fi](https://ko-fi.com/bautitobal)

# License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.