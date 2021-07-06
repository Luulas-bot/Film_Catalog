from Database_models import Base, Connection, User, MovieUser, MovieDb, Genre, Country

# Creación de la clase que contiene lo scripts para manejar la base de datos
class DbManager():
    
    # Función constructora
    def __init__(self):
        self.cn = Connection()
        self.cn.run_engine()
        self.cn.create_session()
        Base.metadata.create_all(self.cn.engine)
        
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

        self.cn.session.add(self.user)

        self.cn.session.commit()
        
    # Lectura de los datos de un usuario en específico para el Login
    def select_login(self, username, password):
        self.username_sl = username
        self.password_sl = password
        self.user_sl = self.cn.session.query(User).filter(
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

        self.movie = MovieDb(name = f'{self.name_movie}', movie_date = f'{self.date_movie}', country_id = f'{self.country_movie}',
        genre_id = f'{self.genre_movie}', description = f'{self.description_movie}')
        
        self.cn.session.add(self.movie)
        self.cn.session.flush()
        self.cn.session.commit()

    # Función para insertar a la tabla 'Pelicula_Usuario' la película insertada recientemente y el usuario que la insertó
    def insert_Pelicula_Usuario(self):

        self.movie_id = self.cn.session.query(MovieDb.id).all()

        self.selected_user_id = self.cn.session.query(User.id).filter(
            User.username == self.working_user
        ).first()

        self.movie_user = MovieUser(movie_id = f'{self.movie_id[-1][0]}', user_id = f'{self.selected_user_id[0]}')
        
        self.cn.session.add(self.movie_user)
        self.cn.session.flush()
        self.cn.session.commit()

    # Función que a través de select, filtros e inner joins arma algunas listas con los nombres de las películas y sus géneros
    def select_movies_to_display(self):

        self.movies_display_name_temp = []
        self.movies_display_genreid_temp = []
        self.movies_display_genre_name_temp = []
        self.movies_display_name = []
        self.movies_display_genreid = []
        self.movies_display_genre_name = []

        # Toma el id del usuario en uso
        self.user_id_display = self.cn.session.query(User.id).filter(
            User.username == self.working_user
        ).first()

        # Filtra todas los id de las películas del usuario en uso
        self.movies_display_id = self.cn.session.query(MovieUser.movie_id).filter(
            MovieUser.user_id == self.user_id_display[0]
        )

        # Toma a partir de los id de las películas, sus nombres
        for i in self.movies_display_id:
            self.movies_display_name_temp.append(self.cn.session.query(MovieDb.name).filter(
                MovieDb.id == i[0]
            ))

        # Toma a partir de los id de las películas sus id de género
        for i in self.movies_display_id:
            self.movies_display_genreid_temp.append(self.cn.session.query(MovieDb.genre_id).filter(
                MovieDb.id == i[0]
            ))

        # Toma a partir de los id de género los nombres de esos géneros
        for i in self.movies_display_genreid_temp:
            self.movies_display_genre_name_temp.append(self.cn.session.query(Genre.name).filter(
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
        self.user_id_edit = self.cn.session.query(User.id).filter(
            User.username == self.working_user
        ).first()

        # Filtra todos los id de las películas de ese usuario
        self.movie_id_edit = self.cn.session.query(MovieUser.movie_id).filter(
            MovieUser.user_id == self.user_id_edit[0]
        ).all()

        # Toma el id en específico de la película que se seleccionó
        for id in self.movie_id_edit:
            self.movie_id_temp.append(self.cn.session.query(MovieDb.id).filter(
                MovieDb.name == self.movie_name_search
            ).filter(
                MovieDb.id == id[0]
            ).first())

        # Limpia la lista para quedarse solo con el id en específico
        for i in self.movie_id_temp:
            if i != None:
                self.movie_id_def = i[0]
            else:
                pass

        # Filtra todos los atributos que se quieren meter en variables a través del id
        self.movie_atr_edit_temp.append(self.cn.session.query(MovieDb.name, MovieDb.movie_date, MovieDb.country_id, MovieDb.genre_id, MovieDb.description, MovieDb.rating).filter(
            MovieDb.id == self.movie_id_def
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
        self.update_list = self.cn.session.query(MovieDb).filter(
            MovieDb.id == self.movie_id_def 
        )

        # Updatea las columnas de esa películas
        self.update_list[0].name = self.update_name
        self.update_list[0].movie_date = self.update_date
        self.update_list[0].country_id = self.update_countryid
        self.update_list[0].genre_id = self.update_genre_id
        self.update_list[0].description = self.update_description
        self.update_list[0].rating = self.update_rating

        self.cn.session.commit()

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
        self.cn.session.query(MovieUser).filter(
            MovieUser.movie_id == self.movie_id_def
        ).delete()
        
        # Borra la película de la tabla de las películas
        self.cn.session.query(MovieDb).filter(
            MovieDb.id == self.movie_id_def
        ).delete()

        self.cn.session.commit()

    # Asigna un uno si la pelicula está en modo "to_watch" a la db
    def assign_filter(self, filter_0, filter_1):
        self.assign_filt = self.cn.session.query(MovieDb).filter(
            MovieDb.id == self.movie_id_def
        ).update(
            {
                f'{filter_1}' : 1,
                f'{filter_0}' : 0
            }
        )

        self.cn.session.commit()
        self.cn.session.flush()

    # Filtra las películas con el filtro "to_watch"
    def filter_movie(self, param):
        self.movies_display_name = []
        self.movies_display_genre_name = []
        self.name_filter_temp = []
        self.genreid_filter_temp = []
        self.genre_name_filter_temp = []
        
        # Filtra el usuario que está en uso
        self.user_id_filter = self.cn.session.query(User.id).filter(
            User.username == self.working_user
        ).first()
        
        # Filtra todas las películas del usuario que está en uso
        self.movie_id_filter_temp = self.cn.session.query(MovieUser.movie_id).filter(
            MovieUser.user_id == self.user_id_filter[0]
        ).all()
        
        if param == 0:
            self.filter_to_watch()
        elif param == 1:
            self.filter_already_seen()
        elif param == 2:
            self.filter_top()
        elif param == 3:
            self.filter_worst()

        # Obtiene el nombre de la película a través del id
        for id in self.movie_id_filter_def:
            self.name_filter_temp.append(self.cn.session.query(MovieDb.name).filter(
                MovieDb.id == id[0]
            ))

        # Obtiene el id de género
        for i in self.movie_id_filter_def:
            self.genreid_filter_temp.append(self.cn.session.query(MovieDb.genre_id).filter(
                MovieDb.id == i[0]
            ))

        # Obtiene el nombre de género a través de su id
        for i in self.genreid_filter_temp:
            self.genre_name_filter_temp.append(self.cn.session.query(Genre.name).filter(
                Genre.id == i[0][0]
            )) 

        # Limpia la lista de los nombres de las películas
        for i in self.name_filter_temp:
            self.movies_display_name.append(i[0][0])

        # Limpia la lista de los nombres de género
        for i in self.genre_name_filter_temp:
            self.movies_display_genre_name.append(i[0][0])

    def filter_to_watch(self):
        self.movie_id_filter_to_watch = self.cn.session.query(MovieDb.id).filter(
            MovieDb.to_watch == 1
        ).all()

        self.movie_id_filter_def = set(self.movie_id_filter_temp).intersection(self.movie_id_filter_to_watch)

    def filter_already_seen(self):
        self.movie_id_filter_alreadyseen = self.cn.session.query(MovieDb.id).filter(
            MovieDb.already_seen == 1
        ).all()
        
        self.movie_id_filter_def = set(self.movie_id_filter_temp).intersection(self.movie_id_filter_alreadyseen)

    def filter_top(self):
        self.movie_id_filter_top = self.cn.session.query(MovieDb.id).filter(
            MovieDb.top_button == 1
        ).all()
        
        self.movie_id_filter_def = set(self.movie_id_filter_temp).intersection(self.movie_id_filter_top)

    def filter_worst(self):
        self.movie_id_filter_worst = self.cn.session.query(MovieDb.id).filter(
            MovieDb.worst == 1
        ).all()
        
        self.movie_id_filter_def = set(self.movie_id_filter_temp).intersection(self.movie_id_filter_worst)

    # Filtra por genero la busqueda
    def genre_filter(self, genre):
        
        self.get_genre_id = []
        self.genre_name_filter_temp = []
        self.name_filter_temp = []
        self.movies_display_genre_name = []
        self.movies_display_name = []
        self.genre_id_def = []

        # Obtiene el id del usuario en funcionamiento
        self.user_id_filter = self.cn.session.query(User.id).filter(
            User.username == self.working_user
        ).first()

        # Obtiene todos los id de las películas del usuario en funcionamiento
        self.movie_id_filter_temp = self.cn.session.query(MovieUser.movie_id).filter(
            MovieUser.user_id == self.user_id_filter[0]
        ).all()
        
        # Obtiene todos los id de género de las películas
        for id in self.movie_id_filter_temp:    
            self.get_genre_id.append(self.cn.session.query(MovieDb.genre_id).filter(
                MovieDb.id == id[0]
            ))

        # Filtra los id de género a través del parámetro que se pasó
        for i in self.get_genre_id:
            if f'{i[0][0]}' == f'{genre}':
                self.genre_id_def.append(i[0][0])

        # Filtra todos los id de películas que tengan el mismo género
        if len(self.genre_id_def) != 0:
            self.movie_id_genre_filter = self.cn.session.query(MovieDb.id).filter(
                MovieDb.genre_id == self.genre_id_def[0]
            ).all()
        else:
            self.movie_id_genre_filter = []
        
        # Encuentra los duplicados entre todas las películas del usuario y aquellas que corresponden al género
        self.movie_id_filter_def = set(self.movie_id_filter_temp).intersection(self.movie_id_genre_filter)

        # Cambia el id de género por el nombre del género
        for g in self.genre_id_def:
            self.genre_name_filter_temp.append(self.cn.session.query(Genre.name).filter(
                Genre.id == g
            ))

        # Cambia el id de la película por el nombre de la película
        for id in self.movie_id_filter_def:
            self.name_filter_temp.append(self.cn.session.query(MovieDb.name).filter(
                MovieDb.id == id[0]
            ))

        # Limpia la lista de nombres
        for i in self.name_filter_temp:
            self.movies_display_name.append(i[0][0])

        # Limpia la lista de los nombres de género
        for i in self.genre_name_filter_temp:
            self.movies_display_genre_name.append(i[0][0])
        
    def filter_country(self):
        self.genre_id_def = []
        self.genre_name_filter_temp = []
        self.name_filter_temp = []
        self.movies_display_genre_name = []
        self.movies_display_name = []

        # Obtiene el id del usuario en funcionamiento
        self.user_id_filter = self.cn.session.query(User.id).filter(
            User.username == self.working_user
        ).first()

        # Obtiene todos los id de las películas del usuario en funcionamiento
        self.movie_id_filter_temp = self.cn.session.query(MovieUser.movie_id).filter(
            MovieUser.user_id == self.user_id_filter[0]
        ).all()

        self.movie_id_country_filter = self.cn.session.query(MovieDb.id).filter(
            MovieDb.country_id == self.country_text
        ).all()

        self.movie_id_def = set(self.movie_id_filter_temp).intersection(self.movie_id_country_filter)

        # Cambia el id de género por el nombre del género
        for i in self.movie_id_def:
            self.genre_id_def.append(self.cn.session.query(MovieDb.genre_id).filter(
                MovieDb.id== i[0]
            ))

        for i in self.genre_id_def:
            self.genre_name_filter_temp.append(self.cn.session.query(Genre.name).filter(
                Genre.id == i[0][0]
            ))

        # Cambia el id de la película por el nombre de la película
        for id in self.movie_id_def:
            self.name_filter_temp.append(self.cn.session.query(MovieDb.name).filter(
                MovieDb.id == id[0]
            ))
        
        # Limpia la lista de nombres
        for i in self.name_filter_temp:
            self.movies_display_name.append(i[0][0])

        # Limpia la lista de los nombres de género
        for i in self.genre_name_filter_temp:
            self.movies_display_genre_name.append(i[0][0])

