import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.dates as mdates

from utils import read_data_country

df_world, df_sweden = read_data_country()
df_finland = df_world[df_world['location'] == 'Finland']
df_finland['date'] = pd.to_datetime(df_finland['date'])
df_finland.set_index('date', inplace=True)
df_poland = df_world[df_world['location'] == 'Poland']
df_poland['date'] = pd.to_datetime(df_poland['date'])
df_poland.set_index('date', inplace=True)

plt.figure(figsize=(10,6))
plt.plot(df_poland.index, df_poland['stringency_index'], label='Poland', color='#44AA99')
plt.plot(df_sweden.index, df_sweden['stringency_index'], label='Sweden', color='#882255')
plt.plot(df_finland.index, df_finland['stringency_index'], label='Finland', color='#DDCC77')

date_format = mdates.DateFormatter('%b., %Y')
plt.gca().xaxis.set_major_formatter(date_format)

plt.title("Strigency index in Sweden, Poland and Finland", fontsize=20)
plt.ylabel('Strigency index', fontsize=14)
plt.legend()
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("../plots/8_strigency_index.png")
