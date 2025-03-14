# index_manager.py

from index_scrapers import IndexScraper

class IndexManager:
    def __init__(self):
        self.scrapers = {}
    
    def register_scraper(self, index_name: str, scraper: IndexScraper):
        """Registra un scraper para un índice dado."""
        self.scrapers[index_name] = scraper

    def get_tickers_by_index(self, index_name: str) -> list:
        """Obtiene los tickers para un índice registrado."""
        if index_name not in self.scrapers:
            raise ValueError(f"El índice '{index_name}' no está registrado.")
        return self.scrapers[index_name].get_tickers()

    def get_all_tickers(self) -> dict:
        """Devuelve un diccionario con los tickers de todos los índices registrados."""
        return {index_name: scraper.get_tickers() for index_name, scraper in self.scrapers.items()}
