import psycopg2 as pg
from psycopg2 import extensions, sql


def createDatabase():
    #Connect to PostgreSQL server
    conn = pg.connect(user="postgres", password="asdf3232")
    conn.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    # conn.autocommit = True
    # Create a cursor object
    cur = conn.cursor()
    # Process to fetch all existing databases
    queryFetchAllDB = '''SELECT datname FROM pg_database;'''
    cur.execute(queryFetchAllDB)
    db_list = cur.fetchall()
    # print(db_list)
    # Check if the 'peripheraldb' database already exists
    if ('peripheraldb',) not in db_list:
        # Create a SQL object and execute the create database query
        queryCreateDB = '''CREATE DATABASE peripheraldb;'''
        createDB = sql.SQL(queryCreateDB)
        cur.execute(createDB)
    else:
        print("Database already exists")


def createTable():
    # Connect to the 'peripheraldb' database
    with pg.connect(database="peripheraldb", user="postgres", password="asdf3232") as conn:
        # Create a cursor object
        with conn.cursor() as cur:
            # Process to check if table 'monitor' exists in schema 'public'
            queryTableExists = '''SELECT EXISTS (
                                    SELECT FROM 
                                        pg_tables
                                    WHERE 
                                        schemaname = 'public' AND 
                                        tablename  = 'monitor'
                                    );
                                    '''
            cur.execute(queryTableExists)
            if not cur.fetchone()[0]:
                # Query to create a new table 'monitor' in schema 'public'
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
