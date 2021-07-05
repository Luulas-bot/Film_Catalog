import pygame
from Constants.constants import WHITE, LIGHTGRAY

class NmText():

    texts_list_temp = []

    def __init__(self, blit_coords, text, tx_rect, tx_coords, text_coords):
        self.tx_rect = pygame.Rect(tx_rect)
        self.tx_coords = tx_coords
        self.blit_coords = blit_coords
        self.text_coords = text_coords
        self.text = text
        self.state = False
        self.texts_list_temp.append(self)

    def change_color(self):
        if self.state == True:
            self.color = WHITE
        else:
            self.color = LIGHTGRAY

class NmDescription():

    description_list_temp = []

    def __init__(self, blit_coords, text, tx_rect, tx_coords):
        self.tx_rect = pygame.Rect(tx_rect)
        self.tx_coords = tx_coords
        self.blit_coords = blit_coords
        self.text = text
        self.state = False
        self.description_list_temp.append(self)
        