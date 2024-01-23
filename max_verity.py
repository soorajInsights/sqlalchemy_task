from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import func

Base = declarative_base()

class RELIENCE(Base):
    __tablename__ = 'RELIENCE'
    ID = Column(Integer, primary_key=True)
    NAME = Column(String(10), nullable=False)
    VERITY= Column(String)
    
    def __repr__(self):
        return f"({self.ID}, {self.NAME}, {self.VERITY})"

class JIOMART(Base):
    __tablename__ = 'JIOMART'
    ID = Column(Integer, primary_key=True)
    NAME = Column(String(10), nullable=False)
    VERITY= Column(String)
    
    def __repr__(self):
        return f"({self.ID}, {self.NAME}, {self.VERITY})"

password = "Sooraj@rotech2023"
encoded_password = quote_plus(password)


engine = create_engine(f"mysql+pymysql://sooraj_usr:{encoded_password}@localhost/relience_grocery_store")

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


max_variety_relience = session.query(RELIENCE.NAME, func.count(RELIENCE.VERITY)).group_by(RELIENCE.NAME).all()
max_verity_jiomart = session.query(JIOMART.NAME,func.count(JIOMART.VERITY)).group_by(JIOMART.NAME).all()

print('Data from relience:')
for relience_max in max_variety_relience:
    print(relience_max)

print('\nData from jiomart')    
for jiomart_max in max_verity_jiomart:
    print(jiomart_max)
    
