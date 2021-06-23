import os.path
import sqlite3
from sqlite3 import Error

class Colours:

    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db = os.path.join(base_dir, 'db/colours.db')

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db)
        except Error as e:
            print(e)
        return conn


    colours_table_sql = '''
    CREATE TABLE IF NOT EXISTS colours (
        colour_name text PRIMARY KEY,
        red integer,
        green integer,
        blue integer
    );'''

    def create_table(self, create_table_sql):
        conn = self.create_connection()
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)
        conn.close()

    def create_colour(self, colour):
        conn = self.create_connection()
        sql = 'INSERT INTO colours(colour_name, red, green, blue) VALUES(?,?,?,?)'
        cur = conn.cursor()
        cur.execute(sql, colour)
        conn.commit()
        conn.close()

    def delete_colour(self, colour_name):
        conn = self.create_connection()
        sql = 'DELETE FROM colours WHERE colour_name=?'
        cur = conn.cursor()
        cur.execute(sql, (colour_name,))
        conn.commit()
        conn.close()

    def delete_all_colours(self):
        conn = self.create_connection()
        sql = 'DELETE FROM colours'
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()
    
    def get_colour(self, colour_name):
        conn = self.create_connection()
        sql = 'SELECT * FROM colours WHERE colour_name=?'
        cur = conn.cursor()
        cur.execute(sql, (colour_name,))
        colour = cur.fetchone()
        conn.close()
        return colour

    def get_all_names(self):
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM colours')
        
        rows = cur.fetchall()

        colours = []
        for row in rows:
            colours.append(f'{row[0]} [{row[1]},{row[2]},{row[3]}]')
        
        return colours

    def print_all(self):
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM colours')

        rows = cur.fetchall()

        for row in rows:
            print(row)