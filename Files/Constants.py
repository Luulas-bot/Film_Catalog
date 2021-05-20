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

# Imágenes de los botones presionados
all_button_pressed = pygame.image.load("Images/all_pressed_button.png")
genre_button_pressed = pygame.image.load("Images/genre_pressed_button.png")
to_watch_button_pressed = pygame.image.load("Images/to_watch_pressed_button.png")
already_seen_button_pressed = pygame.image.load("Images/already_seen_pressed_button.png")
top_button_pressed = pygame.image.load("Images/top_pressed_button.png")
worst_button_pressed = pygame.image.load("Images/worst_pressed_button.png")
country_button_pressed = pygame.image.load("Images/country_pressed_button.png")
exit_button_pressed = pygame.image.load("Images/exit_pressed_button.png")