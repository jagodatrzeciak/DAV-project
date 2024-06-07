import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from statsmodels.tsa.holtwinters import ExponentialSmoothing

from utils import read_data_country


df_world, df_sweden = read_data_country()

deaths_cases_per_million = df_sweden[['new_deaths_smoothed_per_million', 'new_cases_smoothed_per_million']].dropna()
weekly_data = deaths_cases_per_million.resample('W').mean()

train_size = int(len(weekly_data) * 0.75)
train_data, test_data = weekly_data[:train_size], weekly_data[train_size:]

model = ExponentialSmoothing(train_data['new_cases_smoothed_per_million'], trend=None, seasonal="additive", seasonal_periods=49)
fit = model.fit()
test_forecast = fit.forecast(steps=len(test_data))

full_model = ExponentialSmoothing(weekly_data['new_cases_smoothed_per_million'], trend=None, seasonal="additive", seasonal_periods=49)
full_fit = full_model.fit()

future_steps = 52
future_forecast = full_fit.forecast(steps=future_steps)

last_date = weekly_data['new_cases_smoothed_per_million'].index[-1]
future_dates = pd.date_range(start=last_date, periods=future_steps + 1, freq='W')[1:]


plt.figure(figsize=(10, 6))
plt.plot(weekly_data['new_cases_smoothed_per_million'], label='Historical Data', color='#882255')
plt.plot(test_data.index, test_forecast, label='Test Forecast', color='orange')
plt.axvline(x=train_data.index[-1], color='black', linestyle='--', label='Train/Test Split')
plt.plot(future_dates, future_forecast, label='Future Forecast', color='red')

max_value = weekly_data['new_cases_smoothed_per_million'].max()
max_date = weekly_data['new_cases_smoothed_per_million'].idxmax()
plt.annotate(f'Highest Value: {max_value:.1f}\nDate: {max_date.strftime("%Y-%m-%d")}',
             xy=(max_date, max_value),
             xytext=(max_date + pd.Timedelta(weeks=10), max_value),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=7, headlength=10),
             ha='left', va='center')

plt.ylabel('Cases per million citizens', fontsize=14)
plt.title('COVID-19 Cases Forecast in Sweden\nusing HWES model', fontsize=20)
plt.legend()

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.savefig("../plots/7_cases_prediction_hwes.png")
