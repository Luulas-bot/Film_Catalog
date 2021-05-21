import pygame

class Buttons():

    def __init__(self, image, pressed_image, hitbox, coords):
        self.image = image
        self.pressed_image = pressed_image
        self.hitbox = hitbox
        self.coords = coords
        self.button = pygame.image.load(self.image)
        self.pressed_button = pygame.image.load(self.pressed_image)
        self.rect = pygame.Rect()
        self.state_bool()

    def state_bool(self):
        self.state = False

    def draw_normal(self):
        m.screen.blit(self.button, self.coords)

# TODO Todos los boleanos, rectangulos y condiciones de los botones por una clase de botones que funcione