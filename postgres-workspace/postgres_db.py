import psycopg2

# Connecting to database
conn = psycopg2.connect(database='red30',
                        user='redruko',
                        password='password',
                        host='localhost',
                        port=5432)

cursor = conn.cursor()

# Create database table

# cursor.execute('''CREATE TABLE SALES(ORDER_NUM INT PRIMARY KEY,
#      ORDER_TYPE TEXT,
#      CUST_NAME TEXT,
#      PROD_NUMBER TEXT,
#      PROD_NAME TEXT,
#      QUANTITY INT,
#      PRICE REAL,
#      DISCOUNT REAL,
#      ORDER_TOTAL REAL);''')

# Inserting data to the db
cursor.execute('''INSERT INTO SALES(ORDER_NUM, ORDER_TYPE,
                    CUST_NAME, PROD_NUMBER, PROD_NAME, QUANTITY,
                    PRICE, DISCOUNT, ORDER_TOTAL) VALUES(1105910, 'Retail',
                    'Syman Mapstone', 'EB521',
                    'Understanding Artificial Intelligence', 3, 19.5, 0, 58.5)
                ''')

conn.commit()

# Querying data
cursor.execute("SELECT CUST_NAME, ORDER_TOTAL from SALES WHERE ORDER_NUM=1105910")
rows = cursor.fetchall()
for row in rows:
    print("CUST_NAME:", row[0])
    print("ORDER_TOTAL:", row[1], "\n")


# cursor.execute("SELECT * FROM Sales LIMIT 10")
# print(cursor.fetchall())
conn.close()

# \copy sales FROM '/home/kmaster/Documents/Databases/red30-postgres.csv' WITH DELIMITER ',' CSV HEADER;
