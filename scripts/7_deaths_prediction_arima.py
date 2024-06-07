import pandas as pd
from matplotlib import pyplot as plt
from pmdarima import auto_arima
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.dates as mdates

from utils import read_data_country


df_world, df_sweden = read_data_country()

deaths_cases_per_million = df_sweden[['new_deaths_smoothed_per_million', 'new_cases_smoothed_per_million']].dropna()
weekly_data = deaths_cases_per_million.resample('W').mean()

train_size = int(len(weekly_data) * 0.75)
train_data, test_data = weekly_data[:train_size], weekly_data[train_size:]

auto_model = auto_arima(
    train_data['new_deaths_smoothed_per_million'],
    seasonal=True,
    m=52,
    stepwise=True,
    trace=True
)

order = auto_model.order
seasonal_order = auto_model.seasonal_order
model = ARIMA(
    train_data['new_deaths_smoothed_per_million'],
    order=order,
    seasonal_order=seasonal_order
)
fitted_model = model.fit()

order = auto_model.order
seasonal_order = auto_model.seasonal_order
forecast_test = fitted_model.predict(start=test_data.index[0], end=test_data.index[-1])
model_full = ARIMA(
    weekly_data['new_deaths_smoothed_per_million'],
    order=order,
    seasonal_order=seasonal_order
)
fitted_model_full = model_full.fit()

future_steps = 52
forecast_future = fitted_model_full.forecast(steps=future_steps)

last_date = weekly_data.index[-1]
future_dates = pd.date_range(start=last_date, periods=future_steps + 1, freq='W')[1:]

future_forecast_series = pd.Series(forecast_future.values, index=future_dates)

plt.figure(figsize=(10, 6))
plt.plot(weekly_data['new_deaths_smoothed_per_million'], label='Historical Data', color='#882255')
plt.plot(forecast_test, label='Test Forecast', color='orange')
plt.plot(future_forecast_series, label='Future Forecast', color='red')
plt.axvline(x=train_data.index[-1], color='black', linestyle='--', label='Train/Test Split')

max_value = weekly_data['new_deaths_smoothed_per_million'].max()
max_date = weekly_data['new_deaths_smoothed_per_million'].idxmax()
plt.annotate(f'Highest Value: {max_value:.1f}\nDate: {max_date.strftime("%Y-%m-%d")}',
             xy=(max_date, max_value),
             xytext=(max_date + pd.Timedelta(weeks=10), max_value),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=7, headlength=10),
             ha='left', va='center')

plt.title('COVID-19 Deaths Forecast in Sweden\nusing ARIMA model', fontsize=20)
plt.ylabel('Deaths per million citizens', fontsize=14)
plt.legend()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

plt.savefig("../plots/7_deaths_prediction_arima.png")
