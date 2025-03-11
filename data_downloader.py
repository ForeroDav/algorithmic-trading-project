import logging
from ib_insync import util
from ib_connection import IBConnection

logger = logging.getLogger(__name__)

class IBDataDownloader:
    """
    Clase encargada de descargar datos históricos utilizando una conexión existente a IB API.
    """
    def __init__(self, connection: IBConnection):
        self.connection = connection

    def download_historical_data(self, contract, duration="1 D", bar_size="1 hour",
                                 what_to_show="MIDPOINT", use_rth=True):
        """
        Descarga datos históricos para el contrato especificado.
        
        Parámetros:
            contract: Objeto contrato de IB, previamente creado.
            duration (str): Duración de los datos a solicitar.
            bar_size (str): Intervalo de cada barra.
            what_to_show (str): Tipo de dato a solicitar.
            use_rth (bool): Si se usan solo los datos del horario regular de negociación.
        
        Retorna:
            pandas.DataFrame: Datos históricos convertidos a DataFrame.
        """
        try:
            bars = self.connection.ib.reqHistoricalData(
                contract,
                endDateTime='',  # Fecha final: '' utiliza la fecha y hora actuales
                durationStr=duration,
                barSizeSetting=bar_size,
                whatToShow=what_to_show,
                useRTH=use_rth,
                formatDate=1
            )
            df = util.df(bars)
            logger.info("Se han descargado %d barras para %s", len(bars), contract.symbol)
            return df
        except Exception as e:
            logger.error("Error al descargar datos históricos: %s", e)
            raise