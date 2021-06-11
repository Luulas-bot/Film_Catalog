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

    id = Column(Integer(), primary_key = True, autoincrement = True, nullable = False)
    username = Column(String(50), nullable = False, unique = True)
    password = Column(String(50), nullable = False, unique = False)
    created_at = Column(DateTime, default = datetime.now)

    def __str__(self):
        return self.username

# Creación de la tabla de las películas
class Movie_db(Base):
    __tablename__ = "Pelicula"

    id = Column(Integer(), primary_key = True, autoincrement = True, nullable = False)
    name = Column(String(70), nullable = False, unique = False)
    movie_date = Column(String(50), nullable = True, unique = False)
    country_id = Column(CHAR(3), ForeignKey('Pais.id'))
    genre_id = Column(CHAR(3), ForeignKey('Genero.id'))
    description = Column(String(500), nullable = True, unique = False)

# Creación de la tabla de los países
class Country(Base):
    __tablename__ = 'Pais'

    id = Column(CHAR(3), primary_key = True, nullable = False)
    name = Column(String(50), nullable = False, unique = True)

# Creación de la tabla de los géneros
class Genre(Base):
    __tablename__ = "Genero"

    id = Column(CHAR(3), primary_key = True, nullable = False)
    name = Column(String(50), nullable = False, unique = True)

# Creación de la tabla que contiene a los usuarios con sus respectivas películas
class Movie_User(Base):
    __tablename__ = 'Pelicula_Usuario'

    id = Column(Integer(), primary_key = True, autoincrement = True, nullable = False)
    movie_id = Column(Integer(), ForeignKey('Pelicula.id'))
    user_id = Column(Integer(), ForeignKey('Usuario.id'))

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
        
    # Lectura de los datos de un usuario en específico para el Login
    def select_login(self, username, password):
        self.username_sl = username
        self.password_sl = password
        self.user_sl = c.session.query(User).filter(
            User.username == self.username_sl
        ).filter(
            User.password == self.password_sl
        )  

        self.working_user = username

    # Función para insertar peliculas
    def insert_movies(self, name, date, country, genre, description):
        self.name_movie = name
        self.date_movie = date
        self.country_movie = country
        self.genre_movie = genre
        self.description_movie = description

        self.movie = Movie_db(name = f'{self.name_movie}', movie_date = f'{self.date_movie}', country_id = f'{self.country_movie}',
        genre_id = f'{self.genre_movie}', description = f'{self.description_movie}')
        
        c.session.add(self.movie)
        c.session.flush()
        c.session.commit()

    # Función para insertar a la tabla 'Pelicula_Usuario' la película insertada recientemente y el usuario que la insertó
    def insert_Pelicula_Usuario(self):
        
        self.movie_id = c.session.query(Movie_db.id).filter(
            Movie_db.name == self.name_movie
        ).first()
        
        self.selected_user_id = c.session.query(User.id).filter(
            User.username == self.working_user
        ).first()
        
        self.movie_user = Movie_User(movie_id = f'{self.movie_id[0]}', user_id = f'{self.selected_user_id[0]}')
        
        c.session.add(self.movie_user)
        c.session.flush()
        c.session.commit()

    # Función que a través de select, filtros e inner joins arma algunas listas con los nombres de las películas y sus géneros
    def select_movies_to_display(self):

        self.movies_display_name_temp = []
        self.movies_display_genreid_temp = []
        self.movies_display_genre_name_temp = []
        self.movies_display_name = []
        self.movies_display_genreid = []
        self.movies_display_genre_name = []

        self.user_id_display = c.session.query(User.id).filter(
            User.username == self.working_user
        ).first()

        self.movies_display_id = c.session.query(Movie_User.movie_id).filter(
            Movie_User.user_id == self.user_id_display[0]
        )
        for i in self.movies_display_id:
            self.movies_display_name_temp.append(c.session.query(Movie_db.name).filter(
                Movie_db.id == i[0]
            ))
        
        for i in self.movies_display_id:
            self.movies_display_genreid_temp.append(c.session.query(Movie_db.genre_id).filter(
                Movie_db.id == i[0]
            ))

        for i in self.movies_display_genreid_temp:
            self.movies_display_genre_name_temp.append(c.session.query(Genre.name).filter(
                Genre.id == i[0][0]
            )) 

        for i in self.movies_display_name_temp:
            self.movies_display_name.append(i[0][0])
            
        for i in self.movies_display_genre_name_temp:
            self.movies_display_genre_name.append(i[0][0])

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

# El TODO Más grande de la historia:
# - Lo primero que tengo que hacer es crear una función que tome las primeras 6 peliculas del usuario que está usando el programa
# en el momento y que las ponga en una lista o diccionario. Lo que tiene que leer es el nombre, el género y el rating.
# - La segunda cosa que hay que hacer es dentro de la clase de las peliculas crear una función que tome estos datos y los ponga bien
# donde tienen que ir, por ejemplo en el texto del nombre, y así
# - Lo tercero que hay que hacer es dentro de la misma clase crear una fuente que se adapte al tamaño del nombre de la pelicula
# - Lo cuarto que hay que hacer es encontrar las forma de hacer un display de todo esto en cada rectangulo.
# - Lo quinto vemdría a ser, que cuando yo toque la flecha para avanzar, la función que lee las películas lea las siguientes seis 
# peliculas y haga todo el recorrido de vuelta para mostrarlas por pantalla como es debido.
# SUERTE! 
