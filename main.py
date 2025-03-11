from ib_connection import IBConnection
from data_downloader import IBDataDownloader
from contract_factory import create_contract

def main():
    # Crea la conexión a IB API
    connection = IBConnection()
    connection.connect()
    
    try:
        # Recopilar parámetros del usuario para el contrato
        instrument_type = input("Ingrese el tipo de instrumento (forex, stock, option, future): ").strip().lower()
        symbol = input("Ingrese el símbolo del instrumento: ").strip().upper()
        
        extra_params = {}
        if instrument_type in ["stock", "option", "future"]:
            extra_params["exchange"] = input("Ingrese el exchange (por defecto SMART para stock/option, GLOBEX para future): ").strip() or (
                "SMART" if instrument_type in ["stock", "option"] else "GLOBEX")
            extra_params["currency"] = input("Ingrese la moneda (por defecto USD): ").strip() or "USD"
        
        if instrument_type in ["option", "future"]:
            default_trade = "20230421" if instrument_type == "option" else "202306"
            extra_params["lastTradeDateOrContractMonth"] = input(f"Ingrese lastTradeDateOrContractMonth (por defecto {default_trade}): ").strip() or default_trade
        
        if instrument_type == "option":
            extra_params["strike"] = float(input("Ingrese el strike (por defecto 150): ").strip() or 150)
            extra_params["right"] = input("Ingrese el tipo de opción (C o P, por defecto C): ").strip().upper() or "C"
        
        # Crear el contrato usando la fábrica
        contract = create_contract(instrument_type, symbol=symbol, **extra_params)
        
        # Solicitar parámetros para la descarga de datos históricos
        duration = input("Ingrese la duración (por defecto '1 D'): ").strip() or "1 D"
        bar_size = input("Ingrese el bar size (por defecto '1 hour'): ").strip() or "1 hour"
        what_to_show = input("Ingrese el tipo de dato a mostrar (por defecto 'MIDPOINT'): ").strip() or "MIDPOINT"
        use_rth_input = input("¿Usar solo horario regular de negociación? (s/n, por defecto s): ").strip().lower() or "s"
        use_rth = True if use_rth_input == "s" else False
        
        # Crear el descargador de datos utilizando la conexión
        downloader = IBDataDownloader(connection)
        data_df = downloader.download_historical_data(contract,
                                                      duration=duration,
                                                      bar_size=bar_size,
                                                      what_to_show=what_to_show,
                                                      use_rth=use_rth)
        print(data_df)
    finally:
        connection.disconnect()

if __name__ == "__main__":
    main()
