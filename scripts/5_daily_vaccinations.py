import plotly.graph_objects as go

from utils import read_data_country

df_world, df_sweden = read_data_country()
vacc_sweden = df_sweden[~df_sweden['new_vaccinations_smoothed'].isna()]

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=vacc_sweden.index,
    y=vacc_sweden['new_vaccinations_smoothed'],
    mode='lines',
    line=dict(color='#882255'),
    name='Sweden',
    fill='tozeroy'
))
fig.update_layout(
    title="Daily Number of Vaccinations in Sweden (2020-2024)",
    title_x=0.5,
    xaxis_title='',
    yaxis_title='Number of vaccinations',
    xaxis=dict(
        tickformat='%b, %Y',
        tickangle=45
    ),
    template='plotly_white',
)
fig.write_html("../plots/5_daily_vaccinations.html")
