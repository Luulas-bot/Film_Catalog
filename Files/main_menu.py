import pygame
import sys
from Files.Constants import WHITE, BLUE, GRAY

class Main_menu():

    # Función constructora
    def __init__(self, size):
        self.size = size
        self.init_stats()

    # Función que determina las variables iniciales
    def init_stats(self):
        self.screen = pygame.display.set_mode((self.size))

    # Función que registra los eventos
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    # Función que dibuja por pantalla los elementos
    def draw_on_screen(self):
        self.screen.fill(GRAY)
