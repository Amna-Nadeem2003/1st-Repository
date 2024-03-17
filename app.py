from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Defining the database engine
engine = create_engine('sqlite:///pakwheels.db', echo=True)

# Defining the Session class
Session = sessionmaker()
Session.configure(bind=engine)

# Defining the base class for declarative class definitions
Base = declarative_base()

# Defining the model for the seller
class Seller(Base):
    __tablename__ = 'sellers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    cars = relationship('Car', back_populates='seller')

# Defining the model for the car
class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    price = Column(Integer)
    seller_id = Column(Integer, ForeignKey('sellers.id'))
    seller = relationship('Seller', back_populates='cars')

# Creating tables in the database
Base.metadata.create_all(engine)

# Creating a session
session = Session()

# Adding sample data
seller = Seller(name='Amna Nadeem', location='Karachi')
car = Car(make='Toyota', model='Corolla', year=2019, price=1500000, seller=seller)
session.add(seller)
session.add(car)

# Committing the changes to the database
session.commit()

# Querying the database
result = session.query(Car).all()
print(result)

# Closing the session
session.close()
