import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.close("all")

ts = pd.Series(np.random.rand(1000), index=pd.date_range("1/1/2000", periods=1000))

ts = ts.cumsum()

ts.plot()
plt.show()