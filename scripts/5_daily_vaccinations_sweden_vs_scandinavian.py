import plotly.graph_objects as go
import pandas as pd

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

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=vacc_sweden.index,
    y=vacc_sweden['new_vaccinations_smoothed_per_million'],
    mode='lines',
    line=dict(color='#882255'),
    name='Sweden'
))
fig.add_trace(go.Scatter(
    x=vacc_norway.index,
    y=vacc_norway['new_vaccinations_smoothed_per_million'],
    mode='lines',
    line=dict(color='#44AA99'),
    name='Norway'
))
fig.add_trace(go.Scatter(
    x=vacc_finland.index,
    y=vacc_finland['new_vaccinations_smoothed_per_million'],
    mode='lines',
    line=dict(color='#DDCC77'),
    name='Finland'
))
fig.update_layout(
    title="Daily Number of Vaccinations in Sweden, Norway and Finland<br>per Million Citizens",
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
fig.write_html("../plots/5_daily_vaccinations_sweden_vs_scandinavian.html")
