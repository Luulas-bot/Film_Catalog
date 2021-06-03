import pygame

class Textbox():

    def __init__(self, rect, coords):
        
        self.rect = pygame.Rect(rect)
        self.coords = coords
        self.state = False

pygame.quit()
        