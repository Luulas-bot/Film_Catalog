import pygame

pygame.init()

# Sizes
size_login = (500, 500)
size_sign_up = (700, 700)

# Colors
WHITE = (255, 255, 255)
BLUE = (47, 86, 233)
GRAY = (119, 136, 153)
LIGHTGRAY = (211, 211, 211)
color_user_textbox = LIGHTGRAY
color_pass_textbox = LIGHTGRAY
color_re_pass_textbox = LIGHTGRAY

# Pygmae variables
clock = pygame.time.Clock()
pygame.display.set_caption("Login")
fps = 60