# Scrapper/Yahoo_Downloader/main.py
from Scrapper.Yahoo_Downloader.yahoo_downloader import YahooFinanceDownloader
from Scrapper.get_tickers import get_dj_tickers

def main():
    dj_tickers = get_dj_tickers()  # Obtenemos los tickers desde el módulo compartido
    
    downloader = YahooFinanceDownloader()
    
    # Descarga de datos históricos para los tickers obtenidos (por ejemplo, de Dow Jones)
    data = downloader.download_data(tickers=dj_tickers, start_date="2025-01-01")
    
    print("Datos descargados para Dow Jones:")
    print(data)

if __name__ == '__main__':
    main()
