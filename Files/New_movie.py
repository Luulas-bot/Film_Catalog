import pygame
import sys
from Files.Constants import (
    GRAY, WHITE, LIGHTGRAY, BLUE, LIGHTBLUE, color_user_textbox, movie_name, movie_date, movie_country, movie_description,
    color_movie_name_tx, color_movie_date_tx, color_movie_country_tx, color_movie_description_tx, tx_list, tick
)
# from Files.Add_new_Textboxes import Textbox

class AddMovie():
     
    def __init__(self, size):
         self.size = size
         self.init_stats()

    def init_stats(self):
        self.screen = pygame.display.set_mode(self.size)

        # Fuentes de texto
        self.font1 = pygame.font.SysFont("consolas", 20, bold = True)
        self.font2 = pygame.font.SysFont("consolas", 15, bold = True)
        self.name_title = self.font1.render("Nombre de la película", True, LIGHTBLUE)
        self.date_title = self.font1.render("Fecha", True, LIGHTBLUE)
        self.country_title = self.font1.render("Nacionalidad", True, LIGHTBLUE)
        self.description_title = self.font1.render("Descripción", True, LIGHTBLUE)

        # Variables que posteriormente serán alteradas para que oprten lo que el usuario escriba.
        self.name_text = ""
        self.date_text = ""
        self.country_text = ""
        self.description_text = ""

        self.ypos_description = 282
        self.description_count = 0

        self.escape = 0

        self.tick_rect = pygame.Rect(500, 500, 30, 30)

    def events(self):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                sys.exit()
            
            self.mx, self.my = pygame.mouse.get_pos()

            self.get_tx_state()
            self.write_user_text()
            self.tab_mechanics()
            self.esc_mechanics()
            self.enter_mechanics()
            self.get_tick()

    def draw_on_screen(self):
        self.screen.fill(GRAY)

        self.screen.blit(self.name_title, (50, 30))
        self.screen.blit(self.date_title, (50, 105))
        self.screen.blit(self.country_title, (50, 180))
        self.screen.blit(self.description_title, (50, 255))

        self.change_tx_color()

        text_surface1 = self.font2.render(self.name_text, True, BLUE)
        self.screen.blit(text_surface1, (55, 57))
        text_surface2 = self.font2.render(self.date_text, True, BLUE)
        self.screen.blit(text_surface2, (55, 132))
        text_surface3 = self.font2.render(self.country_text, True, BLUE)
        self.screen.blit(text_surface3, (55, 207))
        text_surface4 = self.font2.render(self.description_text, True, BLUE)
        self.screen.blit(text_surface4, (55, self.ypos_description))

        self.screen.blit(tick, (500, 500))

    def get_tx_state(self):
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            if movie_name.rect.collidepoint(self.mx, self.my):
                movie_name.state = True
            else:
                movie_name.state = False
            if movie_date.rect.collidepoint(self.mx, self.my):
                movie_date.state = True
            else:
                movie_date.state = False
            if movie_country.rect.collidepoint(self.mx, self.my):
                movie_country.state = True
            else:
                movie_country.state = False
            if movie_description.rect.collidepoint(self.mx, self.my):
                movie_description.state = True
            else:
                movie_description.state = False

    def change_tx_color(self):
        if movie_name.state == True:
            color_movie_name_tx = WHITE
        else:
            color_movie_name_tx = LIGHTGRAY
        if movie_date.state == True:
            color_movie_date_tx = WHITE
        else:
            color_movie_date_tx = LIGHTGRAY
        if movie_country.state == True:
            color_movie_country_tx = WHITE
        else:
            color_movie_country_tx = LIGHTGRAY
        if movie_description.state == True:
            color_movie_description_tx = WHITE
        else:
            color_movie_description_tx = LIGHTGRAY

        pygame.draw.rect(self.screen, color_movie_name_tx, movie_name, 0, 5)
        pygame.draw.rect(self.screen, color_movie_date_tx, movie_date, 0, 5)
        pygame.draw.rect(self.screen, color_movie_country_tx, movie_country, 0, 5)
        pygame.draw.rect(self.screen, color_movie_description_tx, movie_description, 0, 5)
    
    def write_user_text(self): 
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_BACKSPACE and movie_name.state:
                    self.name_text = self.name_text[:-1]
            elif movie_name.state and len(self.name_text) < 61:
                self.name_text += self.event.unicode
            if self.event.key == pygame.K_BACKSPACE and movie_date.state:
                self.date_text = self.date_text[:-1]
            elif movie_date.state and len(self.date_text) < 61:
                self.date_text += self.event.unicode
            if self.event.key == pygame.K_BACKSPACE and movie_country.state:
                self.country_text = self.country_text[:-1]
            elif movie_country.state and len(self.country_text) < 61:
                self.country_text += self.event.unicode
            if self.event.key == pygame.K_BACKSPACE and movie_description.state:
                self.description_text = self.description_text[:-1]
                self.description_count -= 1
            elif movie_description.state and self.description_count < 61:
                self.description_text += self.event.unicode
                self.description_count += 1

    # Mecánicas del taburador
    def tab_mechanics(self):
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_TAB:
                if movie_name.state:    
                    self.name_text = self.name_text[:-1]
                    movie_name.state = False
                    movie_date.state = True
                elif movie_date.state:
                    self.date_text = self.date_text[:-1]
                    movie_date.state = False
                    movie_country.state = True
                elif movie_country.state:
                    self.country_text = self.country_text[:-1]
                    movie_country.state = False
                    movie_description.state = True
                elif movie_description.state:
                    self.description_text = self.description_text[:-1]
                    movie_description.state = False
                    movie_name.state = True

    def esc_mechanics(self):
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_ESCAPE:
                self.escape += 1

    def enter_mechanics(self):
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_RETURN:
                if movie_description.state:
                    pass
    
    def get_tick(self):
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            if self.tick_rect.collidepoint(self.mx, self.my):
                pass

# TODO Terminar bien las mecanicas del tick
