from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import func

Base = declarative_base()

class GROCERY(Base):
    __tablename__ = 'RELIENCE'
    ID = Column(Integer, primary_key=True)
    NAME = Column(String(10), nullable=False)
    PRICE = Column(Integer)
    CATEGORIES = Column(String(10))
    
    def __repr__(self):
        return f"({self.ID}, {self.NAME}, {self.PRICE}, {self.CATEGORIES})"

class JIOMART(Base):
    __tablename__ = 'JIOMART'
    ID = Column(Integer, primary_key=True)
    NAME = Column(String(10), nullable=False)
    PRICE = Column(Integer)
    CATEGORIES = Column(String(10))
    
    def __repr__(self):
        return f"({self.ID}, {self.NAME}, {self.PRICE}, {self.CATEGORIES})"


password = "Sooraj@rotech2023"
encoded_password = quote_plus(password)


engine = create_engine(f"mysql+pymysql://sooraj_usr:{encoded_password}@localhost/relience_grocery_store")

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


vegetables_relience_rank = session.query(GROCERY).filter_by(CATEGORIES='VEGETABLES').order_by(func.rank().over(order_by=GROCERY.PRICE))
vegetables_jiomart_rank = session.query(JIOMART).filter_by(CATEGORIES='VEGETABLES').order_by(func.rank().over(order_by=JIOMART.PRICE))


print("Data from RELIENCE table:")
for vegetable in vegetables_relience_rank:
    print(vegetable)


print("\nData from JIOMART table:")
for vegetable in vegetables_jiomart_rank:
    print(vegetable)
