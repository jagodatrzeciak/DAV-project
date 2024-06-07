from matplotlib import pyplot as plt
import matplotlib.dates as mdates

from utils import read_data_country

df_world, df_sweden = read_data_country()

fig, ax1 = plt.subplots(figsize=(10, 6))

color = '#44AA99'
ax1.set_xlabel('Date')
ax1.set_ylabel('Deaths per million citizens', color=color)
ax1.plot(df_sweden.index, df_sweden['new_cases_smoothed_per_million'], label='Deaths', color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = '#882255'
ax2.set_ylabel('Stringency Index', color=color)
ax2.plot(df_sweden.index, df_sweden['stringency_index'], label='Stringency Index', color=color)
ax2.tick_params(axis='y', labelcolor=color)

date_format = mdates.DateFormatter('%b, %Y')
ax1.xaxis.set_major_formatter(date_format)

plt.title(f"Stringency Index and Number of COVID-19\nDeath Cases in Sweden", fontsize=20)
fig.tight_layout()
plt.xticks(rotation=30)
plt.savefig("../plots/8_stringency_index_vs_deaths.png")
