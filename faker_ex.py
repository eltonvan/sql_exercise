from faker import Faker


faker = Faker()

data = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    birthdate DATE NOT NULL,
    country TEXT NOT NULL
    );

INSERT INTO users (username, email, birthdate, country) VALUES
    
''' 

for i in range(5):
        username = faker.user_name()
        email = faker.email()
        birthdate = faker.date()
        country = faker.country()
        data += f"('{username}', '{email}', '{birthdate}', '{country}')."


sql_file = open("data.sql", "w")

sql_file.write(data[:-2])
sql_file.close()