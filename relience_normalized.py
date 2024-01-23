from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class RELIENCE(Base):
    __tablename__ = 'RELIENCE'
    ID = Column(Integer, primary_key=True)
    NAME = Column(String(10), nullable=False)
    PRICE = Column(Integer)
    
    def __repr__(self):
        return f"({self.ID}, {self.NAME}, {self.PRICE})"

class NORMALIZED(Base):
    __tablename__ = 'NORMALIZED'
    N_ID = Column(Integer, primary_key=True)
    NORMALIZED_PRICE = Column(Integer)
    NORMALIZED_MEASUREMENT = Column(String)
    PRODUCT_ID = Column(Integer)
    
    def __repr__(self):
        return f"({self.N_ID}, {self.NORMALIZED_PRICE}, {self.NORMALIZED_MEASUREMENT}, {self.PRODUCT_ID})"

password = "Sooraj@rotech2023"
encoded_password = quote_plus(password)

engine = create_engine(f"mysql+pymysql://sooraj_usr:{encoded_password}@localhost/relience_grocery_store")

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


grocery = session.query(RELIENCE, NORMALIZED).filter(RELIENCE.ID == NORMALIZED.PRODUCT_ID).all()

for relience, normalized in grocery:
    print(relience.ID, relience.NAME, relience.PRICE, normalized.NORMALIZED_PRICE, normalized.NORMALIZED_MEASUREMENT)
