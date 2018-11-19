import pandas as pd
import numpy as np
from fbprophet import Prophet

import matplotlib.pyplot as plt


plt.rcParams['figure.figsize']=(20,10)
plt.style.use('ggplot')
plt.interactive(False)

# Python
df = pd.read_csv('C:/ProgramData/MySQL/MySQL Server 5.7/Export/export-res-all-25102017-1.csv')

# print(df.dtypes)
df.set_index('ds').plot(figsize=(12, 9))

print(df.head())

# df['ds'] = pd.DatetimeIndex(df['ds'])
df['y'] = np.log(df['y'])


# print(df.dtypes)

print(df.head())

# m = Prophet()
# m.fit(df)

# future = m.make_future_dataframe(periods=365)
# print(future.tail())

# forecast = m.predict(future)
# print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])

# print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

# m.plot(forecast).show()
# plt.plot(forecast)
# plt.show()
# plt.savefig('test.png')

