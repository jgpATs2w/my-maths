import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style(style="darkgrid")

engine = create_engine(f'oracle+oracledb://@',
                       connect_args={"user": "logista",
                                     "password": "Director3",
                                     "dsn": "DES0395NB.d400.MH.GRP:1521/XEPDB1"
                                     }
                       )
sql = """
select * from APP_ALM_STAT_AGG where TIME_LEVEL = 'hour'
"""
df = pd.read_sql(sql, engine, index_col='time_date')

sns.relplot(data=df, x="time_date", y="alarm_count", hue="alarm_type", kind="line")

plt.show()