import yfinance as yf

def descargar_datos(activo):
    print(activo)
    return yf.Ticker(activo).history(period="max")[['Close', 'Volume']]
    
