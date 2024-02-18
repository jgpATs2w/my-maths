import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

macrodata = sm.datasets.macrodata.load_pandas().data
macrodata.index = pd.period_range('1959Q1', '2009Q3', freq='Q')

endog = macrodata['infl']
endog.plot(figsize=(15, 5))

#plt.show()

mod = sm.tsa.SARIMAX(endog, order=(1,0,0), trend='c')
res = mod.fit()
#print(res.summary())
print(res.forecast())

fig, ax = plt.subplots(figsize=(15,5))
endog.loc['1999':].plot(ax=ax)

fcast = res.get_forecast('2011Q3').summary_frame()
fcast['mean'].plot(ax=ax, style='k--')
ax.fill_between(fcast.index, fcast['mean_ci_lower'], fcast['mean_ci_upper'], color='k', alpha=0.1)

plt.show()