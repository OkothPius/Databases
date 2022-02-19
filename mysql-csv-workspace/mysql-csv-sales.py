import csv
import mysql.connector as mysql

# DB connection
connection = mysql.connect(user='oruko',
                            host='localhost',
                            password='<P1r$Hg02ram/>',
                            database= 'sales',
                            allow_local_infile=True
                            )

cursor = connection.cursor()


# Creating our table
create_query = '''CREATE TABLE salesperson(
    id INT(255) NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email_address VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    state VARCHAR(255) NOT NULL,
    PRIMARY KEY (id))'''

# Check if the table exists
cursor.execute("DROP TABLE IF EXISTS salesperson")

cursor.execute(create_query)

# Read from the CSV file
# with open('./salespeople.csv', 'r') as f:
#     csv_data = csv.reader(f)
#     for row in csv_data:
#         print(row)
#         row_tuple = tuple(row)
#         cursor.execute('INSERT INTO salesperson(first_name, last_name, email_address \
#                         ,city, state) VALUES("%s", "%s", "%s", "%s", "%s")', row_tuple)

# Load csv data directly (Necessary for Bulk data)
q = '''LOAD DATA LOCAL INFILE
    '/home/kmaster/Documents/Databases/mysql-csv-workspace/salespeople.csv'
    INTO TABLE salesperson FIELDS TERMINATED BY ',' ENCLOSED BY '"'
    (first_name, last_name, email_address, city, state);'''

cursor.execute(q)

connection.commit()

# Limit queried objects to 10
cursor.execute("SELECT * FROM salesperson LIMIT 10")
print(cursor.fetchall())

cursor.close()
