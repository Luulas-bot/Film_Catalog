import pygame
import sys
from Files.Constants import (
    GRAY, WHITE, LIGHTGRAY, BLUE, LIGHTBLUE, GOLD
)
from Files.NM_Texts import NM_Text, NM_Description
from Files.Database_Connection import c, e
from sqlalchemy.exc import IntegrityError

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
        self.font3= pygame.font.SysFont("consolas", 13, bold = True)
        self.name_title = self.font1.render("Nombre de la película", True, LIGHTBLUE)
        self.date_title = self.font1.render("Fecha", True, LIGHTBLUE)
        self.country_title = self.font1.render("Nacionalidad", True, LIGHTBLUE)
        self.description_title = self.font1.render("Descripción", True, LIGHTBLUE)
        self.genre_title = self.font1.render("Género", True, LIGHTBLUE)
        self.country_description1 = self.font3.render("Para los países: buscar en google 'código países 3 letras' e", True, LIGHTBLUE)
        self.country_description2 = self.font3.render("introducirlo en la casilla correspondiente. Todo en mayúsculas.", True, LIGHTBLUE)
        self.genre_description1 = self.font3.render("Para los géneros las opciones disponibles son: ACC(Acción) - DRA(Drama)", True, LIGHTBLUE)
        self.genre_description2 = self.font3.render("COM(Comedia) - DOC(Documental) - CFT(Ciencia Ficción) - FAN(Fantasía)", True, LIGHTBLUE)
        self.genre_description3 = self.font3.render("MEL(Melodrama) - MUS(Musical) - ROM(Romance) - SUS(Suspenso) - TER(Terror)", True, LIGHTBLUE)
        self.error_c_g = self.font2.render("Error! La abreviación del país o del género es incorrecta.", True, GOLD)
        self.error_name = self.font2.render("Error! La película debe tener un nombre.", True, GOLD)

        # Indice de las lines de las descripcion
        self.index = 0

        # Variable que maneja cuando se saca la screen actual 
        self.escape = 0

        # Variable que define si hay o no error
        self.error_c_g_state = False
        self.error_name_state = False

        # Tick
        self.tick_rect = pygame.Rect(550, 550, 30, 30)
        self.tick = pygame.image.load("Images/tick.png")

        # Color de las tx
        self.color_movie_name_tx = LIGHTGRAY
        self.color_movie_date_tx = LIGHTGRAY
        self.color_movie_country_tx = LIGHTGRAY
        self.color_movie_genre_tx = LIGHTGRAY
        self.color_movie_description_tx = LIGHTGRAY

        # NM_Text texts   
        self.name_text = NM_Text((55, 57), "", (50, 50, 500, 30), (50, 50))
        self.date_text = NM_Text((55, 132), "", (50, 125, 500, 30), (50, 100))
        self.country_text = NM_Text ((55, 207), "", (50, 200, 200, 30), (50, 150))
        self.genre_text = NM_Text((305, 207),"", (300, 200, 200, 30), (200, 150))
        self.description_text = NM_Description((55, 282), "", (50, 275, 500, 275), (50, 200))
        self.description_text2 = NM_Description((55, 300), "", (50, 275, 500, 275), (50, 200))
        self.description_text3 = NM_Description((55, 318), "", (50, 275, 500, 275), (50, 200))
        self.description_text4 = NM_Description((55, 336), "", (50, 275, 500, 275), (50, 200))
        self.description_text5 = NM_Description((55, 354), "", (50, 275, 500, 275), (50, 200))
        self.description_text6 = NM_Description((55, 372), "", (50, 275, 500, 275), (50, 200))
        self.description_text7 = NM_Description((55, 390), "", (50, 275, 500, 275), (50, 200))
        self.description_text8 = NM_Description((55, 408), "", (50, 275, 500, 275), (50, 200))
        self.description_text9 = NM_Description((55, 426), "", (50, 275, 500, 275), (50, 200))
        self.description_text10 = NM_Description((55, 444), "", (50, 275, 500, 275), (50, 200))
        self.description_text11 = NM_Description((55, 462), "", (50, 275, 500, 275), (50, 200))
        self.description_text12 = NM_Description((55, 480), "", (50, 275, 500, 275), (50, 200))
        self.description_text13 = NM_Description((55, 498), "", (50, 275, 500, 275), (50, 200))
        self.description_text14 = NM_Description((55, 516), "", (50, 275, 500, 275), (50, 200))
        self.description_text15 = NM_Description((55, 534), "", (50, 275, 500, 275), (50, 200))
    
        # Listas que contienen parcialmente o totalmente los textos y textboxes definidos arrriba
        self.description_list = []
        self.texts_list = []

        for i in NM_Description.description_list_temp:
            self.description_list.append(i)

        for i in NM_Text.texts_list_temp:
            self.texts_list.append(i)

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
        self.screen.blit(self.genre_title, (300, 180))
        self.screen.blit(self.description_title, (50, 255))
        self.screen.blit(self.country_description1, (50, 580))
        self.screen.blit(self.country_description2, (50, 600))
        self.screen.blit(self.genre_description1, (50, 630))
        self.screen.blit(self.genre_description2, (50, 650))
        self.screen.blit(self.genre_description3, (50, 670))

        self.change_tx_color()

        # Dibuja por pantalla los inputs de texto del usuario
        self.text_surface1 = self.font2.render(self.texts_list[0].text, True, BLUE)
        self.screen.blit(self.text_surface1, (55, 57))
        self.text_surface2 = self.font2.render(self.texts_list[1].text, True, BLUE)
        self.screen.blit(self.text_surface2, (55, 132))   
        self.text_surface3 = self.font2.render(self.texts_list[2].text, True, BLUE)
        self.screen.blit(self.text_surface3, (55, 207))
        self.text_surface4 = self.font2.render(self.texts_list[3].text, True, BLUE)
        self.screen.blit(self.text_surface4, (305, 207))
        
        self.description_display()

        if self.error_c_g_state == True:
            self.screen.blit(self.error_c_g, (50, 557))
        elif self.error_name_state == True:
            self.screen.blit(self.error_name, (50, 557))

        # Dibuja por pantalla el tick
        self.screen.blit(self.tick, (550, 550))

    # Define si están activas o no las textboxes
    def get_tx_state(self):
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            if self.name_text.tx_rect.collidepoint(self.mx, self.my):
                self.name_text.state = True
            else:
                self.name_text.state = False
            if self.date_text.tx_rect.collidepoint(self.mx, self.my):
                self.date_text.state = True
            else:
                self.date_text.state = False
            if self.country_text.tx_rect.collidepoint(self.mx, self.my):
                self.country_text.state = True
            else:
                self.country_text.state = False
            if self.genre_text.tx_rect.collidepoint(self.mx, self.my):
                self.genre_text.state = True
            else:
                self.genre_text.state = False
            if self.description_text.tx_rect.collidepoint(self.mx, self.my):
                self.description_text.state = True
            else:
                self.description_text.state = False

    # Variable que cambia el color de las textboxes según su estado
    def change_tx_color(self):
        if self.name_text.state == True:
            self.color_movie_name_tx = WHITE
        else:
            self.color_movie_name_tx = LIGHTGRAY
        if self.date_text.state == True:
            self.color_movie_date_tx = WHITE
        else:
            self.color_movie_date_tx = LIGHTGRAY
        if self.country_text.state == True:
            self.color_movie_country_tx = WHITE
        else:
            self.color_movie_country_tx = LIGHTGRAY
        if self.genre_text.state:
            self.color_movie_genre_tx = WHITE
        else:
            self.color_movie_genre_tx = LIGHTGRAY
        if self.description_text.state == True:
            self.color_movie_description_tx = WHITE
        else:
            self.color_movie_description_tx = LIGHTGRAY

        # Dibuja las textboxes con su color por pantalla
        pygame.draw.rect(self.screen, self.color_movie_name_tx, self.name_text.tx_rect, 0, 5)
        pygame.draw.rect(self.screen, self.color_movie_date_tx, self.date_text.tx_rect, 0, 5)
        pygame.draw.rect(self.screen, self.color_movie_country_tx, self.country_text.tx_rect, 0, 5)
        pygame.draw.rect(self.screen, self.color_movie_genre_tx, self.genre_text.tx_rect, 0, 5)
        pygame.draw.rect(self.screen, self.color_movie_description_tx, self.description_text.tx_rect, 0, 5)
    
    # Escribe en las variables lo que el usuario escribe
    def write_user_text(self): 
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_BACKSPACE and self.name_text.state:
                self.texts_list[0].text = self.texts_list[0].text[:-1] 
            elif self.name_text.state and len(self.texts_list[0].text) < 61:
                self.texts_list[0].text += self.event.unicode
            if self.event.key == pygame.K_BACKSPACE and self.date_text.state:
                self.texts_list[1].text = self.texts_list[1].text[:-1]
            elif self.date_text.state and len(self.texts_list[1].text) < 61:
                self.texts_list[1].text += self.event.unicode
            if self.event.key == pygame.K_BACKSPACE and self.country_text.state:
                self.texts_list[2].text = self.texts_list[2].text[:-1]
            elif self.country_text.state and len(self.texts_list[2].text) <= 3:
                self.texts_list[2].text += self.event.unicode
            if self.event.key == pygame.K_BACKSPACE and self.genre_text.state:
                self.texts_list[3].text = self.texts_list[3].text[:-1]
            elif self.genre_text.state and len(self.texts_list[3].text) <= 3:
                self.texts_list[3].text += self.event.unicode
            
            self.description_mechanics()

    # Mecánicas del taburador
    def tab_mechanics(self):
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_TAB:
                if self.name_text.state:    
                    self.texts_list[0].text = self.texts_list[0].text[:-1]
                    self.name_text.state = False
                    self.date_text.state = True
                elif self.date_text.state:
                    self.texts_list[1].text = self.texts_list[1].text[:-1]
                    self.date_text.state = False
                    self.country_text.state = True
                elif self.country_text.state:
                    if len(self.country_text.text) != 3:
                        self.texts_list[2].text = self.texts_list[2].text[:-1]
                    self.country_text.state = False
                    self.genre_text.state = True
                elif self.genre_text.state:
                    if len(self.genre_text.text) != 3:    
                        self.texts_list[3].text = self.texts_list[3].text[:-1]
                    self.genre_text.state = False
                    self.description_text.state = True
                elif self.description_text.state:
                    self.description_list[self.index].text = self.description_list[self.index].text[:-1]
                    self.description_text.state = False
                    self.name_text.state = True

    # Mecánicas del escape
    def esc_mechanics(self):
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_ESCAPE:
                self.escape += 1

    # Mecánicas del enter
    def enter_mechanics(self):
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_RETURN:
                if self.name_text.state and len(self.name_text.text) != 0:
                    self.name_text.text = self.name_text.text[:-1]
                elif self.date_text.state and len(self.date_text.text) != 0:
                    self.date_text.text = self.date_text.text[:-1]
                elif self.country_text.state and len(self.country_text.text) != 0:
                    self.country_text.text = self.country_text.text[:-1]
                elif self.genre_text.state and len(self.genre_text.text) != 0:
                    self.genre_text.text = self.genre_text.text[:-1]
                elif self.description_text.state and len(self.description_list[self.index].text) != 0 and self.index < 15:
                    self.index += 1
                    self.description_list[self.index - 1].text = self.description_list[self.index - 1].text[:-1]
                    
    # Mecánicas del tick
    def get_tick(self):
        try:    
            if self.event.type == pygame.MOUSEBUTTONDOWN:
                if self.tick_rect.collidepoint(self.mx, self.my):
                    if len(self.name_text.text) != 0:    
                        self.description_list_text = []
                        for i in NM_Description.description_list_temp:
                            self.description_list_text.append(i.text)
                        self.all_descriptions = ' '.join(self.description_list_text)
                        e.insert_movies(self.name_text.text, self.date_text.text, self.country_text.text, self.genre_text.text, self.all_descriptions)
                        e.insert_Pelicula_Usuario()
                        self.escape += 1
                        self.name_text.text = ''
                        self.date_text.text = ''
                        self.country_text.text = ''
                        self.genre_text.text = ''
                        for i in self.description_list:
                            i.text = ''
                        NM_Text.texts_list_temp.clear()
                        NM_Description.description_list_temp.clear()
                    else:
                        self.error_name_state = True
                        self.error_c_g_state = False    
        except IntegrityError:
            self.error_c_g_state = True
            self.error_name_state = False
            c.session.rollback()
                
    # Muestra las líneas de la descripción por pantalla
    def description_display(self): 
        for i in self.description_list:   
            self.surface = self.font2.render(i.text, True, (47, 86, 233))
            self.screen.blit(self.surface, (i.blit_coords))

    # Funcionamiento de las líneas de la descripción
    def description_mechanics(self):
        if self.event.key == pygame.K_BACKSPACE and self.description_text.state:
            self.description_list[self.index].text = self.description_list[self.index].text[:-1]
            if self.index < 15 and len(self.description_list[self.index].text) == 0 and self.index != 0:
                self.index -= 1
        elif self.description_text.state and len(self.description_list[self.index].text) < 61:
            self.description_list[self.index].text += self.event.unicode
        elif len(self.description_list[self.index].text) > 59 and self.index < 15 and self.description_text.state:
            self.index += 1

pygame.quit()
