# Imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, CHAR, ForeignKey
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import Boolean

# Se crea la base
Base = declarative_base()

# Creación de la conexión con la base de datos
class Connection():
    
    # Función constructora
    def __init__(self):
        self.set_vars()
    
    # Inicializa las variables
    def set_vars(self):
        self.SERVER = '192.168.0.252:1433'
        self.DATABASE = 'Film'
        self.DRIVER = 'ODBC Driver 17 for SQL Server'
        self.USERNAME = 'SA'
        self.PASSWORD = 'papadopulos'
        self.DATABASE_CONNECTION = f'mssql://{self.USERNAME}:{self.PASSWORD}@{self.SERVER}/{self.DATABASE}?driver={self.DRIVER}'

    # Crea una sesión
    def create_session(self):
        Session = sessionmaker()
        self.session = Session.configure(bind = self.engine)
        self.session = Session()

    # Corre el motor de la base de datos
    def run_engine(self):
        self.engine = create_engine(self.DATABASE_CONNECTION)

# Creación de la tabla de usuario
class User(Base):
    __tablename__ = 'Usuario'

    # Creación de las columnas
    id = Column(Integer(), primary_key = True, autoincrement = True, nullable = False)
    username = Column(String(50), nullable = False, unique = True)
    password = Column(String(50), nullable = False, unique = False)
    created_at = Column(DateTime, default = datetime.now)

    def __str__(self):
        return self.username

# Creación de la tabla de las películas
class MovieDb(Base):
    __tablename__ = "Pelicula"

    # Creación de las columnas
    id = Column(Integer(), primary_key = True, autoincrement = True, nullable = False)
    name = Column(String(70), nullable = False, unique = False)
    movie_date = Column(String(50), nullable = True, unique = False)
    country_id = Column(CHAR(3), ForeignKey('Pais.id'))
    genre_id = Column(CHAR(3), ForeignKey('Genero.id'))
    description = Column(String(915), nullable = True, unique = False)
    rating = Column(String(70), nullable = True, unique = False)
    to_watch = Column(Boolean(), nullable = True, unique = False)
    already_seen = Column(Boolean(), nullable = True, unique = False)
    top_button = Column(Boolean(), nullable = True, unique = False)
    worst = Column(Boolean(), nullable = True, unique = False)

# Creación de la tabla de los países
class Country(Base):
    __tablename__ = 'Pais'

    # Creación de las columnas
    id = Column(CHAR(3), primary_key = True, nullable = False)
    name = Column(String(50), nullable = False, unique = True)

# Creación de la tabla de los géneros
class Genre(Base):
    __tablename__ = "Genero"

    # Creación de las columnas
    id = Column(CHAR(3), primary_key = True, nullable = False)
    name = Column(String(50), nullable = False, unique = True)

# Creación de la tabla que contiene a los usuarios con sus respectivas películas
class MovieUser(Base):
    __tablename__ = 'Pelicula_Usuario'

    # Creación de las columnas
    id = Column(Integer(), primary_key = True, autoincrement = True, nullable = False)
    movie_id = Column(Integer(), ForeignKey('Pelicula.id'))
    user_id = Column(Integer(), ForeignKey('Usuario.id'))
