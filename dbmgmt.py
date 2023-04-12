import psycopg2 as pg
from psycopg2 import extensions, sql


def createDatabase():
    conn = pg.connect(user="postgres", password="asdf3232")
    conn.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    conn.autocommit = True
    cur = conn.cursor()
    queryFetchAllDB = '''SELECT datname FROM pg_database;'''
    cur.execute()
    db_list = cur.fetchall()
    print(db_list)
    if ('peripheraldb',) not in db_list:
        queryCreateDB = '''CREATE DATABASE peripheraldb;'''
        createDB = sql.SQL()
        cur.execute(createDB)
    else:
        print("Database already exists")


def createTable():
    with pg.connect(database="peripheraldb", user="postgres", password="asdf3232") as conn:
        with conn.cursor() as cur:
            queryTableExists = '''SELECT EXISTS (
                                    SELECT FROM 
                                        pg_tables
                                    WHERE 
                                        schemaname = 'public' AND 
                                        tablename  = 'monitor'
                                    );
                                    '''
            cur.execute(queryTableExists)
            if (True,) in cur.fetchone():
                queryCreateMonitorTable = '''CREATE TABLE monitor(
                id SERIAL,
                name VARCHAR(512),
                price MONEY,
                link VARCHAR(512),
                PRIMARY KEY (id)
                )
                '''
                cur.execute(queryCreateMonitorTable)
            else:
                print("Table already exists")

createDatabase()
createTable()

