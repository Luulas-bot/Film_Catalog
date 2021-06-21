import pygame
from Constants.Constants import WHITE, LIGHTGRAY, BLUE, LIGHTBLUE

# Clase de los botones del edit
class Edit_Buttons():

    temp_list = []

    def __init__(self, rect, text, text_coords):
        self.rect = pygame.Rect(rect)
        self.font = pygame.font.SysFont("consolas", 15, bold = True)
        self.text = self.font.render(f"{text}", True, WHITE)
        self.text_coords = text_coords
        self.temp_list.append(self)
        self.state = False

    def change_color(self):
        if self.state:
            self.color = LIGHTBLUE
        else:
            self.color = BLUE