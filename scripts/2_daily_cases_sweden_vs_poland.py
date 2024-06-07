import plotly.graph_objects as go
import pandas as pd

from utils import read_data_country

df_world, df_sweden = read_data_country()
df_poland = df_world[df_world['location'] == 'Poland']
df_poland['date'] = pd.to_datetime(df_poland['date'])
df_poland.set_index('date', inplace=True)

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df_sweden.index,
    y=df_sweden['new_cases_per_million'],
    mode='lines',
    line=dict(color='#882255'),
    name='Sweden'
))
fig.add_trace(go.Scatter(
    x=df_poland.index,
    y=df_poland['new_cases_per_million'],
    mode='lines',
    line=dict(color='#6699CC'),
    name='Poland'
))
fig.update_layout(
    title="Daily COVID-19 Cases in Poland and Sweden\nper Million Citizens",
    title_x=0.5,
    xaxis_title='',
    yaxis_title='Number of cases',
    xaxis=dict(
        tickformat='%b, %Y',
        tickangle=45
    ),
    template='plotly_white',
    legend_title_text='Country'
)
fig.write_html("../plots/2_daily_cases_sweden_vs_poland.html")
