import pygame
import sys
from Files.Constants import (WHITE, BLUE, GRAY, all_button, genre_button, to_watch_button, already_seen_button,
                            top_button, worst_button, country_button, exit_button, all_button_pressed, genre_button_pressed,
                            to_watch_button_pressed, already_seen_button_pressed, top_button_pressed, worst_button_pressed,
                            country_button_pressed, exit_button_pressed
                            )

class Main_menu():

    # Función constructora
    def __init__(self, size):
        self.size = size
        self.init_stats()

    # Función que determina las variables iniciales
    def init_stats(self):
        self.screen = pygame.display.set_mode((self.size))

        # Boleanos para saber que botones están presionados
        self.all_button_active = False
        self.genre_button_active = False
        self.to_watch_button_active = False
        self.already_seen_button_active = False
        self.top_button_active = False
        self.worst_button_active = False
        self.country_button_active = False
        self.exit_button_active = False

        # Hitboxes de los botones
        self.all_button_rect = pygame.Rect(0, 0, 200, 100)
        self.genre_button_rect = pygame.Rect(0, 100, 200, 100)
        self.to_watch_button_rect = pygame.Rect(0, 200, 200, 100)
        self.already_seen_button_rect = pygame.Rect(0, 300, 200, 100)
        self.top_button_rect = pygame.Rect(0, 400, 200, 100)
        self.worst_button_rect = pygame.Rect(0, 500, 200, 100)
        self.country_button_rect = pygame.Rect(0, 600, 200, 100)
        self.exit_button_rect = pygame.Rect(0, 700, 200, 100)

    # Función que registra los eventos
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            # Obtiene la posición del mouse
            mx, my = pygame.mouse.get_pos()
            
            # Registra los eventos de los botones
            # all_button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.all_button_rect.collidepoint(mx, my):
                    self.all_button_active = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.all_button_rect.collidepoint(mx, my):
                    self.all_button_active = False

            # genre_button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.genre_button_rect.collidepoint(mx, my):
                    self.genre_button_active = True

            # to_watch_button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.to_watch_button_rect.collidepoint(mx, my):
                    self.to_watch_button_active = True
                    self.already_seen_button_active = False
            
            # already_seen_button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.already_seen_button_rect.collidepoint(mx, my):
                    self.already_seen_button_active = True
                    self.to_watch_button_active = False
            
            # top_button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.top_button_rect.collidepoint(mx, my):
                    self.top_button_active = True
                    self.worst_button_active = False

            # worst_button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.worst_button_rect.collidepoint(mx, my):
                    self.worst_button_active = True
                    self.top_button_active = False

            # country_button           
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.country_button_rect.collidepoint(mx, my):
                    self.country_button_active = True
            
            # exit_button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.exit_button_rect.collidepoint(mx, my):
                    self.exit_button_active = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.exit_button_rect.collidepoint(mx, my):
                    self.exit_button_active = False
                    sys.exit()

    # Función que dibuja por pantalla los elementos
    def draw_on_screen(self):
        self.screen.fill(GRAY)

        # Dibuja por pantalla los botones en su estado normal
        self.screen.blit(all_button, (0, 0))
        self.screen.blit(genre_button, (0, 100))
        self.screen.blit(to_watch_button, (0, 200))
        self.screen.blit(already_seen_button, (0, 300))
        self.screen.blit(top_button, (0, 400))
        self.screen.blit(worst_button, (0, 500))
        self.screen.blit(country_button, (0, 600))
        self.screen.blit(exit_button, (0, 700))

        # Dibuja los botones cuando están presionados
        if self.all_button_active:
            self.screen.blit(all_button_pressed,(0, 0))
        if self.genre_button_active:
            self.screen.blit(genre_button_pressed,(0, 100))
        if self.to_watch_button_active:
            self.screen.blit(to_watch_button_pressed,(0, 200))
        if self.already_seen_button_active:
            self.screen.blit(already_seen_button_pressed,(0, 300))
        if self.top_button_active:
            self.screen.blit(top_button_pressed,(0, 400))
        if self.worst_button_active:
            self.screen.blit(worst_button_pressed,(0, 500))
        if self.country_button_active:
            self.screen.blit(country_button_pressed,(0, 600))
        if self.exit_button_active:
            self.screen.blit(exit_button_pressed,(0, 700))

# TODO - hay que hacer 11 botones mas que contengan los diferentes generos de peliculas. cada uno de estos va a ser de 120 x 60
# - Tambien para buscar los paises ya que son muchos es mejor dejar que el usuario escriba el pais que quiera buscar. 
# Poner todos los paises que quiero en una base de datos y ver si concuerdan con lo que el usuario, escribe, si es asi,
# poner una condicion que busque por el nombre del pais todas las peliculas