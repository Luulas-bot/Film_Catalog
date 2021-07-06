# Imports
import pygame
import sys
from Constants.constants import GRAY, WHITE, LIGHTGRAY, BLUE, LIGHTBLUE, GOLD
from Classes import NmText, NmDescription
from sqlalchemy.exc import IntegrityError

# Inicialización de pygame
pygame.init()

# Clase de la ventana
class NewMovie():
     
    # Función constructora
    def __init__(self, size, dm):
         self.size = size
         self.init_stats()
         self.dm = dm

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

        # NmText texts   
        self.name_text = NmText((55, 57), "", (50, 50, 500, 30), (50, 50), (55, 57))
        self.date_text = NmText((55, 132), "", (50, 125, 500, 30), (50, 100), (55, 132))
        self.country_text = NmText ((55, 207), "", (50, 200, 200, 30), (50, 150), (55, 207))
        self.genre_text = NmText((305, 207),"", (300, 200, 200, 30), (200, 150), (305, 207))
        self.description_text = NmDescription((55, 282), "", (50, 275, 500, 275), (50, 200))
        self.description_text2 = NmDescription((55, 300), "", (50, 275, 500, 275), (50, 200))
        self.description_text3 = NmDescription((55, 318), "", (50, 275, 500, 275), (50, 200))
        self.description_text4 = NmDescription((55, 336), "", (50, 275, 500, 275), (50, 200))
        self.description_text5 = NmDescription((55, 354), "", (50, 275, 500, 275), (50, 200))
        self.description_text6 = NmDescription((55, 372), "", (50, 275, 500, 275), (50, 200))
        self.description_text7 = NmDescription((55, 390), "", (50, 275, 500, 275), (50, 200))
        self.description_text8 = NmDescription((55, 408), "", (50, 275, 500, 275), (50, 200))
        self.description_text9 = NmDescription((55, 426), "", (50, 275, 500, 275), (50, 200))
        self.description_text10 = NmDescription((55, 444), "", (50, 275, 500, 275), (50, 200))
        self.description_text11 = NmDescription((55, 462), "", (50, 275, 500, 275), (50, 200))
        self.description_text12 = NmDescription((55, 480), "", (50, 275, 500, 275), (50, 200))
        self.description_text13 = NmDescription((55, 498), "", (50, 275, 500, 275), (50, 200))
        self.description_text14 = NmDescription((55, 516), "", (50, 275, 500, 275), (50, 200))
        self.description_text15 = NmDescription((55, 534), "", (50, 275, 500, 275), (50, 200))
    
        # Listas que contienen parcialmente o totalmente los textos y textboxes definidos arrriba
        self.description_list = []
        self.texts_list = []

        for i in NmDescription.description_list_temp:
            self.description_list.append(i)

        for i in NmText.texts_list_temp:
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

        # Cambia los colores de las textboxes
        self.change_tx_color()

        # Dibuja por pantalla los inputs de texto del usuario
        for t in self.texts_list:
            self.text_surface = self.font2.render(t.text, True, BLUE)
            self.screen.blit(self.text_surface, t.text_coords)
        
        # Hace un display de el texto que se escribe en la textbox de la descripción
        self.description_display()

        # Condición que blitea o no el error
        if self.error_c_g_state == True:
            self.screen.blit(self.error_c_g, (50, 557))
        elif self.error_name_state == True:
            self.screen.blit(self.error_name, (50, 557))

        # Dibuja por pantalla el tick
        self.screen.blit(self.tick, (550, 550))

    # Define si están activas o no las textboxes
    def get_tx_state(self):
        for tx in self.texts_list:
            if self.event.type == pygame.MOUSEBUTTONDOWN:
                if tx.tx_rect.collidepoint(self.mx, self.my):
                    tx.state = True
                else:
                    tx.state = False
        
                if self.description_text.tx_rect.collidepoint(self.mx, self.my):
                    self.description_text.state = True
                else:
                    self.description_text.state = False

    # Variable que cambia el color de las textboxes según su estado
    def change_tx_color(self):
        for c in self.texts_list:
            c.change_color()

        if self.description_text.state == True:
            self.color_movie_description_tx = WHITE
        else:
            self.color_movie_description_tx = LIGHTGRAY

        # Dibuja las textboxes con su color por pantalla
        for r in self.texts_list:
            pygame.draw.rect(self.screen, r.color, r.tx_rect, 0, 5)
        
        pygame.draw.rect(self.screen, self.color_movie_description_tx, self.description_text.tx_rect, 0, 5)
    
    # Escribe en las variables lo que el usuario escribe
    def write_user_text(self): 
        for i in self.texts_list[:2]:
            if self.event.type == pygame.KEYDOWN:
                if self.event.key == pygame.K_BACKSPACE and i.state:
                    i.text = i.text[:-1]
                elif i.state and len(i.text) < 61:
                    i.text += self.event.unicode
        for b in self.texts_list[2:]:
            if self.event.type == pygame.KEYDOWN:    
                if self.event.key == pygame.K_BACKSPACE and b.state:
                    b.text = b.text[:-1]
                elif b.state and len(b.text) <= 3:
                    b.text += self.event.unicode
            
        if self.event.type == pygame.KEYDOWN:
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
        for i in self.texts_list:
            if self.event.type == pygame.KEYDOWN:
                if self.event.key == pygame.K_RETURN:
                    if i.state and len(i.text) != 0:
                        i.text = i.text[:-1]
                    elif self.description_text.state and len(self.description_list[self.index].text) != 0 and self.index < 14:
                        self.index += 1
                        self.description_list[self.index - 1].text = self.description_list[self.index - 1].text[:-1]
                    elif self.index == 15:
                        pass
                    
    # Mecánicas del tick
    def get_tick(self):
        try:    
            if self.event.type == pygame.MOUSEBUTTONDOWN:
                if self.tick_rect.collidepoint(self.mx, self.my):
                    if len(self.name_text.text) != 0:    
                        self.description_list_text = []
                        for i in NmDescription.description_list_temp:
                            self.description_list_text.append(i.text)
                        self.all_descriptions = ' '.join(self.description_list_text)
                        self.dm.insert_movies(self.name_text.text, self.date_text.text, self.country_text.text, self.genre_text.text, self.all_descriptions)
                        self.dm.insert_Pelicula_Usuario()
                        self.escape += 1
                        self.name_text.text = ''
                        self.date_text.text = ''
                        self.country_text.text = ''
                        self.genre_text.text = ''
                        for i in self.description_list:
                            i.text = ''
                        NmText.texts_list_temp.clear()
                        NmDescription.description_list_temp.clear()
                    else:
                        self.error_name_state = True
                        self.error_c_g_state = False    
        except IntegrityError:
            self.error_c_g_state = True
            self.error_name_state = False
            self.dm.cn.session.rollback()
                
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
