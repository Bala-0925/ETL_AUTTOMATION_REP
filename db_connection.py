import pandas as pd
from sqlalchemy import create_engine
mysql_engine = create_engine('mysql+pymysql://root:Newuser%40123@localhost:3306/balaqadb')
connection = mysql_engine.connect()
df_query = pd.read_sql("select * from employees",mysql_engine)
print(df_query)