from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData

# engine = create_engine('postgres://postgres:password@localhost/red30')
engine = create_engine('postgresql://redruko:password@localhost/red30',
						isolation_level="AUTOCOMMIT")

with engine.connect() as connection:
	meta = MetaData(engine)
	sales_table = Table('sales', meta, autoload=True, autoload_with=engine)

	# connection.execute('COMMIT')
	connection.execute('CALL return_nondiscounted_item (%s, %s)', (1105910, 1))
