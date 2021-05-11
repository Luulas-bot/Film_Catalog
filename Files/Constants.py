import pygame

pygame.init()

size_login = (500, 500)
WHITE = (255, 255, 255)
BLUE = (47, 86, 233)
GREY = (119, 136, 153)
LIGHTGREY = (211, 211, 211)
color_user_textbox = LIGHTGREY
color_pass_textbox = LIGHTGREY
clock = pygame.time.Clock()
pygame.display.set_caption("Login")
fps = 60