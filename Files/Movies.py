import pygame
from Files.Constants import WHITE

pygame.init()

class Movies(pygame.sprite.Sprite):

    movies_list_temp = []

    def __init__(self, image, rect_coords, movie_name, genre_name, blit_coords_name, blit_coords_genre):
        super().__init__()
        self.movie_name = movie_name
        self.genre_name = genre_name
        self.blit_coords_name = blit_coords_name
        self.blit_coords_genre = blit_coords_genre
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = rect_coords
        self.movies_list_temp.append(self)
        self.adjust_font_size()

    def adjust_font_size(self):
        self.font_name = pygame.font.SysFont("consolas", 37 - len(self.movie_name))
        self.font_genre = pygame.font.SysFont("consolas", 40 - len(self.genre_name))
        self.name_blit = self.font_name.render(f"{self.movie_name}", True, WHITE)
        self.genre_blit = self.font_genre.render(f"{self.genre_name}", True, WHITE)

pygame.quit()