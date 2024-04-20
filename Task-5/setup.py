import sqlite3

with sqlite3.connect('data/contacts.db') as conn:
    conn.cursor().execute('Create table contacts (id String NOT NULL,Name String NOT NULL, PhoneNumber int(10) NOT NULL, Email String, Address String)')
    print(*conn.cursor().execute('PRAGMA table_info(contacts)').fetchall(),sep='\n')