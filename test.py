import sqlite3

connection = sqlite3.connect('test.db')

cursor = connection.cursor()

sql = '''CREATE TABLE IF NOT EXISTS Attendance(
                                    PID INTEGER PRIMARY KEY AUTOINCREMENT,
                                    USERNAME text NOT NULL,
                                    PASSWORD text NOT NULL)'''

cursor.execute(sql)
""""""
sql = "INSERT INTO Attendance (USERNAME, PASSWORD) VALUES ('rahat','1234') "
sql = "INSERT INTO Attendance (USERNAME, PASSWORD) VALUES ('tuman','78910') "

cursor.execute(sql)
connection.commit()

sql = 'SELECT * FROM Attendance'
cursor.execute(sql)

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()




