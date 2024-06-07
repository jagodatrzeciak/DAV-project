url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df_world = pd.read_csv(url)
df_sweden = df_world[df_world['location'] == 'Sweden']
df_sweden['date'] = pd.to_datetime(df_sweden['date'])
df_sweden.set_index('date', inplace=True)

df_norway = df_world[df_world['location'] == 'Norway']
df_norway['date'] = pd.to_datetime(df_norway['date'])
df_norway.set_index('date', inplace=True)

df_finland = df_world[df_world['location'] == 'Finland']
df_finland['date'] = pd.to_datetime(df_finland['date'])
df_finland.set_index('date', inplace=True)

df_poland = df_world[df_world['location'] == 'Poland']
df_poland['date'] = pd.to_datetime(df_poland['date'])
df_poland.set_index('date', inplace=True)



#1
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
plt.show()

#2
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
plt.show()

#3
fig, ax1 = plt.subplots(figsize=(10, 6))

color = '#44AA99'
ax1.set_xlabel('Date')
ax1.set_ylabel('Reproduction rate', color=color)
ax1.plot(df_sweden.index, df_sweden['reproduction_rate'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx() 
color = '#882255'
ax2.set_ylabel('People vacccinated per hundred citizens', color=color)
ax2.plot(df_sweden.index, df_sweden['new_people_vaccinated_smoothed_per_hundred'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

date_format = mdates.DateFormatter('%b, %Y')
ax1.xaxis.set_major_formatter(date_format)

plt.title(f"Reproduction rate and Number of people\nvaccinated in Sweden", fontsize=20)
fig.tight_layout()
plt.xticks(rotation=30)
plt.show()


#4
fig, ax1 = plt.subplots(figsize=(10, 6))

color = '#44AA99'
ax1.set_xlabel('Date')
ax1.set_ylabel('ICU patients per hundred', color=color)
ax1.plot(df_sweden.index, df_sweden['icu_patients_per_million'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx() 
color = '#882255'
ax2.set_ylabel('People vacccinated per hundred citizens', color=color)
ax2.plot(df_sweden.index, df_sweden['new_people_vaccinated_smoothed_per_hundred'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

date_format = mdates.DateFormatter('%b, %Y')
ax1.xaxis.set_major_formatter(date_format)

plt.title(f"ICU patients and Number of people\nvaccinated in Sweden", fontsize=20)
fig.tight_layout()
plt.xticks(rotation=30)
plt.show()


#5
plt.figure(figsize=(10,6))
plt.plot(df_norway.index, df_norway['new_deaths_per_million'], label='Norway', color='#44AA99', zorder=3)
plt.plot(df_sweden.index, df_sweden['new_deaths_per_million'], label='Sweden', color='#882255')
plt.plot(df_finland.index, df_finland['new_deaths_per_million'], label='Finland', color='#DDCC77', zorder=2)

date_format = mdates.DateFormatter('%b., %Y')
plt.gca().xaxis.set_major_formatter(date_format)

plt.title("Daily COVID-19 Deaths in Sweden, Norway and Finland\nper Million Citizens", fontsize=20)
plt.ylabel('Number of cases', fontsize=14)
plt.legend()
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
