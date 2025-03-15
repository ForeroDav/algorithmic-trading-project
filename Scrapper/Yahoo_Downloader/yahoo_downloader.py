import yfinance as yf
import logging

logger = logging.getLogger(__name__)

class YahooFinanceDownloader:
    """
    Clase para descargar datos históricos de Yahoo Finance.

    Ejemplo de uso:
        downloader = YahooFinanceDownloader()
        data = downloader.download_data(tickers="AAPL", start_date="2020-01-01")
        print(data)
    """
    def __init__(self):
        pass

    def download_data(self, tickers, start_date, end_date=None, interval="1d", group_by='ticker'):
        """
        Descarga datos históricos de los tickers proporcionados.

        Parámetros:
            tickers (str o lista de str): Ticker(s) para descargar.
            start_date (str): Fecha de inicio en formato 'YYYY-MM-DD'.
            end_date (str): Fecha final en formato 'YYYY-MM-DD'. Si es None, se descarga hasta la fecha actual.
            interval (str): Intervalo para las barras de datos (ej. '1d' para diario, '1h' para cada hora).
            group_by (str): Método para agrupar los datos; por defecto 'ticker'.

        Retorna:
            DataFrame o dict: Datos históricos descargados.
        """
        try:
            logger.info("Descargando datos de Yahoo Finance para tickers: %s", tickers)
            data = yf.download(tickers=tickers, start=start_date, end=end_date, interval=interval, group_by=group_by)
            logger.info("Descarga completa para los tickers: %s", tickers)
            return data
        except Exception as e:
            logger.error("Error en la descarga de datos: %s", e)
            raise

if __name__ == "__main__":
    # Ejemplo de uso del módulo
    downloader = YahooFinanceDownloader()
    # Aquí puedes definir tus tickers y la fecha de inicio (por ejemplo, la última actualización)
    data = downloader.download_data(tickers="AAPL", start_date="2020-01-01")
    print(data)
