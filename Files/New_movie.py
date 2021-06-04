import pygame
import sys
from Files.Constants import (
    GRAY, WHITE, LIGHTGRAY, BLUE, LIGHTBLUE, color_user_textbox, movie_name, movie_date, movie_country, movie_description,
    tick, description_list, texts_list, all_text_list
)
# from Files.Add_new_Textboxes import Textbox

pygame.init()

class AddMovie():
     
    def __init__(self, size):
         self.size = size
         self.init_stats()

    # Función que define las variables inciales de la window
    def init_stats(self):
        
        pygame.display.quit()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("New Movie")

        # Fuentes de texto
        self.font1 = pygame.font.SysFont("consolas", 20, bold = True)
        self.font2 = pygame.font.SysFont("consolas", 15, bold = True)
        self.name_title = self.font1.render("Nombre de la película", True, LIGHTBLUE)
        self.date_title = self.font1.render("Fecha", True, LIGHTBLUE)
        self.country_title = self.font1.render("Nacionalidad", True, LIGHTBLUE)
        self.description_title = self.font1.render("Descripción", True, LIGHTBLUE)

        # Indice de las lines de las descripcion
        self.index = 0

        # Variable que maneja cuando se saca la screen actual 
        self.escape = 0

        # Hitbox del tick
        self.tick_rect = pygame.Rect(550, 550, 30, 30)

        self.font = pygame.font.SysFont("consolas", 15, bold = True)

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
        text_surface1 = self.font2.render(texts_list[0].text, True, BLUE)
        self.screen.blit(text_surface1, (55, 57))
        text_surface2 = self.font2.render(texts_list[1].text, True, BLUE)
        self.screen.blit(text_surface2, (55, 132))
        text_surface3 = self.font2.render(texts_list[2].text, True, BLUE)
        self.screen.blit(text_surface3, (55, 207))
        
        self.description_display()

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
                    texts_list[0].text = texts_list[0].text[:-1] 
            elif movie_name.state and len(texts_list[0].text) < 61:
                texts_list[0].text += self.event.unicode
            if self.event.key == pygame.K_BACKSPACE and movie_date.state:
                texts_list[1].text = texts_list[1].text[:-1]
            elif movie_date.state and len(texts_list[1].text) < 61:
                texts_list[1].text += self.event.unicode
            if self.event.key == pygame.K_BACKSPACE and movie_country.state:
                texts_list[2].text = texts_list[2].text[:-1]
            elif movie_country.state and len(texts_list[2].text) < 61:
                texts_list[2].text += self.event.unicode
            
            self.description_mechanics()

    # Mecánicas del taburador
    def tab_mechanics(self):
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_TAB:
                if movie_name.state:    
                    texts_list[0].text = texts_list[0].text[:-1]
                    movie_name.state = False
                    movie_date.state = True
                elif movie_date.state:
                    texts_list[1].text = texts_list[1].text[:-1]
                    movie_date.state = False
                    movie_country.state = True
                elif movie_country.state:
                    texts_list[2].text = texts_list[2].text[:-1]
                    movie_country.state = False
                    movie_description.state = True
                elif movie_description.state:
                    description_list[self.index].text = description_list[self.index].text[:-1]
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
                    self.index += 1
                
    
    # Mecánicas del tick
    def get_tick(self):
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            if self.tick_rect.collidepoint(self.mx, self.my):
                self.escape += 1
                # Acá también van todos los inserts a la base de datos

    # Muestra las líneas de la descripción por pantalla
    def description_display(self):
        for i in description_list:    
            self.surface = self.font.render(i.text, True, (47, 86, 233))
            self.screen.blit(self.surface, (i.blit_coords))

    # Funcionamiento de las líneas de la descripción
    def description_mechanics(self):
        if self.event.key == pygame.K_BACKSPACE and movie_description.state:
            description_list[self.index].text = description_list[self.index].text[:-1]
            if self.index < 16 and len(description_list[self.index].text) < 1:
                self.index -= 1
        elif movie_description.state and len(description_list[self.index].text) < 61:
            description_list[self.index].text += self.event.unicode
        elif len(description_list[self.index].text) > 59 and self.index < 16 and movie_description.state:
            self.index += 1
        print(f'{description_list[0].text} {description_list[1].text}')

pygame.quit()


# TODO = Limpiar todo el código. Esto significa agarrar y pasar todas las variables que cambien de valor con el tiempo de Constants
# a sus respectivos archivos. También si voy a definir variables y después meterlas en una lista, es mejor usar un diccionario directamente
# y definir las variables con sus atributos en el orden que quiero.
# Una vez hecho eso, fijarme que todo el código funcione bien y fijarme si se solucionó el error o no. Si no es el caso antes de renderizar
# el texto, poner una condición que impida la renderizacion del texto si este no tiene anchura.
# Por último, ya que voy a estar sacando todo de consatants y poniendolo en sus respectivos lugares, me puedo fijar si puede almacenar más 
# parte de las mécanicas dentro de las propias clases, por ejemplo, la clase de NM_Text.
# Suerte