import pygame
import sys
from Files.Constants import (
    GRAY, WHITE, LIGHTGRAY, BLUE, LIGHTBLUE, color_user_textbox, movie_name, movie_date, movie_country, movie_description,
    color_movie_name_tx, color_movie_date_tx, color_movie_country_tx, color_movie_description_tx, tx_list, tick, 
    description_text
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
        #self.description_text = ""
        self.description_text2 = ""
        self.description_text3 = ""

        # Variable que maneja cuando se saca la screen actual 
        self.escape = 0

        # Hitbox del tick
        self.tick_rect = pygame.Rect(550, 550, 30, 30)

    # Función que registra los eventos
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

    # Función que dibuja por pantalla todo
    def draw_on_screen(self):
        self.screen.fill(GRAY)
        
        # Muestra por pantalla los título
        self.screen.blit(self.name_title, (50, 30))
        self.screen.blit(self.date_title, (50, 105))
        self.screen.blit(self.country_title, (50, 180))
        self.screen.blit(self.description_title, (50, 255))

        self.change_tx_color()

        # Dibuja por pantalla los inputs de texto del usuario
        text_surface1 = self.font2.render(self.name_text, True, BLUE)
        self.screen.blit(text_surface1, (55, 57))
        text_surface2 = self.font2.render(self.date_text, True, BLUE)
        self.screen.blit(text_surface2, (55, 132))
        text_surface3 = self.font2.render(self.country_text, True, BLUE)
        self.screen.blit(text_surface3, (55, 207))
        self.screen.blit(description_text.surface, (description_text.blit_coords))
        text_surface5 = self.font2.render(self.description_text2, True, BLUE)
        self.screen.blit(text_surface5, (55, 300))
        text_surface6 = self.font2.render(self.description_text3, True, BLUE)
        self.screen.blit(text_surface6, (55, 317))

        # Dibuja por pantalla el tick
        self.screen.blit(tick, (550, 550))

    # Define si están activas o no las textboxes
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

    # Variable que cambia el color de las textboxes según su estado
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

        # Dibuja las textboxes con su color por pantalla
        pygame.draw.rect(self.screen, color_movie_name_tx, movie_name, 0, 5)
        pygame.draw.rect(self.screen, color_movie_date_tx, movie_date, 0, 5)
        pygame.draw.rect(self.screen, color_movie_country_tx, movie_country, 0, 5)
        pygame.draw.rect(self.screen, color_movie_description_tx, movie_description, 0, 5)
    
    # Escribe en las variables lo que el usuario escribe
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
            if self.event.key == pygame.K_BACKSPACE and movie_description.state and len(description_text.text) < 61:
                description_text.text = description_text.text[:-1]
            elif self.event.key == pygame.K_BACKSPACE and movie_description.state and len(description_text.text) > 60:
                self.description_text2 = self.description_text2[:-1]
            elif self.event.key == pygame.K_BACKSPACE and movie_description.state and len(self.description_text2) > 60:
                self.description_text3 = self.description_text3[:-1]
            elif movie_description.state and len(description_text.text) < 61:
                description_text.text += self.event.unicode
            elif movie_description.state and len(description_text.text) > 60 and len(self.description_text2) < 61:
                self.description_text2 += self.event.unicode
            elif movie_description.state and len(self.description_text2) > 60 and len(self.description_text3) < 61:
                self.description_text3 += self.event.unicode
            print(description_text.text)

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

    # Mecánicas del escape
    def esc_mechanics(self):
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_ESCAPE:
                self.escape += 1

    # Mecánicas del enter
    def enter_mechanics(self):
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_RETURN:
                if movie_description.state:
                    self.description_text += "\n"
    
    # Mecánicas del tick
    def get_tick(self):
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            if self.tick_rect.collidepoint(self.mx, self.my):
                self.escape += 1
                # Acá también van todos los inserts a la base de datos

# TODO Terminar de pasar todos los reglones de la descripcion a la clase. Además hay que acrodarse que lo que no funciona el el display
# del texto, eso significa que el texto está bien en la variable, pero no se muestra por pantalla, quizás algún error
# en el blit o algo. También hacer todas las mecánicas utilizando los estados de cada reglon y por último, hacer que cuando,
# se apriete backspace y no haya más letras en el reglon, vuelva un reglón para atrás. Suerte.
