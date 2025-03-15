# Scrapper/get_tickers.py
from Scrapper.index_manager import IndexManager
from Scrapper.index_scrapers import DowJonesScraper

def get_dj_tickers():
    """
    Configura el scraper para Dow Jones y retorna la lista de tickers.
    """
    manager = IndexManager()
    manager.register_scraper("Dow Jones", DowJonesScraper())
    return manager.get_tickers_by_index("Dow Jones")
