import sqlite3

connection = sqlite3.connect('users.db')

cursor = connection.cursor()

'''
Creating & Fetching Databases Queries
'''
cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS Users
            (user_id INT,
            first_name TEXT,
            last_name TEXT,
            email TEXT)
            '''
            )

usersDetails = [(1, 'John', 'Doe', 'jdoe@test.com'),
                (2, 'jane', 'Doe', 'janedoe@test.com'),
                (3, 'randy', 'smith', 'randy@test.com'),
                (4, 'grace', 'smith', 'graces@test.com'),
                (5, 'maggie', 'harriet', 'maggie@test.com')]

cursor.executemany("INSERT INTO Users VALUES (?,?,?,?)", usersDetails)

email = cursor.execute('SELECT email FROM Users')
print(cursor.fetchall())

connection.commit()
connection.close()
