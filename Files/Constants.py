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
