import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

plt.close("all")
CICLOS = 20
N = 1000
space = np.linspace(-CICLOS/2*np.pi, CICLOS/2*np.pi, num=N)
t = pd.date_range("2023-01-01", freq="min", periods=N)

ts = pd.Series(np.sin(space), index=t)

sns.relplot(data=ts, kind="line", alpha=0.5)

plt.show()

