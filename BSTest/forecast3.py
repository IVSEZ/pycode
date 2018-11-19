import os
import pandas as pd
import numpy as np
from fbprophet import Prophet
import pymysql
import configparser
import pandas as pd

import matplotlib.pyplot as plt


plt.rcParams['figure.figsize']=(20,10)
plt.style.use('ggplot')
plt.interactive(False)

# connect to mysql
config = configparser.ConfigParser()
config.read('dbconfig.ini')

cnx = pymysql.connect(host=config['rcbill_my']['host'], user=config['rcbill_my']['user'],
                      password=config['rcbill_my']['pass'], db=config['rcbill_my']['db'], charset="utf8",
                      use_unicode=True)

# reg = 'Mahe'
# reg = 'Praslin'

cc='Residential'
# cc='Corporate'
# cc='Corporate Bundle'
# cc='Corporate Bulk'
# cc='Corporate Lite'
# cc='Corporate Small'
# cc='Employee'
# cc='Intelvision Office'
# cc='VIP'
# cc='Corporate Large'
# cc='Prepaid'
# cc='Standing Order'
# cc='USD_standard'



sc = 'Internet'
# cpc = 0.00008
cpc = 0.005

# sc='TV'
# cpc = 0.00006

# sc='Voice'
# cpc = 0.00005


# 'and ' \
# ' and period<"2017-08-31" ' \

q1 = ' select period as ds, sum(activenos) as y ' \
     ' from rcbill_my.customersactivity_all ' \
     ' where ' \
     ' clientclass in ("' + cc + '") ' \
     ' and servicecategory in ("' + sc + '") ' \
     ' group by period'


df = pd.read_sql(q1, con=cnx)

# print(df.dtypes)

df['ds'] = pd.to_datetime(df['ds'])
# print(df.dtypes)
df['y_orig']=df['y']




df['y'] = np.log(df['y'])

weekends = pd.DataFrame({
  'holiday': 'weekends',
  'ds': pd.to_datetime(['']),
  'lower_window': 0,
  'upper_window': 1,
})

specialdays = pd.DataFrame({
  'holiday': 'specialdays',
  'ds': pd.to_datetime(['2016-01-01', '2016-03-25', '2016-03-26','2016-03-27','2016-05-01','2016-05-02','2016-06-05','2016-06-18','2016-06-29','2016-08-15','2016-11-01','2016-12-08','2016-12-25','2016-12-31'
                           ,'2017-01-01', '2017-02-28','2017-04-14', '2017-04-15','2017-04-17','2017-04-30','2017-05-01','2017-06-15','2017-06-19','2017-06-29','2017-08-15','2017-11-01','2017-12-08','2017-12-25','2017-12-31'
                           ,'2018-01-01', '2018-02-28', '2018-03-30', '2018-03-31','2018-04-02','2018-05-01','2018-05-31','2018-06-18','2018-06-29','2018-08-15','2018-11-01','2018-12-08','2018-12-25','2018-12-31']),
  'lower_window': 0,
  'upper_window': 1,
})

holidays = pd.concat((weekends, specialdays))
# interval_width=0.99,
#
m = Prophet(yearly_seasonality=True, holidays=holidays, changepoint_prior_scale=cpc)

# RESIDENTIAL INTERNET
# m = Prophet(yearly_seasonality=True,holidays=holidays, changepoint_prior_scale=0.00008)

# RESIDENTIAL TV
# m = Prophet(yearly_seasonality=True,holidays=holidays, changepoint_prior_scale=cpc)

# RESIDENTIAL VOICE
# m = Prophet(yearly_seasonality=True,holidays=holidays, changepoint_prior_scale=0.00004)

# df['cap']=2
# m = Prophet(holidays=holidays)
m.fit(df)

future_data = m.make_future_dataframe(periods=421)
# future_data['cap'] = 0.00001

forecast = m.predict(future_data)

# merge real points with forcast
real_and_forecast = pd.merge(left=forecast, right=df, on="ds")

# get the difference between prediction and forcast
real_and_forecast["residual"] = real_and_forecast.y - real_and_forecast.yhat

# get the range between 80% confidence intervals
real_and_forecast["uncertainty"] = real_and_forecast.yhat_upper - real_and_forecast.yhat_lower

# define an outlier as more than two intervals away from the forecast
v = 2
(
    real_and_forecast
    [real_and_forecast.residual.abs() > v * real_and_forecast.uncertainty]
    [["ds", "residual"]]
)

# print(forecast.head())

# forecast.to_csv('C:/ProgramData/MySQL/MySQL Server 5.7/Export/predictoutputlogs.csv')
forecast_data_orig = forecast # make sure we save the original forecast data
forecast_data_orig['yhat'] = np.exp(forecast_data_orig['yhat'])
forecast_data_orig['yhat_lower'] = np.exp(forecast_data_orig['yhat_lower'])
forecast_data_orig['yhat_upper'] = np.exp(forecast_data_orig['yhat_upper'])

header = ["ds", "yhat", "yhat_lower", "yhat_upper"]
# forecast_data_orig.to_csv('C:/ProgramData/MySQL/MySQL Server 5.7/Export/pred_' + cc + '_' + sc + '.csv',columns=header)
# forecast_data_orig.to_csv('C:/ProgramData/MySQL/MySQL Server 5.7/Export/pred_' + cc + '_' + sc + '.csv')
plt.plot(df['ds'],df['y_orig'])
# plt.show()
plt.plot(forecast_data_orig['ds'],forecast_data_orig['yhat'])
plt.show()
