import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def convert_time(s):
    h, m, s = map(int, s.split(':'))
    return pd.Timedelta(hours=h, minutes=m, seconds=s)

data = pd.read_csv('marathon-data.csv', converters={'split':convert_time, 'final': convert_time})
data['split_sec'] = data['split'].astype('int64') / 1E9
data['final_sec'] = data['final'].astype('int64') / 1E9

print(data.head())
print(data.dtypes)

with sns.axes_style('white'):
    g = sns.jointplot(data, x='split_sec', y='final_sec', kind='hex')
    g.ax_joint.plot(np.linspace(4000, 16000),
                    np.linspace(8000, 35000), 'k:')

data['split_frac'] = 1 - 2 * data['split_sec'] / data['final_sec']
sns.displot(data['split_frac'], kde=False)
plt.axvline(0, color="k", linestyle="--")

g2 = sns.PairGrid(data, vars=['age', 'split_sec'], hue='gender', palette='RdBu_r')
g2.map(plt.scatter, alpha=0.8)
g2.add_legend()
plt.show()