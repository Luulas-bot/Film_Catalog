from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Connection():

    def __init__(self):
        self.set_vars()

    def set_vars(self):
        self.SERVER = '192.168.0.252:1433'
        self.DATABASE = 'Film'
        self.DRIVER = 'ODBC Driver 17 for SQL Server'
        self.USERNAME = 'SA'
        self.PASSWORD = 'papadopulos'
        self.DATABASE_CONNECTION = f'mssql://{self.USERNAME}:{self.PASSWORD}@{self.SERVER}/{self.DATABASE}?driver={self.DRIVER}'

    def create_session(self):
        Session = sessionmaker()
        self.session = Session.configure(bind = self.engine)
        self.session = Session()

    def run_engine(self):
        self.engine = create_engine(self.DATABASE_CONNECTION)

c = Connection()

class User(Base):
    __tablename__ = 'Usuario'

    id = Column(Integer(), primary_key = True)
    username = Column(String(50), nullable = False, unique = True)
    password = Column(String(50), nullable = False, unique = True)
    created_at = Column(DateTime, default = datetime.now)

    def __str__(self):
        return self.username

class Execute():
    
    def __init__(self):
        c.run_engine()
        c.create_session()
        Base.metadata.create_all(c.engine)

    def insert(self, in_var1, in_var2):
        self.in_var1 = in_var1
        self.in_var2 = in_var1
        self.user = User(username = f'{in_var1}', password = f'{in_var2}')

        c.session.add(self.user)

        c.session.commit()
        

    def select(self):
        pass

    def update(self):
        pass

    def delete(self):
        c.session.query(User).filter(
            User.id > 0
        ).delete()

        c.session.commit()

e = Execute()
# e.delete()
# e.insert()
# e.select()
# e.update()
