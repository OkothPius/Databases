import sqlalchemy as db

engine = db.create_engine('sqlite:///users-sqlalchemy.db')

metadata = db.MetaData()


connection = engine.connect()

users = db.Table('Users', metadata,
        db.Column('user_id', db.Integer, primary_key=True),
        db.Column('first_name', db.Text),
        db.Column('last_name', db.Text),
        db.Column('email_address', db.Text))


metadata.create_all(engine)


insertion_query = users.insert().values([
    {"first_name":"Tine", "last_name":"Mccoy", "email_address":"tmccoy@test.com"},
    {"first_name":"Jared", "last_name":"Ed", "email_address":"jed@test.com"},
    {"first_name":"Tim", "last_name":"Ored", "email_address":"timeor@test.com"},
    {"first_name":"John", "last_name":"Doe", "email_address":"jdoe@test.com"},
    {"first_name":"Mark", "last_name":"Mccoy", "email_address":"markm@test.com"}
    ])


connection.execute(insertion_query)

selection_query = db.select([users.columns.email_address])
selection_result = connection.execute(selection_query)

print(selection_result.fetchall())
