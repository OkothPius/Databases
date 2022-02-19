import pandas
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Connecting to our database
engine = create_engine("mysql+mysqlconnector://oruko:<P1r$Hg02ram/>@localhost:\
                        3306/landon", echo=True)

Base = declarative_base()

class Purchase(Base):
	__tablename__ = 'purchases'
	__table_args__ = {"schema":"landon"}

	order_id = Column(Integer, primary_key=True)
	property_id = Column(Integer)
	property_city = Column(String(250))
	property_state = Column(String(250))
	product_id = Column(Integer)
	product_category = Column(String(250))
	product_name = Column(String(250))
	quantity = Column(Integer)
	product_price = Column(Float)
	order_total = Column(Float)

	def __repr__(self):
		return '''<Purchase(order_id='{0}', property_id='{1}',
			property_city='{2}', property_state='{3}',
			product_id='{4}', product_category='{5}',
			product_name='{6}', quantity='{7}', product_price='{8}',
			order_total='{9}')>'''.format(self.order_id,
			self.property_id, self.property_city,
			self.property_state, self.product_id,
			self.product_category, self.product_name,
			self.quantity, self.product_price, self.order_total)

Base.metadata.create_all(engine)

filename = "landon.csv"

df = pandas.read_csv(filename)

df.to_sql(con=engine, name=Purchase.__tablename__, if_exists='append', index=False)

session = sessionmaker()
session.configure(bind=engine)
s = session()

results = s.query(Purchase).limit(10).all()
for r in results:
	print(r)
