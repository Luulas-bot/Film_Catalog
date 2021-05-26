import pygame
import sys
from Files.Constants import (WHITE, BLUE, GRAY, LIGHTGRAY, all_button, genre_button, to_watch_button, already_seen_button,
                            top_button, worst_button, country_button, exit_button, action_button, science_fiction_button, 
                            comedy_button, drama_button, fantasy_button, melodrama_button, musical_button, romance_button,
                            suspense_button, terror_button, documentary_button, button_list, genre_button_list, color_user_textbox,

                            )

class Main_menu():

    # Función constructora
    def __init__(self, size):
        self.size = size
        self.init_stats()

    # Función que determina las variables iniciales
    def init_stats(self):
        self.screen = pygame.display.set_mode((self.size))

        # Boleano para saber si los botones de los géneros están presionados o no
        self.all_genre_buttons_active = False

        # Variables de la textbox de los países
        self.text_box_font = pygame.font.SysFont("consolas", 20)
        self.country_text = ""
        self.country_textbox_active = False
        self.country_textbox = pygame.Rect(200, 625, 300, 50)

    # Función que registra los eventos
    def events(self):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                sys.exit()
            
            # Obtiene la posición del mouse
            self.mx, self.my = pygame.mouse.get_pos()
            
            self.get_main_button_press()
            self.get_all_buttons_press()
            self.country_textbox_mechanics()
            self.get_genre_button_press()
            self.exit_button()

            # Registra si el genre_button está activo o no y descativa los botones de los géneros
            if genre_button.state == False:
                self.all_genre_buttons_active = False

    # Función que dibuja por pantalla los elementos
    def draw_on_screen(self):
        self.screen.fill(GRAY)

        self.draw_buttons()
        self.draw_genre_buttons()
        
        # Determina el color de la textbox
        if self.country_textbox_active:
            color_user_textbox = WHITE
        else:
            color_user_textbox = LIGHTGRAY

        self.draw_country_text()
                
    # Crea una textbox para determinar el país que se usará como filtro
    def country_textbox_mechanics(self):    
        
        # Registra todas las formas en las cuales el usuario puede activar o desactivar la textbox
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            if country_button.rect.collidepoint(self.mx, self.my):
                if country_button.state:
                    self.all_genre_buttons_active = False
                    genre_button.state = False
                    self.country_textbox_active = True
                elif country_button.state == False:
                    self.country_textbox_active = False   
        if self.event.type == pygame.KEYDOWN and self.country_textbox_active:
            if self.event.key == pygame.K_ESCAPE:
                self.country_textbox_active = False
                self.country_text = ""
                country_button.state = False
            if self.event.key == pygame.K_RETURN:
                self.country_textbox_active = False
                self.country_text = ""
                country_button.state = False

        # Registra lo que presiona el usuario y lo guarda en una variable    
        if self.country_textbox_active:
            if self.event.type == pygame.KEYDOWN:
                if self.event.key == pygame.K_BACKSPACE:
                    self.country_text = self.country_text[:-1]
                elif len(self.country_text) < 26:
                    self.country_text += self.event.unicode

    # Registra el presionado de todos los botones
    def get_all_buttons_press(self):
        for button in button_list[1:-1]:    
            if self.event.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(self.mx, self.my):
                    button.state = not button.state
                    if button == to_watch_button and to_watch_button.state:
                        already_seen_button.state = False
                    if button == already_seen_button and already_seen_button:
                        to_watch_button.state = False
                    if button == top_button and top_button.state:
                        worst_button.state = False
                    if button == worst_button and worst_button.state:
                        top_button.state = False
                    if button == genre_button and genre_button.state:
                        country_button.state = False
                        self.all_genre_buttons_active = True
                        self.country_textbox_active = False
                    if button == country_button and country_button.state:
                        genre_button.state = False

    # Registra si algún botón de género es presionado   
    def get_genre_button_press(self):
        for button in genre_button_list:
            if self.event.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(self.mx, self.my):
                    button.state = not button.state
            if self.event.type == pygame.MOUSEBUTTONUP:
                if button.rect.collidepoint(self.mx, self.my):
                    button.state = not button.state
                    genre_button.state = False
                    self.all_genre_buttons_active = False

    # Registra si se presionó o no el all_button (en este caso llamado el main)
    def get_main_button_press(self):
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            if all_button.rect.collidepoint(self.mx, self.my):
                all_button.state = True
        elif self.event.type == pygame.MOUSEBUTTONUP:
            if all_button.rect.collidepoint(self.mx, self.my):
                for button in button_list:
                    button.state = False
                    self.all_genre_buttons_active = False
                    self.country_textbox_active = False
                
    # Mecánicas del exit_button
    def exit_button(self):
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            if exit_button.rect.collidepoint(self.mx, self.my):
                exit_button.state = True
        elif self.event.type == pygame.MOUSEBUTTONUP:
            if exit_button.rect.collidepoint(self.mx, self.my):
                exit_button.state = False
                sys.exit()

    # Dibuja los botones por pantalla
    def draw_buttons(self):
        for button in button_list:
            if button.state == True:
                self.screen.blit(button.pressed_button, button.coords)
            else:
                self.screen.blit(button.button, button.coords)

    # Dibuja los botones de género por pantalla
    def draw_genre_buttons(self):
        for button in genre_button_list:
            if self.all_genre_buttons_active:
                if button.state == True:
                    self.screen.blit(button.pressed_button, button.coords)
                else:
                    self.screen.blit(button.button, button.coords)

    # Dibuja el texto ingresado por el usuario en la textbox de los países
    def draw_country_text(self):
        if self.country_textbox_active:
            pygame.draw.rect(self.screen, color_user_textbox, self.country_textbox, 0, 5)
            text_surface = self.text_box_font.render(self.country_text, True, BLUE)
            self.screen.blit(text_surface, (207, 645))

# TODO - Hacer los boleanos de los generos y dibujarlos por pantalla
# - Tambien para buscar los paises ya que son muchos es mejor dejar que el usuario escriba el pais que quiera buscar. 
# Poner todos los paises que quiero en una base de datos y ver si concuerdan con lo que el usuario, escribe, si es asi,
# poner una condicion que busque por el nombre del pais todas las peliculas