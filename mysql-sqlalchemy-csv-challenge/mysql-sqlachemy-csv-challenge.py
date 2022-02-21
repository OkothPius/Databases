import pandas
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Connecting to the database
engine = create_engine("mysql+mysqlconnector://oruko:<P1r$Hg02ram/>@localhost:\
                        3306/red30", echo=True)

Base = declarative_base()

# Defining model
class Sales(Base):
    __tablename__='sales'
    __table_args__={"schema":"red30"}

    order_num = Column(Integer, primary_key=True)
    order_type = Column(String(250))
    cust_name = Column(String(250))
    cust_state = Column(String(250))
    prod_category = Column(String(250))
    prod_number = Column(String(250))
    prod_name = Column(String(250))
    quantity = Column(Float())
    price = Column(Float())
    discount = Column(Float())
    order_total = Column(Float())

    def __repr__(self):
        return '''<Sales(order_num='{0}', order_type='{1}',
        	cust_name='{2}', cust_state='{3}',
        	prod_category='{4}', prod_number='{5}',
        	prod_name='{6}', quantity='{7}', price='{8}',
        	discount='{9}', order_total='{10}')>'''.format(self.order_num,
        	self.order_type, self.cust_name,
        	self.cust_state, self.prod_category,
        	self.prod_number, self.prod_name,
        	self.quantity, self.price, self.discount, self.order_total)


Base.metadata.create_all(engine)

filename = 'red30.csv'

df = pandas.read_csv(filename)

df.to_sql(con=engine, name=Sales.__tablename__, if_exists='replace', index=False)

# Session
session = sessionmaker()
session.configure(bind=engine)
s = session()

# Query data
overall_max = s.query(func.max(Sales.order_total)).scalar()
print(overall_max)

results = s.query(Sales).order_by(Sales.order_total.desc()).limit(10)
print(r for r in results)
