#https://pandas.pydata.org/docs/user_guide/10min.html
import numpy as np
import pandas as pd

rng = pd.date_range("1/1/2012", periods=100, freq="S")
ts = pd.Series(np.random.randint(0,500,len(rng)), index=rng)

print(ts.resample("5min").sum())