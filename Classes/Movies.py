import pygame
from Constants.Constants import WHITE

pygame.init()

class Movies():

    movies_list_temp = []

    def __init__(self, image, rect_coords, blit_coords_name, blit_coords_genre, movie_name, genre_name):
        self.movie_name = movie_name
        self.genre_name = genre_name
        self.blit_coords_name = blit_coords_name
        self.blit_coords_name2 = (self.blit_coords_name[0], self.blit_coords_name[1] + 30)
        self.blit_coords_genre = blit_coords_genre
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = rect_coords
        self.movies_list_temp.append(self)
        self.adjust_name_size()

    def adjust_name_size(self):
        #self.slice_int = len(self.movie_name)/2
        if len(self.movie_name) > 20:
            self.movie_name1 = self.movie_name[:12]
            self.movie_name2 = self.movie_name[12:]
            self.adjust_font_size_large()
        else:
            self.adjust_font_size()

    def adjust_font_size(self):
        self.font_name = pygame.font.SysFont("consolas", 37 - len(self.movie_name))
        self.font_genre = pygame.font.SysFont("consolas", 40 - len(self.genre_name))
        self.name_blit = self.font_name.render(f"{self.movie_name}", True, WHITE)
        self.genre_blit = self.font_genre.render(f"{self.genre_name}", True, WHITE)

    def adjust_font_size_large(self):
        self.font_name1 = pygame.font.SysFont("consolas", 37 - len(self.movie_name1))
        self.font_name2 = pygame.font.SysFont("consolas", 37 - len(self.movie_name2))
        self.font_genre = pygame.font.SysFont("consolas", 40 - len(self.genre_name))
        self.name_blit1 = self.font_name1.render(f"{self.movie_name1}", True, WHITE)
        self.name_blit2 = self.font_name2.render(f"{self.movie_name2}", True, WHITE)
        self.genre_blit = self.font_genre.render(f"{self.genre_name}", True, WHITE)

pygame.quit()