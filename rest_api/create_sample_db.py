import sqlite3
from sqlite3 import Error


CREATE_TABLE = """ CREATE TABLE IF NOT EXISTS people (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        age integer,
                                        occupation text
                                    ); """
POPULATE_TABLE = ''' INSERT INTO people(id,name,age,occupation)
              VALUES(0,\'mario\',19,\'plumber\') '''

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.cursor().execute(CREATE_TABLE)
        conn.cursor().execute(POPULATE_TABLE)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"people.db")