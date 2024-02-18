#https://pandas.pydata.org/docs/user_guide/10min.html
import numpy as np
import pandas as pd

global s
s = pd.Series([1,3,5,np.nan,6,8])

#print(s)

dates = pd.date_range("20230101", periods=6)

#print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)
print(df.to_numpy())
print(df.dtypes)
print(df.describe())
print(df.T)
print(df.sort_index(ascending=False))
print(df.sort_values(by="B"))
print(df["A"])
print(df[0:2])
print(df.loc[dates[0]])


df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

#print(df2)
#print(df2["A"])