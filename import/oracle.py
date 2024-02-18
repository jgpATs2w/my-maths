from sqlalchemy import create_engine

engine = create_engine("oracle+cx_oracle://logista:Director3@DES0395NB.d400.MH.GRP:1521/?service_name=XEPDB1")

with engine.connect() as conn:
    print(conn.scalar("select 1 FROM dual"))

print('OK')
