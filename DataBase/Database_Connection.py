from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, CHAR, ForeignKey
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import Binary, Boolean

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
    description = Column(String(915), nullable = True, unique = False)
    rating = Column(String(70), nullable = True, unique = False)
    to_watch = Column(Integer(), nullable = True, unique = False)
    already_seen = Column(Integer(), nullable = True, unique = False)
    top_button = Column(Integer(), nullable = True, unique = False)
    worst = Column(Integer(), nullable = True, unique = False)

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
        
        self.movie_name_search = ""
        self.update_name = ""
        self.update_date = ""
        self.update_countryid = ""
        self.update_genre_id = ""
        self.update_description = ""
        self.update_rating = ""

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
        
        self.movie_id = c.session.query(Movie_db.id).all()

        self.selected_user_id = c.session.query(User.id).filter(
            User.username == self.working_user
        ).first()

        self.movie_user = Movie_User(movie_id = f'{self.movie_id[-1][0]}', user_id = f'{self.selected_user_id[0]}')
        
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

    # Selecciona la data que se va a editar cuando se toca en una pelicula
    def select_edit_data(self):
               
        self.movie_atr_edit_temp = []   
        self.movie_id_temp = []

        self.user_id_edit = c.session.query(User.id).filter(
            User.username == self.working_user
        ).first()
        
        self.movie_id_edit = c.session.query(Movie_User.movie_id).filter(
            Movie_User.user_id == self.user_id_edit[0]
        ).all()
        
        for id in self.movie_id_edit:
            self.movie_id_temp.append(c.session.query(Movie_db.id).filter(
                Movie_db.name == self.movie_name_search
            ).filter(
                Movie_db.id == id[0]
            ).first())
        
        for i in self.movie_id_temp:
            if i != None:
                self.movie_id_def = i[0]
            else:
                pass

        self.movie_atr_edit_temp.append(c.session.query(Movie_db.name, Movie_db.movie_date, Movie_db.country_id, Movie_db.genre_id, Movie_db.description, Movie_db.rating).filter(
            Movie_db.id == self.movie_id_def
        )) 

        self.movie_name_edit = self.movie_atr_edit_temp[0][0][0]
        self.movie_date_edit = self.movie_atr_edit_temp[0][0][1]
        self.movie_country_edit = self.movie_atr_edit_temp[0][0][2]
        self.movie_genre_edit = self.movie_atr_edit_temp[0][0][3]
        self.movie_description_edit = self.movie_atr_edit_temp[0][0][4].strip()
        self.movie_rating_edit = self.movie_atr_edit_temp[0][0][5]

    # Actualiza los registros de la pelicula editada
    def update_changes(self):

        self.update_list = c.session.query(Movie_db).filter(
            Movie_db.id == self.movie_id_def 
        )
        self.update_list[0].name = self.update_name
        self.update_list[0].movie_date = self.update_date
        self.update_list[0].country_id = self.update_countryid
        self.update_list[0].genre_id = self.update_genre_id
        self.update_list[0].description = self.update_description
        self.update_list[0].rating = self.update_rating

        c.session.commit()

        self.update_name = ""
        self.update_date = ""
        self.update_countryid = ""
        self.update_genre_id = ""
        self.update_description = ""
        self.update_rating = ""

    def delete_movies(self):
        c.session.query(Movie_User).filter(
            Movie_User.movie_id == self.movie_id_def
        ).delete()
        
        c.session.query(Movie_db).filter(
            Movie_db.id == self.movie_id_def
        ).delete()

        c.session.commit()

    def assign_to_watch(self):
        self.to_watch = c.session.query(Movie_db).filter(
            Movie_db.id == self.movie_id_def
        )

        self.to_watch.to_watch = 1
        self.to_watch.already_seen = 0
        
    def assign_already_seen(self):
        self.already_seen = c.session.query(Movie_db).filter(
            Movie_db.id == self.movie_id_def
        )

        self.already_seen.already_seen = 1
        self.already_seen.to_watch = 0

    def assign_top(self):
        pass

    def assign_worst(self):
        pass

e = Execute()

# ATENCION: Lamentablemente no encontré el tipo de dato preciso para las últimas cuatro columnas de la tabla "Pelicula". En 
# SQL Alchemy existe el tipo de dato Boleano mientras que en SQL Server existe el tipo de dato bit y no pude hacer que ambos 
# hagan su trabajo correctamente. Por ende terminé usando el tipo de dato int, que no es lo mejor en performance para la tarea.
# Cualquier sugerencia se agradece.

# TODO 
# Una vez creados esos botones la segunda tarea seria atribuirles esas propiedades a las peliculas. Eso se puede hacer creando mas 
# columnas con la caracteristica de ser binario y leer de esa forma si es True o False.
# Para la logica de arriba va a ser necesario crear una logica adicional que permita leer si una peli ya esta por ejemplo en 
# "already seen". Si ese es el caso y el usuario quiere camibarla a to watch. Insertar en la columna de "already seen" un cero
# y en la otra un 1.
# Una vez finalizado toda esa parte lo ultimo que quedaria por hacer seria aplicar los filtros de busqueda en el main menu y hacer
# un poco mas lindo el display de peliculas.
# Una vez terminado todo lo de arriba y considerando que van a aparecer bugs. Taran ta tan
# ----> FINALIZACION DEL PROYECTO <--------