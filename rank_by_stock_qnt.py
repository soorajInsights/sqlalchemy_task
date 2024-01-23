from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import func
Base = declarative_base()

class RELIENCE(Base):
    __tablename__ = 'RELIENCE'
    ID = Column(Integer, primary_key=True)
    NAME = Column(String(10), nullable=False)
    PRICE = Column(Integer)
    CATEGORIES = Column(String(10))
    TOTAL_STOCK_QUANTITY = Column(Integer)
    
    def __repr__(self):
        return f"({self.ID}, {self.NAME}, {self.PRICE}, {self.CATEGORIES},{self.TOTAL_STOCK_QUANTITY})"

class JIOMART(Base):
    __tablename__ = 'JIOMART'
    ID = Column(Integer, primary_key=True)
    NAME = Column(String(10), nullable=False)
    PRICE = Column(Integer)
    CATEGORIES = Column(String(10))
    TOTAL_STOCK_QUANTITY = Column(Integer)
    
    def __repr__(self):
        return f"({self.ID}, {self.NAME}, {self.PRICE}, {self.CATEGORIES},{self.TOTAL_STOCK_QUANTITY})"

password = "Sooraj@rotech2023"
encoded_password = quote_plus(password)


engine = create_engine(f"mysql+pymysql://sooraj_usr:{encoded_password}@localhost/relience_grocery_store")

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

stock_r = session.query(RELIENCE).order_by(func.rank().over(order_by=RELIENCE.TOTAL_STOCK_QUANTITY)).all()
stock_j = session.query(JIOMART).order_by(func.rank().over(order_by=JIOMART.TOTAL_STOCK_QUANTITY)).all()



print("Data from RELIENCE table:")
for vegetable in stock_r:
    print(vegetable)

print("\nData from JIOMART table:")
for vegetable in stock_j:
    print(vegetable)
