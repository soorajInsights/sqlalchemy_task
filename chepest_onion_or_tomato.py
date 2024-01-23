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


min_price_relience = session.query(func.min(RELIENCE.PRICE)).filter(RELIENCE.NAME == 'TOMATO').scalar()
chepest_r = session.query(RELIENCE).filter((RELIENCE.PRICE == min_price_relience) & (RELIENCE.NAME == 'TOMATO')).first()

min_price_jiomart = session.query(func.min(JIOMART.PRICE)).filter(JIOMART.NAME == 'TOMATO').scalar()
chepest_j = session.query(JIOMART).filter((JIOMART.PRICE == min_price_jiomart) & (JIOMART.NAME == 'TOMATO')).first()

print("Chepest tomato from RELIENCE table:")
print(chepest_r)

print("\nChepest tomato from JIOMART table:")
print(chepest_j)
