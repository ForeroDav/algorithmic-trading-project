from ib_insync import Forex, Stock, Option, Future

def create_contract(instrument_type, **kwargs):
    """
    Fabrica un contrato de IB según el tipo de instrumento y parámetros proporcionados.

    Parámetros:
        instrument_type (str): Tipo de instrumento ('forex', 'stock', 'option', 'future').
        kwargs: Parámetros específicos para el contrato, por ejemplo, symbol, exchange, currency, etc.
    
    Retorna:
        Objeto contrato de IB.
    """
    instrument_type = instrument_type.lower()
    
    if instrument_type == 'forex':
        symbol = kwargs.get('symbol', 'EURUSD')
        return Forex(symbol)
    
    elif instrument_type == 'stock':
        symbol = kwargs.get('symbol', 'AAPL')
        exchange = kwargs.get('exchange', 'SMART')
        currency = kwargs.get('currency', 'USD')
        return Stock(symbol, exchange, currency)
    
    elif instrument_type == 'option':
        symbol = kwargs.get('symbol', 'AAPL')
        lastTradeDateOrContractMonth = kwargs.get('lastTradeDateOrContractMonth', '20230421')
        strike = kwargs.get('strike', 150)
        right = kwargs.get('right', 'C')
        exchange = kwargs.get('exchange', 'SMART')
        currency = kwargs.get('currency', 'USD')
        return Option(symbol, lastTradeDateOrContractMonth, strike, right, exchange, currency)
    
    elif instrument_type == 'future':
        symbol = kwargs.get('symbol', 'ES')
        lastTradeDateOrContractMonth = kwargs.get('lastTradeDateOrContractMonth', '202306')
        exchange = kwargs.get('exchange', 'GLOBEX')
        currency = kwargs.get('currency', 'USD')
        return Future(symbol, lastTradeDateOrContractMonth, exchange, currency)
    
    else:
        raise ValueError("Tipo de instrumento no soportado: {}".format(instrument_type))