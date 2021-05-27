import pygame
import sys
from Files.Constants import (
    GRAY, color_user_textbox, movie_name
)
from Files.Add_new_Textboxes import Textbox

class AddMovie():
     
    def __init__(self, size):
         self.size = size
         self.init_stats()

    def init_stats(self):
        self.screen = pygame.display.set_mode(self.size)

        # Variables que posteriormente serán alteradas para que oprten lo que el usuario escriba.
        self.movie_name = ""
        self.movie_date = ""
        self.movie_country = ""
        self.movie_descrpition = ""

    def events(self):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                sys.exit()

    def draw_on_screen(self):
        self.screen.fill(GRAY)

        pygame.draw.rect(self.screen, color_user_textbox, movie_name, 0, 5)