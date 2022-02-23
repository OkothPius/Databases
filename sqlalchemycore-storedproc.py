from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData

# engine = create_engine('postgres://postgres:password@localhost/red30')
engine = create_engine('postgresql://redruko:password@localhost/red30')

with engine.connect() as connection:
	meta = MetaData(engine)
	sales_table = Table('sales', meta, autoload=True, autoload_with=engine)
