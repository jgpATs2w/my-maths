import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn
import seaborn as sns

seaborn.set()
data = pd.read_csv('rollingsums_groupby.csv', index_col='Date', parse_dates=True)
print(data.head())
data.columns = ['Date', 'West', 'East']
data['Total'] = data.eval('West + East')
print(data.dropna().describe())

#data.plot()
weekly = data.resample('W').sum()
#weekly.plot(style=[':', '--', '-'])

daily = data.resample('D').sum()
#daily.rolling(50, center=True, win_type='gaussian').sum(std=10).plot(style=[':', '--', '-'])

#by_time = data.groupby(data.index.time).mean()
hourly_ticks = 4 * 60 * 60 * np.arange(6)
#by_time.plot(xticks=hourly_ticks, style=[':', '--', '-'])

#plt.ylabel('Bicicle Count')

weekend = np.where(data.index.weekday < 5, 'Weekday', 'Weekend')
by_time_split = data.groupby([weekend, data.index.time]).mean()

fig,ax = plt.subplots(1,2,figsize=(14,5))
by_time_split.loc['Weekday'].plot(ax=ax[0], title='Weekdays', xticks=hourly_ticks, style=[':', '--', '-'])
by_time_split.loc['Weekend'].plot(ax=ax[1], title='Weekend', xticks=hourly_ticks, style=[':', '--', '-'])

plt.show()