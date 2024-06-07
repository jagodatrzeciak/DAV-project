import plotly.graph_objects as go
import pandas as pd

from utils import read_data_country

df_world, df_sweden = read_data_country()
df_poland = df_world[df_world['location'] == 'Poland']
df_poland['date'] = pd.to_datetime(df_poland['date'])
df_poland.set_index('date', inplace=True)

vacc_sweden = df_sweden[~df_sweden['new_vaccinations_smoothed_per_million'].isna()]
vacc_poland = df_poland[~df_poland['new_vaccinations_smoothed_per_million'].isna()]

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=vacc_sweden.index,
    y=vacc_sweden['new_vaccinations_smoothed_per_million'],
    mode='lines',
    line=dict(color='#882255'),
    name='Sweden'
))
fig.add_trace(go.Scatter(
    x=vacc_poland.index,
    y=vacc_poland['new_vaccinations_smoothed_per_million'],
    mode='lines',
    line=dict(color='#6699CC'),
    name='Poland'
))
fig.update_layout(
    title="Daily Number of Vaccinations in Poland and Sweden<br>per Million Citizens",
    title_x=0.5,
    xaxis_title='',
    yaxis_title='Number of vaccinations per million citizens',
    xaxis=dict(
        tickformat='%b, %Y',
        tickangle=45
    ),
    template='plotly_white',
    legend_title_text='Country'
)
fig.write_html("../plots/5_daily_vaccinations_sweden_vs_poland.html")
