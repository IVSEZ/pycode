import os
import pandas as pd
import numpy as np
from fbprophet import Prophet

# import matplotlib.pyplot as plt


# Python
df = pd.read_csv('C:/ProgramData/MySQL/MySQL Server 5.7/Export/export-res-all-25102017-1.csv')
df['ds'] = pd.to_datetime(df['ds'])
print(df.head())

df.set_index('ds').plot(figsize=(12, 9))

df['y'] = np.log(df['y'])
df.set_index('ds').plot(figsize=(12, 9))

m = Prophet(daily_seasonality=True)
m.fit(df)

future_data = m.make_future_dataframe(periods=365)
# print(future_data.tail())

forecast = m.predict(future_data)


# print(forecast.columns)

# print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail() )

# m.plot(forecast)
# m.plot_components(forecast)
#
# playoffs = pd.DataFrame({
#   'holiday': 'playoff',
#   'ds': pd.to_datetime(['2008-01-13', '2009-01-03', '2010-01-16',
#                         '2010-01-24', '2010-02-07', '2011-01-08',
#                         '2013-01-12', '2014-01-12', '2014-01-19',
#                         '2014-02-02', '2015-01-11', '2016-01-17',
#                         '2016-01-24', '2016-02-07']),
#   'lower_window': 0,
#   'upper_window': 1,
# })
#
# superbowls = pd.DataFrame({
#   'holiday': 'superbowl',
#   'ds': pd.to_datetime(['2010-02-07', '2014-02-02', '2016-02-07']),
#   'lower_window': 0,
#   'upper_window': 1,
# })
#
# holidays = pd.concat((playoffs, superbowls))
#
# m = Prophet(holidays=holidays)


# forecast = m.fit(df).predict(future_data)
# m.plot_components(forecast)
#

# print(forecast.tail())


# forecast['y']=np.exp(forecast['yhat'])
print(forecast.tail())

forecast.to_csv('C:/ProgramData/MySQL/MySQL Server 5.7/Export/predictoutputlogs.csv')
forecast_data_orig = forecast # make sure we save the original forecast data
forecast_data_orig['yhat'] = np.exp(forecast_data_orig['yhat'])
forecast_data_orig['yhat_lower'] = np.exp(forecast_data_orig['yhat_lower'])
forecast_data_orig['yhat_upper'] = np.exp(forecast_data_orig['yhat_upper'])

# from sklearn.metrics import mean_absolute_error
# data = m.predict(df)
# print(mean_absolute_error(np.exp(data['y']), np.exp(data['yhat'])))


# rows = zip(timestamp,tempFuture)


header = ["ds", "yhat", "yhat_lower", "yhat_upper"]
forecast_data_orig.to_csv('C:/ProgramData/MySQL/MySQL Server 5.7/Export/predictoutput.csv',columns=header)
