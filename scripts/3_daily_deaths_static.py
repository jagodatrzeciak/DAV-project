from matplotlib import pyplot as plt
import matplotlib.dates as mdates

from utils import read_data_country

df_world, df_sweden = read_data_country()

plt.figure(figsize=(10,6))
plt.plot(df_sweden.index, df_sweden['new_deaths'], color='#882255')

date_format = mdates.DateFormatter('%b., %Y')
plt.gca().xaxis.set_major_formatter(date_format)

plt.title("Daily COVID-19 Deaths in Sweden (2020-2024)", fontsize=20)
plt.ylabel('Number of deaths', fontsize=14)
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("../plots/3_daily_deaths_static.png")
