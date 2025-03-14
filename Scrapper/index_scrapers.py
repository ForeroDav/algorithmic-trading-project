# index_scrapers.py

import pandas as pd
from abc import ABC, abstractmethod

class IndexScraper(ABC):
    @abstractmethod
    def fetch_data(self) -> pd.DataFrame:
        """Obtiene y procesa los datos crudos del índice."""
        pass

    @abstractmethod
    def get_tickers(self) -> list:
        """Devuelve la lista de tickers del índice."""
        pass

class DowJonesScraper(IndexScraper):
    URL = "https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average"

    def fetch_data(self) -> pd.DataFrame:
        df_list = pd.read_html(self.URL)
        target_df = None
        for df in df_list:
            if "Date added" in df.columns:
                target_df = df.copy()
                break
        if target_df is None:
            raise ValueError("No se encontró la tabla esperada en la página de Dow Jones.")
        
        # Renombrar columnas y transformar datos
        target_df.rename(columns={"Date added": "Date_Added", "Index weighting": "Weights"}, inplace=True)
        target_df["Date_Added"] = pd.to_datetime(target_df["Date_Added"])
        target_df["Weights"] = pd.to_numeric(target_df["Weights"].str.replace("%", ""), errors="coerce")
        if "Notes" in target_df.columns:
            target_df.drop(columns="Notes", inplace=True)
        target_df.set_index("Symbol", inplace=True)
        return target_df

    def get_tickers(self) -> list:
        df = self.fetch_data()
        return df.index.tolist()

class SP500Scraper(IndexScraper):
    URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    
    def fetch_data(self) -> pd.DataFrame:
        df = pd.read_html(self.URL)[0]
        df.set_index("Symbol", inplace=True)
        return df

    def get_tickers(self) -> list:
        df = self.fetch_data()
        return df.index.tolist()