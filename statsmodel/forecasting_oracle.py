import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine(f'oracle+oracledb://@',
                       connect_args={"user": "logista",
                                     "password": "Director3",
                                     "dsn": "DES0395NB.d400.MH.GRP:1521/XEPDB1"
                                     }
                       )
sql = """
select time_date, sum(alarm_count) alarm_count from APP_ALM_STAT_AGG where TIME_LEVEL = 'hour' group by time_date
"""
ts = pd.read_sql(sql, engine, index_col='time_date')
ts = ts.asfreq(freq='H')
#macrodata.index = pd.period_range('1959Q1', '2009Q3', freq='Q')

endog = ts['alarm_count']
#endog.plot(figsize=(15, 5))
#plt.show()

mod = sm.tsa.SARIMAX(endog, order=(1,0,0), trend='c')
res = mod.fit()
print(res.summary())
print(res.forecast())

fig, ax = plt.subplots(figsize=(15,5))
endog.loc[:].plot(ax=ax)

fcast = res.get_forecast(steps=3).summary_frame()
fcast['mean'].plot(ax=ax, style='k--')
ax.fill_between(fcast.index, fcast['mean_ci_lower'], fcast['mean_ci_upper'], color='k', alpha=0.1)

plt.show()