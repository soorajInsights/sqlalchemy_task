from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class RELIENCE(Base):
    __tablename__ = 'RELIENCE'
    ID = Column(Integer, primary_key=True)
    NAME = Column(String(10), nullable=False)
    COUNTRY_OF_ORIGIN = Column(String)
    
    def __repr__(self):
        return f"({self.ID}, {self.NAME}, {self.COUNTRY_OF_ORIGIN})"

class JIOMART(Base):
    __tablename__ = 'JIOMART'
    ID = Column(Integer, primary_key=True)
    NAME = Column(String(10), nullable=False)
    COUNTRY_OF_ORIGIN = Column(String)
    
    def __repr__(self):
        return f"({self.ID}, {self.NAME}, {self.COUNTRY_OF_ORIGIN})"


password = "Sooraj@rotech2023"
encoded_password = quote_plus(password)


engine = create_engine(f"mysql+pymysql://sooraj_usr:{encoded_password}@localhost/relience_grocery_store")

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


apple_relience = session.query(RELIENCE.NAME,RELIENCE.COUNTRY_OF_ORIGIN).filter_by(NAME = 'APPLE').group_by(RELIENCE.COUNTRY_OF_ORIGIN).all()
apple_jiomart = session.query(JIOMART.NAME,JIOMART.COUNTRY_OF_ORIGIN).filter_by(NAME = 'APPLE').group_by(JIOMART.COUNTRY_OF_ORIGIN).all()


print("Data from RELIENCE table:")
for i in apple_relience:
    print(i)

print("\nData from JIOMART table:")
for j in apple_jiomart:
    print(j)
