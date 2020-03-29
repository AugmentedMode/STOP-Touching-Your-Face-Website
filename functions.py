import os
import hashlib
import sqlite3



def get_database_connection():
    '''
        Creates a connection between selected database
    '''
    sqlite_file = 'site.db'
    file_exists = os.path.isfile(sqlite_file)
    conn = sqlite3.connect(sqlite_file)
    if not file_exists:
        create_sqlite_tables(conn)
    if os.stat(sqlite_file).st_size == 0:
        create_sqlite_tables(conn)
    return conn


def create_sqlite_tables(conn):
    '''
        Creates a sqlite tables as specified in schema_sqlite.sql file
    '''
    cursor = conn.cursor()
    with open('schema_sqlite.sql', 'r') as schema_file:
        cursor.executescript(schema_file.read())
    conn.commit()


def add_email(email):
    '''
        Function for storing email
    '''
    conn = get_database_connection()
    try:
        cursor = conn.cursor()
        print('hello before insert')
        print(email)
        cursor.execute("INSERT INTO subscriber_emails(emails) VALUES (?)", (email))
        print('hello after insert')
        conn.commit()
        cursor.close()
        return
    except:
        cursor.close()
