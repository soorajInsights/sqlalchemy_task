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


avg_price_relience = session.query(func.avg(RELIENCE.PRICE)).scalar()
above_avg_r = session.query(RELIENCE).filter(RELIENCE.PRICE > avg_price_relience)



avg_price_jiomart = session.query(func.avg(JIOMART.PRICE)).scalar()
above_avg_j = session.query(JIOMART).filter(JIOMART.PRICE > avg_price_jiomart)


print("Data from RELIENCE table:")
for vegetable in above_avg_r:
    print(vegetable)

print("\nData from JIOMART table:")
for vegetable in above_avg_j:
    print(vegetable)
