# import oracledb
# import pandas as pd
# from sqlalchemy import create_engine
#
# engine = create_engine(f'oracle+oracledb://@',
#                        connect_args={"user": "logista",
#                                      "password": "Director3",
#                                      "dsn": "DES0395NB.d400.MH.GRP:1521/XEPDB1"
#                                      }
#                        )
# sql = """
# select * from APP_ALM_STAT_AGG where TIME_LEVEL = 'hour'
# """
# df = pd.read_sql(sql, engine, index_col='time_date')

from sqlalchemy.engine import create_engine
import pandas as pd

DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'
USERNAME = 'logista' #enter your username
PASSWORD = 'Director3' #enter your password
HOST = 'DES0395NB.d400.MH.GRP' #enter the oracle db host url
PORT = 1521 # enter the oracle port number
SERVICE = 'XEPDB1' # enter the oracle db service name
ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST  + '/?service_name=' + SERVICE

print(ENGINE_PATH_WIN_AUTH)

engine = create_engine(ENGINE_PATH_WIN_AUTH)


#test query
test_df = pd.read_sql_query('SELECT 1 FROM dual', engine)

print('OK')