import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

create_table ="CREATE TABLE IF NOT EXISTS users(id integer primary key autoincrement, username text, password text)"

cursor.execute(create_table)

sql = "insert into users(username,password) values('test','asdf');"

cursor.execute(sql)

connection.commit()

rows = cursor.execute("select * from users")

for row in rows:
    print(row)


item_table ="CREATE TABLE items(id integer primary key autoincrement, name text, price real)"

cursor.execute(item_table)


connection.commit()


connection.close()

