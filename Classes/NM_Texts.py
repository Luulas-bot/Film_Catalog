import pygame

class NM_Text():

    texts_list_temp = []

    def __init__(self, blit_coords, text, tx_rect, tx_coords):
        self.tx_rect = pygame.Rect(tx_rect)
        self.tx_coords = tx_coords
        self.blit_coords = blit_coords
        self.text = text
        self.state = False
        self.texts_list_temp.append(self)

class NM_Description():

    description_list_temp = []

    def __init__(self, blit_coords, text, tx_rect, tx_coords):
        self.tx_rect = pygame.Rect(tx_rect)
        self.tx_coords = tx_coords
        self.blit_coords = blit_coords
        self.text = text
        self.state = False
        self.description_list_temp.append(self)
        