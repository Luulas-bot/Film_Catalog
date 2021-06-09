import pygame
from Files.Movies import Movies

pygame.init()

# Sizes
size_login = (500, 500)
size_sign_up = (500, 500)
size_main_menu = (1100, 800)
size_add_new = (600, 700)

# Colors
WHITE = (255, 255, 255)
BLUE = (47, 86, 233)
LIGHTBLUE = (131, 181, 255)
GRAY = (61, 61, 61)
LIGHTGRAY = (181, 181, 181)
GOLD = (255, 215, 0)

# Pygmae variables
clock = pygame.time.Clock()
fps = 60


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

pygame.quit()