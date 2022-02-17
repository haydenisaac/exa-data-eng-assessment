from sqlalchemy import create_engine
mysql_conn_str = "mysql+pymysql://root:root@mysql_db:3306/patients"
engine = create_engine(mysql_conn_str)
connection = engine.connect()
q = connection.execute('SHOW DATABASES')
print(q.fetchall())
