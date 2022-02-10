import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

'''
Creating & Fetching Databases Queries
'''

# cursor.execute(
#                 '''
#                 CREATE TABLE IF NOT EXISTS Movies
#                 (Title TEXT, DIRECTOR TEXT, YEAR INT)
#                 '''
#             )
#
# # cursor.execute("INSERT INTO Movies VALUES ('Taxi Driver', 'Martin Scorsese', 1996)")
#
# famousFilms = [('Pulp Fiction', 'Quentin Qurantino', 1994),
#                 ('Back to the Future', 'Steven Spielberg', 1985),
#                 ('Moonrise Kingdom', 'Wes Anderson', 2012)]
#
# cursor.executemany('Insert INTO Movies VALUES (?,?,?)', famousFilms)
#
# records = cursor.execute("SELECT * FROM Movies")
#
# print(cursor.fetchall())
#
# print(record for record in records)

# print(cursor.fetchone())

'''
Filtering Databases Queries
'''
release_year = (1985, )

cursor.execute("SELECT * FROM Movies WHERE year=?", release_year)

print(cursor.fetchall())



connection.commit()
connection.close()
