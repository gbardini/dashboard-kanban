import pandas as pd

# Função para verificar e converter a coluna "Aberto em"
def convert_to_date(date_series):
    valid_dates = []
    for date in date_series:
        try:
            valid_date = pd.to_datetime(date, errors='raise').date()  # Converte para data
            valid_dates.append(valid_date)
        except Exception:
            valid_dates.append(None)  # Manter como None se não for uma data válida
    return valid_dates