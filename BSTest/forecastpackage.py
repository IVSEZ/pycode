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

dt = '04122017'

# reg = 'All'
reg = 'Mahe'
# reg = 'Praslin'


cc = 'Residential'
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

# cpc = 0.05
# sc = 'Internet'
# cpc = 0.00008

sc='TV'
cpc = 0.00006
cpc = 0.00005

# sc='Voice'
# cpc = 0.00005

# TV PACKAGES
# pk = 'Basic'
# cpc = 0.0005
# pk = 'Corporate'
# pk = 'Executive'
pk = 'Extravagance'
cpc = 0.0005
# pk = 'Extravagance Corporate'
# pk = 'French'
# cpc = 0.00009
# for praslin french
# cpc = 0.0005
# pk = 'Indian'
# cpc = 0.00005
# pk = 'Indian Corporate'
# pk = 'Intelenovela'
# cpc = 0.0005
# pk = 'Prestige'
# cpc = 0.0005
# pk = 'TurquoiseTV'

# INTERNET PACKAGES
# pk = '10GB'
# pk = '20GB'
# pk = '40GB'
# pk = 'Business Unlimited-1'
# pk = 'Business Unlimited-2'
# pk = 'Business Unlimited-8'
# pk = 'Business Unlimited-8-daytime'
# pk = 'Crimson'
# cpc = 0.0000099

# pk = 'Crimson Corporate'
# pk = 'Elite'
# cpc = 0.005
# cpc = 0.0005
# pk = 'Extreme'
# cpc = 0.000009
# pk = 'Extreme Plus'
# cpc = 0.000009
# pk = 'Intel Data 10'
# cpc = 0.000009
# Praslin
# cpc = 0.000009
# pk = 'Performance'
# cpc = 0.000009
# pk = 'Performance Plus'
# cpc = 0.5
# pk = 'Prepaid Data 10'
# cpc = 1

# pk = 'Prepaid Single'
# cpc = 0.05
# pk = 'Starter'
# cpc = 0.00009
# pk = 'Value'
# cpc = 0.000095


# 'and ' \
# ' and period<"2017-08-31" ' \

# OTHERS
# q1 = ' select period as ds, sum(activenos) as y ' \
#      ' from rcbill_my.customersactivity_all ' \
#      ' where ' \
#      ' clientclass in ("' + cc + '") ' \
#      ' and servicecategory in ("' + sc + '") ' \
#      ' and package in ("' + pk + '") ' \
#      ' group by period'

# OTHERS WITH REGION
q1 = ' select period as ds, sum(activenos) as y ' \
     ' from rcbill_my.customersactivity_all ' \
     ' where ' \
     ' clientclass in ("' + cc + '") ' \
     ' and servicecategory in ("' + sc + '") ' \
     ' and package in ("' + pk + '") ' \
     ' and region in ("' + reg + '") ' \
     ' group by period'

# FRENCH
# q1 = ' select period as ds, sum(activenos) as y ' \
#      ' from rcbill_my.customersactivity_all ' \
#      ' where ' \
#      ' clientclass in ("' + cc + '") ' \
#      ' and servicecategory in ("' + sc + '") ' \
#      ' and (package in ("French") or service in ("Subscription French")) ' \
#      ' group by period'

# q1 = ' select period as ds, sum(activenos) as y ' \
#      ' from rcbill_my.customersactivity_all ' \
#      ' where ' \
#      ' clientclass in ("' + cc + '") ' \
#      ' and servicecategory in ("' + sc + '") ' \
#      ' and region in ("' + reg + '") ' \
#      ' and period > "2017-01-01" ' \
#      ' and (package in ("French") or service in ("Subscription French")) ' \
#      ' group by period'

# Intelenovela
# q1 = ' select period as ds, sum(activenos) as y ' \
#      ' from rcbill_my.customersactivity_all ' \
#      ' where ' \
#      ' clientclass in ("' + cc + '") ' \
#      ' and servicecategory in ("' + sc + '") ' \
#      ' and (package in ("Intelenovela") or service in ("Subscription Intelenovela")) ' \
#      ' group by period'

# q1 = ' select period as ds, sum(activenos) as y ' \
#      ' from rcbill_my.customersactivity_all ' \
#      ' where ' \
#      ' clientclass in ("' + cc + '") ' \
#      ' and servicecategory in ("' + sc + '") ' \
#      ' and region in ("' + reg + '") ' \
#      ' and (package in ("Intelenovela") or service in ("Subscription Intelenovela")) ' \
#      ' group by period'

# Crimson
# q1 = ' select period as ds, sum(activenos) as y ' \
#      ' from rcbill_my.customersactivity_all ' \
#      ' where ' \
#      ' clientclass in ("' + cc + '") ' \
#      ' and servicecategory in ("' + sc + '") ' \
#      ' and package in ("' + pk + '") ' \
#      ' and period > "2017-03-31" ' \
#      ' group by period'

# q1 = ' select period as ds, sum(activenos) as y ' \
#      ' from rcbill_my.customersactivity_all ' \
#      ' where ' \
#      ' clientclass in ("' + cc + '") ' \
#      ' and servicecategory in ("' + sc + '") ' \
#      ' and region in ("' + reg + '") ' \
#      ' and package in ("' + pk + '") ' \
#      ' and period > "2017-03-31" ' \
#      ' group by period'

df = pd.read_sql(q1, con=cnx)

# print(df.dtypes)

df['ds'] = pd.to_datetime(df['ds'])
# print(df.dtypes)
df['y_orig'] = df['y']

df.loc[df['y'] == 0] = 1
# df.loc[0] = None

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
# RESIDENTIAL INTERNET
# m = Prophet(yearly_seasonality=True, holidays=holidays, changepoint_prior_scale=cpc, growth='logistic')

# for crimson
# m = Prophet(weekly_seasonality=True, holidays=holidays, changepoint_prior_scale=cpc, growth='logistic')

# RESIDENTIAL TV
m = Prophet(yearly_seasonality=True,holidays=holidays, changepoint_prior_scale=cpc)

# Prestige
# m = Prophet(yearly_seasonality=True,holidays=holidays, changepoint_prior_scale=cpc)

# Intelenovela
# m = Prophet(yearly_seasonality=True,holidays=holidays, changepoint_prior_scale=cpc)

# RESIDENTIAL VOICE
# m = Prophet(yearly_seasonality=True,holidays=holidays, changepoint_prior_scale=cpc)

df['cap'] = 7
# m = Prophet(holidays=holidays)
m.fit(df)

future_data = m.make_future_dataframe(periods=400)
future_data['cap'] = 7

forecast = m.predict(future_data)

# merge real points with forcast
# real_and_forecast = pd.merge(left=forecast, right=df, on="ds")

# get the difference between prediction and forcast
# real_and_forecast["residual"] = real_and_forecast.y - real_and_forecast.yhat

# get the range between 80% confidence intervals
# real_and_forecast["uncertainty"] = real_and_forecast.yhat_upper - real_and_forecast.yhat_lower

# define an outlier as more than two intervals away from the forecast
# v = 2
# (
#     real_and_forecast
#     [real_and_forecast.residual.abs() > v * real_and_forecast.uncertainty]
#     [["ds", "residual"]]
# )

print(forecast.tail())

# forecast.to_csv('C:/ProgramData/MySQL/MySQL Server 5.7/Export/predictoutputlogs.csv')
forecast_data_orig = forecast # make sure we save the original forecast data
forecast_data_orig['logy'] = forecast_data_orig['yhat']
forecast_data_orig['yhat'] = np.exp(forecast_data_orig['yhat'])
forecast_data_orig['yhat_lower'] = np.exp(forecast_data_orig['yhat_lower'])
forecast_data_orig['yhat_upper'] = np.exp(forecast_data_orig['yhat_upper'])

header = ["ds", "yhat"]
# forecast_data_orig.to_csv('C:/ProgramData/MySQL/MySQL Server 5.7/Export/pred_' + reg + '_' + cc + '_' + sc + '_' + pk + '_' + dt + '.csv',columns=header)
# forecast_data_orig.to_csv('C:/ProgramData/MySQL/MySQL Server 5.7/Export/pred_' + cc + '_' + sc + '_' + pk + '_' + dt + '.csv',columns=header)
# forecast_data_orig.to_csv('C:/ProgramData/MySQL/MySQL Server 5.7/Export/pred_' + cc + '_' + sc + '_' + pk + '_' + dt +'.csv')

plt.plot(df['ds'],df['y_orig'])
# plt.show()
plt.plot(forecast_data_orig['ds'],forecast_data_orig['yhat'])
plt.show()
