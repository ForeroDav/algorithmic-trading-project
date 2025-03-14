import logging

# Configuración básica de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuración de la conexión a IB API
IB_HOST = '127.0.0.1'
IB_PORT = 7496
IB_CLIENT_ID = 1

