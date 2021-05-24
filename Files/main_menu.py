import pygame
import sys
from Files.Constants import (WHITE, BLUE, GRAY, all_button, genre_button, to_watch_button, already_seen_button,
                            top_button, worst_button, country_button, exit_button, action_button, science_fiction_button, 
                            comedy_button, drama_button, fantasy_button, melodrama_button, musical_button, romance_button,
                            suspense_button, terror_button, documentary_button, button_list, genre_button_list
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

    # Función que registra los eventos
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            # Obtiene la posición del mouse
            mx, my = pygame.mouse.get_pos()
            
            # Registra si se apretó el all_button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if all_button.rect.collidepoint(mx, my):
                    all_button.state = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if all_button.rect.collidepoint(mx, my):
                    for button in button_list:
                        button.state = False
            
            # Registra el presionado de todos los botones
            for button in button_list[1:-1]:    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button.rect.collidepoint(mx, my):
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
                        if button == country_button and country_button.state:
                            genre_button.state = False

            # Registra si el genre_button está activo o no y descativa los botones de los géneros
            if genre_button.state == False:
                self.all_genre_buttons_active = False
                
            # Registra si algún botón de género es presionado
            for button in genre_button_list:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button.rect.collidepoint(mx, my):
                        button.state = not button.state
                if event.type == pygame.MOUSEBUTTONUP:
                    if button.rect.collidepoint(mx, my):
                        button.state = not button.state
                        genre_button.state = False
                        self.all_genre_buttons_active = False

            # Registra si se presiona el exit_button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.rect.collidepoint(mx, my):
                    exit_button.state = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if exit_button.rect.collidepoint(mx, my):
                    exit_button.state = False
                    sys.exit()


    # Función que dibuja por pantalla los elementos
    def draw_on_screen(self):
        self.screen.fill(GRAY)

        # Dibuja por pantalla los botones
        for button in button_list:
            if button.state == True:
                self.screen.blit(button.pressed_button, button.coords)
            else:
                self.screen.blit(button.button, button.coords)

        # Dibuja por pantalla los botones de los géneros
        for button in genre_button_list:
            if self.all_genre_buttons_active:
                if button.state == True:
                    self.screen.blit(button.pressed_button, button.coords)
                else:
                    self.screen.blit(button.button, button.coords)
                
# TODO - Hacer los boleanos de los generos y dibujarlos por pantalla
# - Tambien para buscar los paises ya que son muchos es mejor dejar que el usuario escriba el pais que quiera buscar. 
# Poner todos los paises que quiero en una base de datos y ver si concuerdan con lo que el usuario, escribe, si es asi,
# poner una condicion que busque por el nombre del pais todas las peliculas