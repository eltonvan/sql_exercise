import sqlite3
from faker import Faker

faker = Faker()
user_num = input("How many users do you want to create? ")
data = ""
data_lst = []
for i in range(int(user_num)):
    username = faker.user_name()
    email = faker.email()
    birthdate = faker.date()
    country = faker.country()
    data = (username, email, birthdate, country)
    data_lst.append(data)
data_lst[:-1] = data_lst[:-1][:-2]
con = sqlite3.connect("users.db")
cur = con.cursor()
cur.execute(
    """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    birthdate DATE NOT NULL,
    country TEXT NOT NULL
    );"""
)

cur.executemany(
    "insert into users (username, email, birthdate, country) VALUES (?,?,?,?)", data_lst
)

con.commit()


con.close()

new_con = sqlite3.connect("users.db")
new_cur = new_con.cursor()
res = new_cur.execute("select * from users")
print(res.fetchall())
