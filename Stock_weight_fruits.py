from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, String, Integer, func
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class RELIENCE(Base):
    __tablename__ = 'RELIENCE'
    ID = Column(Integer, primary_key=True)
    NAME = Column(String(10), nullable=False)
    PRICE = Column(Integer)
    CATEGORIES = Column(String(10))
    STOCK_WEIGHT = Column(Integer)
    
    def __repr__(self):
        return f"({self.ID}, {self.NAME}, {self.PRICE}, {self.CATEGORIES},{self.STOCK_WEIGHT})"

class JIOMART(Base):
    __tablename__ = 'JIOMART'
    ID = Column(Integer, primary_key=True)
    NAME = Column(String(10), nullable=False)
    PRICE = Column(Integer)
    CATEGORIES = Column(String(10))
    STOCK_WEIGHT = Column(Integer)
    
    def __repr__(self):
        return f"({self.ID}, {self.NAME}, {self.PRICE}, {self.CATEGORIES},{self.STOCK_WEIGHT})"

password = "Sooraj@rotech2023"
encoded_password = quote_plus(password)

engine = create_engine(f"mysql+pymysql://sooraj_usr:{encoded_password}@localhost/relience_grocery_store")

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


total_stock_relience = session.query(RELIENCE.CATEGORIES, func.sum(RELIENCE.STOCK_WEIGHT)).group_by(RELIENCE.CATEGORIES).all()
total_stock_jiomart = session.query(JIOMART.CATEGORIES, func.sum(JIOMART.STOCK_WEIGHT)).group_by(JIOMART.CATEGORIES).all()

print("Total Stock Weight from RELIENCE:")
for category, total_stock_weight in total_stock_relience:
    print(f"Category: {category}, Total Stock Weight: {total_stock_weight}")

print("\nTotal Stock Weight from JIOMART:")
for category, total_stock_weight in total_stock_jiomart:
    print(f"Category: {category}, Total Stock Weight: {total_stock_weight}")
