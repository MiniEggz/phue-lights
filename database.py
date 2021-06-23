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
    

colours_table_sql = '''
CREATE TABLE IF NOT EXISTS colours (
    colour_name text PRIMARY KEY,
    red integer,
    green integer,
    blue integer
);'''

def create_colour(conn, colour):
    sql = 'INSERT INTO colours(colour_name, red, green, blue) VALUES(?,?,?,?)'
    cur = conn.cursor()
    cur.execute(sql, colour)
    conn.commit()



if __name__ == '__main__':
    db = 'db\\colours.db'
    conn = create_connection(db)

    with conn:
        colour = ('white', 255, 255, 255)
        create_colour(conn, colour)