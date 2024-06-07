import plotly.graph_objects as go

from utils import read_data_country

df_world, df_sweden = read_data_country()
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df_sweden.index,
    y=df_sweden['total_tests'],
    mode='lines',
    line=dict(color='#882255'),
    name='Sweden',
    fill='tozeroy'
))
fig.update_layout(
    title="Total COVID-19 Tests in Sweden (2020-2024)",
    title_x=0.5,
    xaxis_title='',
    yaxis_title='Number of tests',
    xaxis=dict(
        range=['2020-01-01', '2022-07-01'],
        tickformat='%b, %Y',
        tickangle=45
    ),
    template='plotly_white',
)
fig.write_html("../plots/4_total_tests.html")
