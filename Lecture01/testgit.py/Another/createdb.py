import sqlite3

conn = sqlite3.connect('registration2.sqlite3')

conn.execute('CREAT TABLE IF NOT EXISTS Students (Id INI, Name TEXT)')

conn.execute("INSERT INTO Students (Id, Name) VELUES (1, 'Sam')")
conn.execute("INSERT INTO Students (Id, Name) VELUES (2, 'Mary')")
conn.execute("INSERT INTO Students (Id, Name) VELUES (3, 'Tina')")


conn.commit()


cursor = conn.execute('SELECT * FROM Students')
for row in cursor:
    print(f"Id = {row[0]}, Name = {row[1]}")

conn.close()

