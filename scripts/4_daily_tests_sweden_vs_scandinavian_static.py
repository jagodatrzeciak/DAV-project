import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.dates as mdates

from utils import read_data_country

df_world, df_sweden = read_data_country()
df_finland = df_world[df_world['location'] == 'Finland']
df_finland['date'] = pd.to_datetime(df_finland['date'])
df_finland.set_index('date', inplace=True)
df_norway = df_world[df_world['location'] == 'Norway']
df_norway['date'] = pd.to_datetime(df_norway['date'])
df_norway.set_index('date', inplace=True)

plt.figure(figsize=(10,6))
plt.plot(df_sweden.index, df_sweden['new_tests'], label='Sweden', color='#882255')
plt.plot(df_norway.index, df_norway['new_tests'], label='Norway', color='#44AA99')
plt.plot(df_finland.index, df_finland['new_tests'], label='Finland', color='#DDCC77')

date_format = mdates.DateFormatter('%b., %Y')
plt.gca().xaxis.set_major_formatter(date_format)

plt.title("Daily COVID-19 Tests in Sweden, Norway and Finland", fontsize=20)
plt.ylabel('Number of tests', fontsize=14)
plt.legend()
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("../plots/4_daily_tests_sweden_vs_scandinavian_static.png")