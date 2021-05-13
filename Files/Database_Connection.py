from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from sqlalchemy.orm import sessionmaker

SERVER = '192.168.0.252:1433'
DATABASE = 'Film'
DRIVER = 'ODBC Driver 17 for SQL Server'
USERNAME = 'SA'
PASSWORD = 'papadopulos'
DATABASE_CONNECTION = f'mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'

engine = create_engine(DATABASE_CONNECTION)
Base = declarative_base()

class User(Base):
    __tablename__ = 'Usuario'

    id = Column(Integer(), primary_key = True)
    username = Column(String(50), nullable = False, unique = True)
    password = Column(String(50), nullable = False, unique = True)
    created_at = Column(DateTime, default = datetime.now)

    def __str__(self):
        return self.username

Session = sessionmaker()
session = Session()

if __name__== '__main__':
    
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)