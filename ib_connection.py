from ib_insync import IB, util
import logging
from config import IB_HOST, IB_PORT, IB_CLIENT_ID

logger = logging.getLogger(__name__)

class IBConnection:
    """
    Clase encargada de gestionar la conexión a la API de Interactive Brokers.
    """
    def __init__(self, host=IB_HOST, port=IB_PORT, client_id=IB_CLIENT_ID):
        self.host = host
        self.port = port
        self.client_id = client_id
        self.ib = IB()

    def connect(self):
        """Establece la conexión con la API de IB."""
        try:
            util.startLoop()
            self.ib.connect(self.host, self.port, clientId=self.client_id)
            logger.info("Conexión establecida con IB API en %s:%s", self.host, self.port)
        except Exception as e:
            logger.error("Error al conectar con IB API: %s", e)
            raise

    def disconnect(self):
        """Desconecta de la API de IB."""
        self.ib.disconnect()
        logger.info("Desconectado de IB API")
