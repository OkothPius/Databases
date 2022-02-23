from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgres://postgres:password@localhost/red30')
Base = declarative_base(engine)
Base.metadata.reflect(engine)

class Sales(Base):
    __table__ = Base.metadata.tables['sales']

    def __repr__(self):
        return '''<Sale(order_num='{0}', order_type'{1}', cust_name='{2}', 
            prod_name='{3}', quantity='{4}', 
            order_total='{5}')>'''.format(self.order_num, 
            self.order_type, self.cust_name, self.prod_name, 
            self.quantity, self.order_total)

def loadSession():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

if __name__ == "__main__":
    session = loadSession()

    # Read
    smallest_sales = session.query(Sales).order_by(Sales.order_total).limit(10)
    print(smallest_sales[0].cust_name)

    # Insert
    recent_sale = Sales(order_num=1105910, order_type='Retail', cust_name='Syman Mapstone', prod_number='EB521', prod_name='Understanding Artificial Intelligence', quantity=3, price=19.5, discount=0, order_total=58.5)
    print(recent_sale)
    session.add(recent_sale)
    session.commit()

    # Update
    recent_sale.quantity = 2
    recent_sale.order_total = 39
    session.commit()
    updated_sale = session.query(Sales).filter(Sales.order_num == 1105910).first()
    print(updated_sale)

    # Delete
    returned_sale = session.query(Sales).filter(Sales.order_num == 1105910).first()
    session.delete(returned_sale)
    session.commit()








