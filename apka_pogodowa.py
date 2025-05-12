import pandas as pd
import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets



# Wczytanie danych z pliku CSV
df = pd.read_csv("weather_2024.csv", parse_dates=["date"])

# Podgląd danych
print(df.head())


#srednia kroczaca
df["temp_avg"] = df["temperature"].rolling(window=7).mean()


#wykrywanie anomalii
mean_temp = df["temperature"].mean()
std_temp = df["temperature"].std()
df["is_anomaly"] = (df["temperature"] > mean_temp + 2 * std_temp) | (df["temperature"] < mean_temp - 2 * std_temp)


#grupowanie msc
df_monthly = df.groupby(df["date"].dt.month).mean()


#korelacja

correlation_matrix = df[["temperature", "humidity", "precipitation"]].corr()
print(correlation_matrix)


app = QtWidgets.QApplication([])
win = pg.GraphicsLayoutWidget(show=True)

# Wykres liniowy
plot = win.addPlot(title="Temperatura i średnia krocząca")
plot.plot(df["date"], df["temperature"], pen="b", name="Temperatura")
#plot.plot(df["date"], df["rolling_avg"], pen="r", name="Średnia krocząca")

# Wykres słupkowy
win.nextRow()
bar_plot = win.addPlot(title="Miesięczne opady")
bar_plot.plot(df_monthly.index, df_monthly["precipitation"], pen=None, symbol="s", symbolBrush="g")

app.exec_()