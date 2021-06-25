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

# Creación de la tabla de las películas
class Movie_db(Base):
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
class Movie_User(Base):
    __tablename__ = 'Pelicula_Usuario'

    # Creación de las columnas
    id = Column(Integer(), primary_key = True, autoincrement = True, nullable = False)
    movie_id = Column(Integer(), ForeignKey('Pelicula.id'))
    user_id = Column(Integer(), ForeignKey('Usuario.id'))

c = Connection()

# Creación de la clase que contiene lo scripts para manejar la base de datos
class Execute():
    
    # Función constructora
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
        self.country_text = ""

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

        # Toma el id del usuario en uso
        self.user_id_display = c.session.query(User.id).filter(
            User.username == self.working_user
        ).first()

        # Filtra todas los id de las películas del usuario en uso
        self.movies_display_id = c.session.query(Movie_User.movie_id).filter(
            Movie_User.user_id == self.user_id_display[0]
        )

        # Toma a partir de los id de las películas, sus nombres
        for i in self.movies_display_id:
            self.movies_display_name_temp.append(c.session.query(Movie_db.name).filter(
                Movie_db.id == i[0]
            ))

        # Toma a partir de los id de las películas sus id de género
        for i in self.movies_display_id:
            self.movies_display_genreid_temp.append(c.session.query(Movie_db.genre_id).filter(
                Movie_db.id == i[0]
            ))

        # Toma a partir de los id de género los nombres de esos géneros
        for i in self.movies_display_genreid_temp:
            self.movies_display_genre_name_temp.append(c.session.query(Genre.name).filter(
                Genre.id == i[0][0]
            )) 

        # Limpia la lista de nombres
        for i in self.movies_display_name_temp:
            self.movies_display_name.append(i[0][0])

        # Limpia la lista de los nombres de los géneros
        for i in self.movies_display_genre_name_temp:
            self.movies_display_genre_name.append(i[0][0])

    # Selecciona la data que se va a editar cuando se toca en una pelicula
    def select_edit_data(self):
               
        self.movie_atr_edit_temp = []   
        self.movie_id_temp = []

        # Toma el id del usuario en uso
        self.user_id_edit = c.session.query(User.id).filter(
            User.username == self.working_user
        ).first()

        # Filtra todos los id de las películas de ese usuario
        self.movie_id_edit = c.session.query(Movie_User.movie_id).filter(
            Movie_User.user_id == self.user_id_edit[0]
        ).all()
        
        # Toma el id en específico de la película que se seleccionó
        for id in self.movie_id_edit:
            self.movie_id_temp.append(c.session.query(Movie_db.id).filter(
                Movie_db.name == self.movie_name_search
            ).filter(
                Movie_db.id == id[0]
            ).first())
        
        # Limpia la lista para quedarse solo con el id en específico
        for i in self.movie_id_temp:
            if i != None:
                self.movie_id_def = i[0]
            else:
                pass

        # Filtra todos los atributos que se quieren meter en variables a través del id
        self.movie_atr_edit_temp.append(c.session.query(Movie_db.name, Movie_db.movie_date, Movie_db.country_id, Movie_db.genre_id, Movie_db.description, Movie_db.rating).filter(
            Movie_db.id == self.movie_id_def
        )) 

        # Transfiere los atributos a unas variables
        self.movie_name_edit = self.movie_atr_edit_temp[0][0][0]
        self.movie_date_edit = self.movie_atr_edit_temp[0][0][1]
        self.movie_country_edit = self.movie_atr_edit_temp[0][0][2]
        self.movie_genre_edit = self.movie_atr_edit_temp[0][0][3]
        self.movie_description_edit = self.movie_atr_edit_temp[0][0][4].strip()
        self.movie_rating_edit = self.movie_atr_edit_temp[0][0][5]

    # Actualiza los registros de la pelicula editada
    def update_changes(self):

        # Crea una variable que contenga todos las columnas de la película con el id que se seleccionó 
        self.update_list = c.session.query(Movie_db).filter(
            Movie_db.id == self.movie_id_def 
        )

        # Updatea las columnas de esa películas
        self.update_list[0].name = self.update_name
        self.update_list[0].movie_date = self.update_date
        self.update_list[0].country_id = self.update_countryid
        self.update_list[0].genre_id = self.update_genre_id
        self.update_list[0].description = self.update_description
        self.update_list[0].rating = self.update_rating

        c.session.commit()

        # Limpia las variables para que sean reutilizables
        self.update_name = ""
        self.update_date = ""
        self.update_countryid = ""
        self.update_genre_id = ""
        self.update_description = ""
        self.update_rating = ""

    # Borra la película seleccionada
    def delete_movies(self):
        # Borra la película que se seleccionó de la tabla de las películas y usuarios
        c.session.query(Movie_User).filter(
            Movie_User.movie_id == self.movie_id_def
        ).delete()
        
        # Borra la película de la tabla de las películas
        c.session.query(Movie_db).filter(
            Movie_db.id == self.movie_id_def
        ).delete()

        c.session.commit()

    # Asigna un uno si la pelicula está en modo "to_watch" a la db
    def assign_to_watch(self):
        self.to_watch = c.session.query(Movie_db).filter(
            Movie_db.id == self.movie_id_def
        ).update(
            {
                'to_watch' : 1,
                'already_seen' : 0
            }
        )

        c.session.commit()
        c.session.flush()

    # Asigna un uno si la pelicula está en modo "already_seen" a la db
    def assign_already_seen(self):
        c.session.query(Movie_db).filter(
            Movie_db.id == self.movie_id_def
        ).update(
            {
                'already_seen' : 1,
                'to_watch' : 0
            }
        )

        c.session.commit()
        c.session.flush()

    # Asigna un uno si la pelicula está en modo "top" a la db
    def assign_top(self):
        c.session.query(Movie_db).filter(
            Movie_db.id == self.movie_id_def
        ).update(
            {
                'top_button' : 1,
                'worst' : 0
            }
        )

        c.session.commit()
        c.session.flush()

    # Asigna un uno si la pelicula está en modo "worst" a la db
    def assign_worst(self):
        c.session.query(Movie_db).filter(
            Movie_db.id == self.movie_id_def
        ).update(
            {
                'worst' : 1,
                'top_button' : 0
            }
        )

        c.session.commit()
        c.session.flush()

    # Filtra las películas con el filtro "to_watch"
    def filter_to_watch(self):
        self.movies_display_name = []
        self.movies_display_genre_name = []
        self.name_filter_temp = []
        self.genreid_filter_temp = []
        self.genre_name_filter_temp = []
        
        # Filtra el usuario que está en uso
        self.user_id_filter = c.session.query(User.id).filter(
            User.username == self.working_user
        ).first()
        
        # Filtra todas las películas del usuario que está en uso
        self.movie_id_filter_temp = c.session.query(Movie_User.movie_id).filter(
            Movie_User.user_id == self.user_id_filter[0]
        ).all()
        
        # Filtra todas las películas de la db que tengan un uno en el campo "to_watch"
        self.movie_id_filter_to_watch = c.session.query(Movie_db.id).filter(
            Movie_db.to_watch == 1
        ).all()
        
        # Obtiene los duplicados de la lista de todas las pelis del usuario, y todas las pelis con el campo en un de "to_watch"
        self.movie_id_filter_def = set(self.movie_id_filter_temp).intersection(self.movie_id_filter_to_watch)

        # Obtiene el nombre de la película a través del id
        for id in self.movie_id_filter_def:
            self.name_filter_temp.append(c.session.query(Movie_db.name).filter(
                Movie_db.id == id[0]
            ))

        # Obtiene el id de género
        for i in self.movie_id_filter_def:
            self.genreid_filter_temp.append(c.session.query(Movie_db.genre_id).filter(
                Movie_db.id == i[0]
            ))

        # Obtiene el nombre de género a través de su id
        for i in self.genreid_filter_temp:
            self.genre_name_filter_temp.append(c.session.query(Genre.name).filter(
                Genre.id == i[0][0]
            )) 

        # Limpia la lista de los nombres de las películas
        for i in self.name_filter_temp:
            self.movies_display_name.append(i[0][0])

        # Limpia la lista de los nombres de género
        for i in self.genre_name_filter_temp:
            self.movies_display_genre_name.append(i[0][0])

    # Filtra las películas por el campo "already_seen". Mismo funcionamiento que la función para filtrar por el "to_watch"
    def filter_already_seen(self):
        self.movies_display_name = []
        self.movies_display_genre_name = []
        self.name_filter_temp = []
        self.genreid_filter_temp = []
        self.genre_name_filter_temp = []
        
        self.user_id_filter = c.session.query(User.id).filter(
            User.username == self.working_user
        ).first()

        self.movie_id_filter_temp = c.session.query(Movie_User.movie_id).filter(
            Movie_User.user_id == self.user_id_filter[0]
        ).all()
        
        self.movie_id_filter_alreadyseen = c.session.query(Movie_db.id).filter(
            Movie_db.already_seen == 1
        ).all()
        
        self.movie_id_filter_def = set(self.movie_id_filter_temp).intersection(self.movie_id_filter_alreadyseen)

        for id in self.movie_id_filter_def:
            self.name_filter_temp.append(c.session.query(Movie_db.name).filter(
                Movie_db.id == id[0]
            ))

        for i in self.movie_id_filter_def:
            self.genreid_filter_temp.append(c.session.query(Movie_db.genre_id).filter(
                Movie_db.id == i[0]
            ))

        for i in self.genreid_filter_temp:
            self.genre_name_filter_temp.append(c.session.query(Genre.name).filter(
                Genre.id == i[0][0]
            )) 

        for i in self.name_filter_temp:
            self.movies_display_name.append(i[0][0])

        for i in self.genre_name_filter_temp:
            self.movies_display_genre_name.append(i[0][0])

    # Filtra las películas por el campo "top". Mismo funcionamiento que la función para filtrar por el "to_watch"
    def filter_top(self):
        self.movies_display_name = []
        self.movies_display_genre_name = []
        self.name_filter_temp = []
        self.genreid_filter_temp = []
        self.genre_name_filter_temp = []
        
 
        self.user_id_filter = c.session.query(User.id).filter(
            User.username == self.working_user
        ).first()
        
        self.movie_id_filter_temp = c.session.query(Movie_User.movie_id).filter(
            Movie_User.user_id == self.user_id_filter[0]
        ).all()
        
        self.movie_id_filter_top = c.session.query(Movie_db.id).filter(
            Movie_db.top_button == 1
        ).all()
        
        self.movie_id_filter_def = set(self.movie_id_filter_temp).intersection(self.movie_id_filter_top)

        for id in self.movie_id_filter_def:
            self.name_filter_temp.append(c.session.query(Movie_db.name).filter(
                Movie_db.id == id[0]
            ))

        for i in self.movie_id_filter_def:
            self.genreid_filter_temp.append(c.session.query(Movie_db.genre_id).filter(
                Movie_db.id == i[0]
            ))

        for i in self.genreid_filter_temp:
            self.genre_name_filter_temp.append(c.session.query(Genre.name).filter(
                Genre.id == i[0][0]
            )) 

        for i in self.name_filter_temp:
            self.movies_display_name.append(i[0][0])

        for i in self.genre_name_filter_temp:
            self.movies_display_genre_name.append(i[0][0])

    # Filtra las películas por el campo "worst". Mismo funcionamiento que la función para filtrar por el "to_watch"
    def filter_worst(self):
        self.movies_display_name = []
        self.movies_display_genre_name = []
        self.name_filter_temp = []
        self.genreid_filter_temp = []
        self.genre_name_filter_temp = []
        
        self.user_id_filter = c.session.query(User.id).filter(
            User.username == self.working_user
        ).first()
        
        self.movie_id_filter_temp = c.session.query(Movie_User.movie_id).filter(
            Movie_User.user_id == self.user_id_filter[0]
        ).all()
        
        self.movie_id_filter_worst = c.session.query(Movie_db.id).filter(
            Movie_db.worst == 1
        ).all()
        
        self.movie_id_filter_def = set(self.movie_id_filter_temp).intersection(self.movie_id_filter_worst)

        for id in self.movie_id_filter_def:
            self.name_filter_temp.append(c.session.query(Movie_db.name).filter(
                Movie_db.id == id[0]
            ))

        for i in self.movie_id_filter_def:
            self.genreid_filter_temp.append(c.session.query(Movie_db.genre_id).filter(
                Movie_db.id == i[0]
            ))

        for i in self.genreid_filter_temp:
            self.genre_name_filter_temp.append(c.session.query(Genre.name).filter(
                Genre.id == i[0][0]
            )) 

        for i in self.name_filter_temp:
            self.movies_display_name.append(i[0][0])

        for i in self.genre_name_filter_temp:
            self.movies_display_genre_name.append(i[0][0])

    # Filtra por genero la busqueda
    def genre_filter(self, genre):
        self.get_genre_id = []
        self.genre_name_filter_temp = []
        self.name_filter_temp = []
        self.movies_display_genre_name = []
        self.movies_display_name = []
        self.genre_id_def = []

        # Obtiene el id del usuario en funcionamiento
        self.user_id_filter = c.session.query(User.id).filter(
            User.username == self.working_user
        ).first()

        # Obtiene todos los id de las películas del usuario en funcionamiento
        self.movie_id_filter_temp = c.session.query(Movie_User.movie_id).filter(
            Movie_User.user_id == self.user_id_filter[0]
        ).all()
        
        # Obtiene todos los id de género de las películas
        for id in self.movie_id_filter_temp:    
            self.get_genre_id.append(c.session.query(Movie_db.genre_id).filter(
                Movie_db.id == id[0]
            ))

        # Filtra los id de género a través del parámetro que se pasó
        for i in self.get_genre_id:
            if f'{i[0][0]}' == f'{genre}':
                self.genre_id_def.append(i[0][0])

        # Filtra todos los id de películas que tengan el mismo género
        if len(self.genre_id_def) != 0:
            self.movie_id_genre_filter = c.session.query(Movie_db.id).filter(
                Movie_db.genre_id == self.genre_id_def[0]
            ).all()
        else:
            self.movie_id_genre_filter = []
        
        # Encuentra los duplicados entre todas las películas del usuario y aquellas que corresponden al género
        self.movie_id_filter_def = set(self.movie_id_filter_temp).intersection(self.movie_id_genre_filter)

        # Cambia el id de género por el nombre del género
        for g in self.genre_id_def:
            self.genre_name_filter_temp.append(c.session.query(Genre.name).filter(
                Genre.id == g
            ))

        # Cambia el id de la película por el nombre de la película
        for id in self.movie_id_filter_def:
            self.name_filter_temp.append(c.session.query(Movie_db.name).filter(
                Movie_db.id == id[0]
            ))

        # Limpia la lista de nombres
        for i in self.name_filter_temp:
            self.movies_display_name.append(i[0][0])

        # Limpia la lista de los nombres de género
        for i in self.genre_name_filter_temp:
            self.movies_display_genre_name.append(i[0][0])
    
    # Filtra por el país que el usuario escribió
    def filter_country(self):
        self.genre_id_def = []
        self.genre_name_filter_temp = []
        self.name_filter_temp = []
        self.movies_display_genre_name = []
        self.movies_display_name = []

        # Obtiene el id del usuario en funcionamiento
        self.user_id_filter = c.session.query(User.id).filter(
            User.username == self.working_user
        ).first()

        # Obtiene todos los id de las películas del usuario en funcionamiento
        self.movie_id_filter_temp = c.session.query(Movie_User.movie_id).filter(
            Movie_User.user_id == self.user_id_filter[0]
        ).all()

        self.movie_id_country_filter = c.session.query(Movie_db.id).filter(
            Movie_db.country_id == self.country_text
        ).all()

        self.movie_id_def = set(self.movie_id_filter_temp).intersection(self.movie_id_country_filter)

        # Cambia el id de género por el nombre del género
        for i in self.movie_id_def:
            self.genre_id_def.append(c.session.query(Movie_db.genre_id).filter(
                Movie_db.id== i[0]
            ))

        for i in self.genre_id_def:
            self.genre_name_filter_temp.append(c.session.query(Genre.name).filter(
                Genre.id == i[0][0]
            ))

        # Cambia el id de la película por el nombre de la película
        for id in self.movie_id_def:
            self.name_filter_temp.append(c.session.query(Movie_db.name).filter(
                Movie_db.id == id[0]
            ))
        
        # Limpia la lista de nombres
        for i in self.name_filter_temp:
            self.movies_display_name.append(i[0][0])

        # Limpia la lista de los nombres de género
        for i in self.genre_name_filter_temp:
            self.movies_display_genre_name.append(i[0][0])

e = Execute()