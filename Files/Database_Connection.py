from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, CHAR, ForeignKey
from datetime import datetime
from sqlalchemy.orm import sessionmaker

# Se crea la base
Base = declarative_base()

# Creación de la conexión con la base de datos
class Connection():

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

    id = Column(Integer(), primary_key = True)
    username = Column(String(50), nullable = False, unique = True)
    password = Column(String(50), nullable = False, unique = False)
    created_at = Column(DateTime, default = datetime.now)
    movies_id = Column(Integer(), ForeignKey('Pelicula.id'))

    def __str__(self):
        return self.username

class Movie_db(Base):
    __tablename__ = "Pelicula"

    id = Column(Integer(), primary_key = True)
    name = Column(String(70), nullable = False, unique = True)
    movie_date = Column(String(50), nullable = True, unique = False)
    country_id = Column(CHAR(3), ForeignKey('Pais.id'))
    genre_id = Column(CHAR(3), ForeignKey('Genero.id'))
    description = Column(String(500), nullable = True, unique = False)

class Country(Base):
    __tablename__ = 'Pais'

    id = Column(CHAR(3), primary_key = True)
    name = Column(String(50), nullable = False, unique = True)

class Genre(Base):
    __tablename__ = "Genero"

    id = Column(CHAR(3), primary_key = True)
    name = Column(String(50), nullable = False, unique = True)

c = Connection()

# Creación de la clase que contiene lo scripts para manejar la base de datos
class Execute():
    
    def __init__(self):
        c.run_engine()
        c.create_session()
        Base.metadata.create_all(c.engine)

    # Inserción de los datos de un nuevo usuario creado a la tabla Usuario
    def insert_sign_up(self, in_var1, in_var2):
        self.in_var1 = in_var1
        self.in_var2 = in_var2
        self.user = User(username = f'{self.in_var1}', password = f'{self.in_var2}')

        c.session.add(self.user)

        c.session.commit()
        
    # Lectura de los datos de un usuario en específico
    def select_login(self, username, password):
        self.username_sl = username
        self.password_sl = password
        self.user_sl = c.session.query(User).filter(
            User.username == self.username_sl
        ).filter(
            User.password == self.password_sl
        )  

    # Función para insertar peliculas
    def insert_movies(self, name, date, country, description):
        self.name_movie = name
        self.date_movie = date
        self.country_movie = country
        self.description_movie = description

        self.movie = Movie_db(name = f'{self.name_movie}', movie_date = f'{self.date_movie}', movie_genre_id = f'{self.country_movie}', description = f'{self.description_movie}' )

        c.session.add(self.movie)
        c.session.commit()

    def update(self):
        pass

    def delete(self):
        c.session.query(User).filter(
            User.id > 0
        ).delete()

        c.session.commit()

e = Execute()

# ATENCIÓN: La base de datos no es manejada por un sistema de tipo crear y borrar. Esto significa que cada vez que se quiere
# modificar la base de datos, no se inserta todo y se borra todo, sino que se inserta solo. Después existe la funcion de borrar.
# está heca de este modo, para una optimización mayor.