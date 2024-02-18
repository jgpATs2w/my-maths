#https://pandas.pydata.org/docs/user_guide/visualization.html#plotting-tools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.rand(1000,4), columns=["a", "b","c","d"])
pd.plotting.scatter_matrix(df, alpha=0.2, figsize=(6,6), diagonal="kde")

plt.show()