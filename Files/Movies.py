import pygame

class Movies(pygame.sprite.Sprite):

    def __init__(self, image, coords):
        super().__init__()
        self.coords= coords
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coords
        