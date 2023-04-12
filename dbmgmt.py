import psycopg2 as pg
from psycopg2 import extensions, sql

conn = pg.connect(user = "postgres", password = "asdf3232")
conn.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)
conn.autocommit = True
cur = conn.cursor()
cur.execute("SELECT datname FROM pg_database;")
db_list = cur.fetchall()
if 'PeripheralDB' not in db_list:
    createDB = sql.SQL("CREATE DATABASE PeripheralDB;")
    cur.execute(createDB)
else:
    print("Database already exists")
