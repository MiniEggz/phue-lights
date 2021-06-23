import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
        print('error')
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
    

colours_table_sql = ''' CREATE TABLE IF NOT EXISTS colours (
                            colour_name text PRIMARY KEY,
                            red integer,
                            green integer,
                            blue integer
                        );'''

if __name__ == '__main__':
    conn = create_connection('db\\colours.db')
    if conn is not None:
        create_table(conn, colours_table_sql)
    else:
        print("ERROR: cannot connect to database")
    conn.close()