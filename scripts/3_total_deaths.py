import plotly.graph_objects as go

from utils import read_data_country

df_world, df_sweden = read_data_country()
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df_sweden.index,
    y=df_sweden['total_deaths'],
    mode='lines',
    line=dict(color='#882255'),
    name='Sweden'
))
fig.update_layout(
    title="Total COVID-19 Deaths in Sweden (2020-2024)",
    title_x=0.5,
    xaxis_title='',
    yaxis_title='Number of deaths',
    xaxis=dict(
        tickformat='%b, %Y',
        tickangle=45
    ),
    template='plotly_white',
)
fig.write_html("../plots/3_total_deaths.html")
