import pygame

pygame.init()

class Movies(pygame.sprite.Sprite):

    movies_list_temp = []

    def __init__(self, image, coords):
        super().__init__()
        self.coords= coords
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coords
        self.movies_list_temp.append(self)

pygame.quit()