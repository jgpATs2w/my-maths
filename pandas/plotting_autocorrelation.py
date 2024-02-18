#https://pandas.pydata.org/docs/user_guide/visualization.html#autocorrelation-plot
from pandas.plotting import autocorrelation_plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#plt.figure()
plt.close("all")
spacing = np.linspace(-9*np.pi, 9*np.pi, num=1000)
data = pd.Series(0.7*np.random.rand(1000)+0.3*np.sin(spacing))

#autocorrelation_plot(data)
df = pd.DataFrame(data, index=range(1000))
df.plot()
plt.show()

