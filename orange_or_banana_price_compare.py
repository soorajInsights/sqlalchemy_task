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
    
    def __repr__(self):
        return f"({self.ID}, {self.NAME}, {self.PRICE})"

class JIOMART(Base):
    __tablename__ = 'JIOMART'
    ID = Column(Integer, primary_key=True)
    NAME = Column(String(10), nullable=False)
    PRICE = Column(Integer)
    
    def __repr__(self):
        return f"({self.ID}, {self.NAME}, {self.PRICE})"

password = "Sooraj@rotech2023"
encoded_password = quote_plus(password)


engine = create_engine(f"mysql+pymysql://sooraj_usr:{encoded_password}@localhost/relience_grocery_store")

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


orange_r = session.query(RELIENCE.NAME,RELIENCE.PRICE).filter(RELIENCE.NAME=='ORANGE')
orange_j = session.query(JIOMART.NAME,JIOMART.PRICE).filter(JIOMART.NAME=='ORANGE')

print('Orange price from relience')
for i in orange_r:
    print(i)
    
print('\nOrange price from jiomart')
for j in orange_j:
    print(j)