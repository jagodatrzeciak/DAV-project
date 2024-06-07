import plotly.graph_objects as go

from utils import read_data_country

df_world, df_sweden = read_data_country()
vacc_sweden = df_sweden[~df_sweden['people_vaccinated'].isna()]
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=vacc_sweden.index,
    y=vacc_sweden['people_vaccinated'],
    mode='lines',
    line=dict(color='#882255'),
    name='Sweden'
))
fig.update_layout(
    title="Total Number of Vaccinated People in Sweden (2020-2024)",
    title_x=0.5,
    xaxis_title='',
    yaxis_title='Number of people',
    xaxis=dict(
        tickformat='%b, %Y',
        tickangle=45
    ),
    template='plotly_white',
)
fig.write_html("../plots/5_total_vaccinations.html")
