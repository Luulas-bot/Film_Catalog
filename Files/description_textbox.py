import pygame

class Description():

    def __init__(self, blit_coords, text):
        self.blit_coords = blit_coords
        self.text = text
        self.font = pygame.font.SysFont("consolas", 15, bold = True)
        self.state = False
        
    def update_surface(self):
        self.surface = self.font.render(self.text, True, (47, 86, 233))
        