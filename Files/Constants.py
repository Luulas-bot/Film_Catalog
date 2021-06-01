import pygame
from Files.Buttons import Buttons
from Files.Movies import Movies
from Files.Add_new_Textboxes import Textbox

pygame.init()

# Sizes
size_login = (500, 500)
size_sign_up = (500, 500)
size_main_menu = (1100, 800)
size_add_new = (600, 600)

# Colors
WHITE = (255, 255, 255)
BLUE = (47, 86, 233)
LIGHTBLUE = (131, 181, 255)
GRAY = (61, 61, 61)
LIGHTGRAY = (181, 181, 181)
color_user_textbox = LIGHTGRAY
color_pass_textbox = LIGHTGRAY
color_re_pass_textbox = LIGHTGRAY
color_movie_name_tx = LIGHTGRAY
color_movie_date_tx = LIGHTGRAY
color_movie_country_tx = LIGHTGRAY
color_movie_description_tx = LIGHTGRAY

# Pygmae variables
clock = pygame.time.Clock()
pygame.display.set_caption("Login")
fps = 60

# Lista de los botones
button_list = []
genre_button_list = []

# Botones principales
all_button = Buttons("Images/all_button.png", "Images/all_pressed_button.png", (0, 0, 200, 100), (0, 0))
button_list.append(all_button)
genre_button = Buttons("Images/genre_button.png", "Images/genre_pressed_button.png", (0, 100, 200, 100), (0, 100))
button_list.append(genre_button)
to_watch_button = Buttons("Images/to_watch_button.png", "Images/to_watch_pressed_button.png", (0, 200, 200, 100), (0, 200))
button_list.append(to_watch_button)
already_seen_button = Buttons("Images/already_seen_button.png", "Images/already_seen_pressed_button.png", (0, 300, 200, 100), (0, 300))
button_list.append(already_seen_button)
top_button = Buttons("Images/top_button.png", "Images/top_pressed_button.png", (0, 400, 200, 100), (0, 400))
button_list.append(top_button)
worst_button = Buttons("Images/worst_button.png", "Images/worst_pressed_button.png", (0, 500, 200, 100), (0, 500))
button_list.append(worst_button)
country_button = Buttons("Images/country_button.png", "Images/country_pressed_button.png", (0, 600, 200, 100), (0, 600))
button_list.append(country_button)
exit_button = Buttons("Images/exit_button.png", "Images/exit_pressed_button.png", (0, 700, 200, 100), (0, 700))
button_list.append(exit_button)
add_button = Buttons("Images/add_new_button.png", "Images/add_new_pressed_button.png", (900, 0, 200, 100), (900, 0))
button_list.append(add_button)

# Botones de los géneros
action_button = Buttons("Images/action_button.png", "Images/action_pressed_button.png", (200, 70, 120, 60), (200, 70))
genre_button_list.append(action_button)
science_fiction_button = Buttons("Images/science_fiction.png", "Images/science_fiction_pressed_button.png", (200, 130, 120, 60), (200, 130))
genre_button_list.append(science_fiction_button)
comedy_button = Buttons("Images/comedy_button.png", "Images/comedy_pressed_button.png", (200, 190, 120, 60), (200, 190))
genre_button_list.append(comedy_button)
drama_button = Buttons("Images/drama_button.png", "Images/drama_pressed_button.png", (200, 250, 120, 60), (200, 250))
genre_button_list.append(drama_button)
fantasy_button = Buttons("Images/fantasy_button.png", "Images/fantasy_pressed_button.png", (200, 310, 120, 60), (200, 310))
genre_button_list.append(fantasy_button)
melodrama_button = Buttons("Images/melodrama_button.png", "Images/melodrama_pressed_button.png", (200, 370, 120, 60), (200, 370))
genre_button_list.append(melodrama_button)
musical_button = Buttons("Images/musical_button.png", "Images/musical_pressed_button.png", (200, 430, 120, 60), (200, 430))
genre_button_list.append(musical_button)
romance_button = Buttons("Images/romance_button.png", "Images/romance_pressed_button.png", (200, 490, 120, 60), (200, 490))
genre_button_list.append(romance_button)
suspense_button = Buttons("Images/suspense_button.png", "Images/suspense_pressed_button.png", (200, 550, 120, 60), (200, 550))
genre_button_list.append(suspense_button)
terror_button = Buttons("Images/terror_button.png", "Images/terror_pressed_button.png", (200, 610, 120, 60), (200, 610))
genre_button_list.append(terror_button)
documentary_button = Buttons("Images/documentary_button.png", "Images/documentary_pressed_button.png", (200, 670, 120, 60), (200, 670))
genre_button_list.append(documentary_button)

# Rectángulo de las peliculas -------- OPTIMIZAR ESTO, SOLO DE PRUEBA----------------------------
all_sprites_list = pygame.sprite.Group()
movie = Movies("Images/movies_rect.png", (290, 120))
movie2 = Movies("Images/movies_rect.png", (540, 120))
movie3 = Movies("Images/movies_rect.png", (800, 120))
movie4 = Movies("Images/movies_rect.png", (290, 450))
movie5 = Movies("Images/movies_rect.png", (540, 450))
movie6 = Movies("Images/movies_rect.png", (800, 450))
all_sprites_list.add(movie)
all_sprites_list.add(movie2)
all_sprites_list.add(movie3)
all_sprites_list.add(movie4)
all_sprites_list.add(movie5)
all_sprites_list.add(movie6)

# Textboxes del agregadode películas
tx_list = []

movie_name = Textbox((50, 50, 500, 30), (50, 50))
tx_list.append(movie_name)
movie_date = Textbox((50, 125, 500, 30), (50, 100))
tx_list.append(movie_date)
movie_country = Textbox((50, 200, 500, 30), (50, 150))
tx_list.append(movie_country)
movie_description = Textbox((50, 275, 500, 275), (50, 200))
tx_list.append(movie_description)

tick = pygame.image.load("Images/tick.png")