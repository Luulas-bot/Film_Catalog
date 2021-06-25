from Constants.Constants import WHITE, LIGHTGRAY
import pygame

class Edit_Texts():

    texts_list_temp = []

    def __init__(self, blit_coords, text, tx_rect, tx_coords, text_coords):
        self.tx_rect = pygame.Rect(tx_rect)
        self.tx_coords = tx_coords
        self.blit_coords = blit_coords
        self.text = text
        self.state = False
        self.text_coords = text_coords
        self.texts_list_temp.append(self)

    def change_color(self):
        if self.state == True:
            self.color = WHITE
        else:
            self.color = LIGHTGRAY

class Edit_Description():

    description_list_temp = []

    def __init__(self, blit_coords, text, tx_rect, tx_coords):
        self.tx_rect = pygame.Rect(tx_rect)
        self.tx_coords = tx_coords
        self.blit_coords = blit_coords
        self.text = text
        self.state = False
        self.description_list_temp.append(self)