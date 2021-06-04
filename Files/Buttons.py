import pygame

pygame.init()

# Clase de los botones
class Buttons():

    # Función constructora
    def __init__(self, image, pressed_image, hitbox, coords):
        self.image = image
        self.pressed_image = pressed_image
        self.hitbox = hitbox
        self.coords = coords
        self.button = pygame.image.load(self.image)
        self.pressed_button = pygame.image.load(self.pressed_image)
        self.rect = pygame.Rect(self.hitbox)
        self.state = False

pygame.quit()