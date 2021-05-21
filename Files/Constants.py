import pygame

pygame.init()

# Sizes
size_login = (500, 500)
size_sign_up = (500, 500)
size_main_menu = (1100, 800)

# Colors
WHITE = (255, 255, 255)
BLUE = (47, 86, 233)
LIGHTBLUE = (131, 181, 255)
GRAY = (61, 61, 61)
LIGHTGRAY = (181, 181, 181)
color_user_textbox = LIGHTGRAY
color_pass_textbox = LIGHTGRAY
color_re_pass_textbox = LIGHTGRAY

# Pygmae variables
clock = pygame.time.Clock()
pygame.display.set_caption("Login")
fps = 60

# Imágenes
# Imágenes de los botones
all_button = pygame.image.load("Images/all_button.png")
genre_button = pygame.image.load("Images/genre_button.png")
to_watch_button = pygame.image.load("Images/to_watch_button.png")
already_seen_button = pygame.image.load("Images/already_seen_button.png")
top_button = pygame.image.load("Images/top_button.png")
worst_button = pygame.image.load("Images/worst_button.png")
country_button = pygame.image.load("Images/country_button.png")
exit_button = pygame.image.load("Images/exit_button.png")

# Generos
action_button = pygame.image.load("Images/action_button.png")
science_fiction_button = pygame.image.load("Images/science_fiction.png")
comedy_button = pygame.image.load("Images/comedy_button.png")
drama_button = pygame.image.load("Images/drama_button.png")
fantasy_button = pygame.image.load("Images/fantasy_button.png")
melodrama_button = pygame.image.load("Images/melodrama_button.png")
musical_button = pygame.image.load("Images/musical_button.png")
romance_button = pygame.image.load("Images/romance_button.png")
suspense_button = pygame.image.load("Images/suspense_button.png")
terror_button = pygame.image.load("Images/terror_button.png")
documentary_button = pygame.image.load("Images/documentary_button.png")

# Imágenes de los botones presionados
all_button_pressed = pygame.image.load("Images/all_pressed_button.png")
genre_button_pressed = pygame.image.load("Images/genre_pressed_button.png")
to_watch_button_pressed = pygame.image.load("Images/to_watch_pressed_button.png")
already_seen_button_pressed = pygame.image.load("Images/already_seen_pressed_button.png")
top_button_pressed = pygame.image.load("Images/top_pressed_button.png")
worst_button_pressed = pygame.image.load("Images/worst_pressed_button.png")
country_button_pressed = pygame.image.load("Images/country_pressed_button.png")
exit_button_pressed = pygame.image.load("Images/exit_pressed_button.png")

# Botónes de los géneros presionados
action_pressed_button = pygame.image.load("Images/action_pressed_button.png")
science_fiction_pressed_button = pygame.image.load("Images/science_fiction_pressed_button.png")
comedy_pressed_button = pygame.image.load("Images/comedy_pressed_button.png")
drama_pressed_button = pygame.image.load("Images/drama_pressed_button.png")
fantasy_pressed_button = pygame.image.load("Images/fantasy_pressed_button.png")
melodrama_pressed_button = pygame.image.load("Images/melodrama_pressed_button.png")
musical_pressed_button = pygame.image.load("Images/musical_pressed_button.png")
romance_pressed_button = pygame.image.load("Images/romance_pressed_button.png")
suspense_pressed_button = pygame.image.load("Images/suspense_pressed_button.png")
terror_pressed_button = pygame.image.load("Images/terror_pressed_button.png")
documentary_pressed_button = pygame.image.load("Images/documentary_pressed_button.png")