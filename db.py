# Criação do banco (roda uma vez no terminal python)
import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')
conn.executemany('INSERT INTO users (name) VALUES (?)', [('Alice',), ('Bob',), ('Carol',), ('Dave',)])
conn.commit()
conn.close()
