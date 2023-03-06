import  psycopg2

## set connection credits
DB_USER = 'gis43'
DB_PASSWORD = 'iti'
DB_NAME = 'gis43'
HOST = 'localhost'  ## 127.0.0.1
PORT = 5432

def connectToDatbase():
    try:
        # connection  = psycopg2.connect(user=DB_USER, password=DB_PASSWORD,
        #                                host=HOST, port=PORT,database=DB_NAME)
        dsn=f'user={DB_USER} password={DB_PASSWORD} dbname={DB_NAME} host={HOST} port={PORT}'
        connection = psycopg2.connect(dsn)
        print(connection)
        return connection

    except Exception as e:
        print(e)
        return None

# connectToDatbase()