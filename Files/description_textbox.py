import pygame

class Description():

    def __init__(self, blit_coords, text):
        self.font = pygame.font.SysFont("consolas", 15, bold = True)
        self.blit_coords = blit_coords
        self.text = text
        self.states = list(range(0, 13))
        self.surface = self.font.render(self.text, True, (47, 86, 233))
        
