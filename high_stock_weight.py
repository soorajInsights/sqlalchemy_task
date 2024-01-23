from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, String, Integer, func
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class RELIENCE(Base):
    __tablename__ = 'RELIENCE'
    ID = Column(Integer, primary_key=True)
    NAME = Column(String(10), nullable=False)
    STOCK_WEIGHT = Column(Integer)
    
    def __repr__(self):
        return f"({self.ID}, {self.NAME},{self.STOCK_WEIGHT})"

class JIOMART(Base):
    __tablename__ = 'JIOMART'
    ID = Column(Integer, primary_key=True)
    NAME = Column(String(10), nullable=False)
    STOCK_WEIGHT = Column(Integer)
    
    def __repr__(self):
        return f"({self.ID}, {self.NAME},{self.STOCK_WEIGHT})"

password = "Sooraj@rotech2023"
encoded_password = quote_plus(password)

engine = create_engine(f"mysql+pymysql://sooraj_usr:{encoded_password}@localhost/relience_grocery_store")

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


high_stock_r = session.query(func.max(RELIENCE.STOCK_WEIGHT)).scalar()
stock_r = session.query(RELIENCE).filter(RELIENCE.STOCK_WEIGHT == high_stock_r)

high_stock_j = session.query(func.max(JIOMART.STOCK_WEIGHT)).scalar()
stock_j = session.query(JIOMART).filter(JIOMART.STOCK_WEIGHT == high_stock_j)

for i in stock_r:
    print(i)

for j in stock_j:
    print(j)
