from matplotlib import pyplot as plt
import plotly.express as px

from utils import read_data_country

df_world, df_sweden = read_data_country()

plt.figure(figsize=(10,6))
fig = px.line(df_sweden, x=df_sweden.index, y='total_cases', title="Total COVID-19 Cases in Sweden (2020-2024)", color_discrete_sequence=["#882255"])
fig.update_layout(
    title={'text': "Total COVID-19 Cases in Sweden (2020-2024)", 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
    xaxis_title='',
    yaxis_title='Number of cases',
    xaxis=dict(
        tickformat='%b, %Y',
        tickangle=45
    ),
    template='plotly_white'
)
fig.write_html("../plots/2_total_cases.html")
