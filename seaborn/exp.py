import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

plt.close("all")
CICLOS = 20
N = 1000
LIMIT = np.random.rand()*10
space = np.linspace(-LIMIT, LIMIT, num=N)
t = pd.date_range("2023-01-01", freq="ms", periods=N)

ts = pd.Series(np.exp(space), index=t)

sns.relplot(data=ts, kind="line", alpha=0.5)

plt.show()

