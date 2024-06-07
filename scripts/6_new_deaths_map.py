from matplotlib import pyplot as plt, animation

from utils import read_regional_data, WEEKS_TO_MONTHS

data_proj, new_deaths = read_regional_data("sweden_new_deaths")
new_deaths_regions = data_proj.merge(new_deaths, on='Region')
new_deaths_regions = new_deaths_regions.dropna(axis=1, how='all')

fig, ax = plt.subplots(1, figsize=(5, 6))
max_val = new_deaths.max(axis=1, numeric_only=True).max()
min_val = new_deaths.min(axis=1, numeric_only=True).min()
sm = plt.cm.ScalarMappable(cmap='Reds', norm=plt.Normalize(vmin=min_val, vmax=max_val))
cbar = fig.colorbar(sm, ax=plt.gca())

def update(frame):
    plt.cla()
    column = new_deaths_regions.columns[2:][frame]
    year = column.split(" ")[0]
    week = column.split(" ")[1]
    month = WEEKS_TO_MONTHS[year][week]
    ax.axis('off')
    ax.set_title(f'New COVID-19 Deaths in Sweden\n{month} {year}', fontdict={'fontsize': '18', 'fontweight' : '3'})
    new_deaths_regions.plot(column=column, cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.8', norm=plt.Normalize(vmin=min_val, vmax=max_val))

anim = animation.FuncAnimation(fig, update, frames=len(new_deaths_regions.columns[2:]))
anim.save("../plots/6_new_deaths_map.gif")
