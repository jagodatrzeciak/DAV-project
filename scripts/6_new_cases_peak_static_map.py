from matplotlib import pyplot as plt

from utils import read_regional_data

data_proj, new_cases = read_regional_data("sweden_new_cases")
new_cases_regions = data_proj.merge(new_cases, on='Region')
new_cases_regions = new_cases_regions.dropna(axis=1, how='all')

fig, ax = plt.subplots(1, figsize=(5, 6))
ax.axis('off')
max_val = new_cases_regions['2022 w3'].max()
min_val = 0
sm = plt.cm.ScalarMappable(cmap='Reds', norm=plt.Normalize(vmin=min_val, vmax=max_val))
ax.set_title('New COVID-19 Cases in Sweden\nJanuary 2022', fontdict={'fontsize': '18', 'fontweight': '3'})
fig.colorbar(sm, ax=ax)
new_cases_regions.plot(column='2022 w4', cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.8',norm=plt.Normalize(vmin=min_val, vmax=max_val))

plt.savefig("../plots/6_new_cases_peak_static_map.png")
