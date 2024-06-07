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

vacc_sweden = df_sweden[~df_sweden['new_vaccinations_smoothed_per_million'].isna()]
vacc_norway = df_norway[~df_norway['new_vaccinations_smoothed_per_million'].isna()]
vacc_finland = df_finland[~df_finland['new_vaccinations_smoothed_per_million'].isna()]

plt.figure(figsize=(10,6))
plt.plot(vacc_sweden.index, vacc_sweden['new_vaccinations_smoothed_per_million'], color='#882255', label='Sweden')
plt.plot(vacc_norway.index, vacc_norway['new_vaccinations_smoothed_per_million'], color='#44AA99', label='Norway')
plt.plot(vacc_finland.index, vacc_finland['new_vaccinations_smoothed_per_million'], color='#DDCC77', label='Finland')

date_format = mdates.DateFormatter('%b., %Y')
plt.gca().xaxis.set_major_formatter(date_format)

plt.title("Daily Number of Vaccinations in Sweden, Norway and Finland\nper Million Citizens", fontsize=20)
plt.ylabel('Number of vaccinations', fontsize=14)
plt.xticks(rotation=30)
plt.tight_layout()
plt.legend()
plt.savefig("../plots/5_daily_vaccinations_sweden_vs_scandinavian_static.png")
