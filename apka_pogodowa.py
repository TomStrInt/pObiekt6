import pandas as pd

# Wczytanie danych z pliku CSV
df = pd.read_csv("weather_2024.csv", parse_dates=["date"])

# Podgląd danych
print(df.head())


#srednia kroczaca
df["temp_avg"] = df["temperature"].rolling(window=7).mean()
