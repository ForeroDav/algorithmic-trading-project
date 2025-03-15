# Scrapper/main.py
from Scrapper.index_manager import IndexManager
from Scrapper.index_scrapers import DowJonesScraper, SP500Scraper

def main():
    manager = IndexManager()
    
    # Registrar los scrapers para cada índice
    manager.register_scraper("Dow Jones", DowJonesScraper())
    manager.register_scraper("S&P 500", SP500Scraper())

    # Obtener y mostrar los tickers para cada índice
    dj_tickers = manager.get_tickers_by_index("Dow Jones")
    sp500_tickers = manager.get_tickers_by_index("S&P 500")
    
    print("Tickers del Dow Jones:", dj_tickers)
    print("Tickers del S&P 500:", sp500_tickers)

if __name__ == '__main__':
    main()
