import sqlite3

a = sqlite3.connect("mydatebase.db")

malumot = a.cursor()

malumot.execute('''
CREATE TABLE IF NOT EXISTS gullar(
    nomi TEXT
    rangi TEXT




)''')

