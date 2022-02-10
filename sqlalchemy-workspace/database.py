import sqlalchemy as db

engine = db.create_engine('sqlite:///movies.db')

connection = engine.connect()

metadata = db.MetaData()

movies = db.Table('Movies', metadata, autoload=True, autoload_with=engine)


# Querying all objects
query = db.select([movies])

result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()

print(result_set[0])
print(result_set)


# Filter by Director
query = db.select([movies]).where(movies.columns.DIRECTOR == "Martin Scorsese")

result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()

print(result_set[0])


# Inserting an object in database
query = movies.insert().values(Title="Pyscho", DIRECTOR="Alfred Hitchcock", YEAR="1969")

connection.execute(query)

query = db.select([movies])
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()

print(result_set)
