import pygame
import sys
from Files.Constants import (WHITE, BLUE, GRAY, all_button, genre_button, to_watch_button, already_seen_button,
                            top_button, worst_button, country_button, exit_button, all_button_pressed, genre_button_pressed,
                            to_watch_button_pressed, already_seen_button_pressed, top_button_pressed, worst_button_pressed,
                            country_button_pressed, exit_button_pressed, action_button, science_fiction_button, comedy_button,
                            drama_button, fantasy_button, melodrama_button, musical_button, romance_button, suspense_button,
                            terror_button, documentary_button, action_pressed_button, comedy_pressed_button, science_fiction_pressed_button,
                            drama_pressed_button, fantasy_pressed_button, melodrama_pressed_button, musical_pressed_button, romance_pressed_button,
                            suspense_pressed_button, terror_pressed_button, documentary_pressed_button
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

        # Boleanos para saber si los botónes de género están individualmente presionados
        self.action_button_active = False
        self.comedy_button_active = False
        self.science_fiction_button_active = False
        self.drama_button_active = False
        self.fantasy_button_active = False
        self.melodrama_button_active = False
        self.musical_button_active = False
        self.romance_button_active = False
        self.suspense_button_active = False
        self.terror_button_active = False
        self.documentary_button_active = False

        # Boleano para saber si los botones de los géneros están presionados o no
        self.all_genre_buttons_active = False

        # Boleano para saber si los botones de los países están presionados o no
        self.all_country_buttons_active = False

        # Hitboxes de los botones
        self.all_button_rect = pygame.Rect(0, 0, 200, 100)
        self.genre_button_rect = pygame.Rect(0, 100, 200, 100)
        self.to_watch_button_rect = pygame.Rect(0, 200, 200, 100)
        self.already_seen_button_rect = pygame.Rect(0, 300, 200, 100)
        self.top_button_rect = pygame.Rect(0, 400, 200, 100)
        self.worst_button_rect = pygame.Rect(0, 500, 200, 100)
        self.country_button_rect = pygame.Rect(0, 600, 200, 100)
        self.exit_button_rect = pygame.Rect(0, 700, 200, 100)

        # Hitboxes de los botones de género
        self.action_button_rect = pygame.Rect(200, 70, 120, 60)
        self.science_fiction_button_rect = pygame.Rect(200, 130, 120, 60)
        self.comedy_button_rect = pygame.Rect(200, 190, 120, 60)
        self.drama_button_rect = pygame.Rect(200, 250, 120, 60)
        self.fantasy_button_rect = pygame.Rect(200, 310, 120, 60)
        self.melodrama_button_rect = pygame.Rect(200, 370, 120, 60)
        self.musical_button_rect = pygame.Rect(200, 430, 120, 60)
        self.romance_button_rect = pygame.Rect(200, 490, 120, 60)
        self.suspense_button_rect = pygame.Rect(200, 550, 120, 60)
        self.terror_button_rect = pygame.Rect(200, 610, 120, 60)
        self.documentary_button_rect = pygame.Rect(200, 670, 120, 60)

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
                    self.genre_button_active = False
                    self.to_watch_button_active = False
                    self.already_seen_button_active = False
                    self.top_button_active = False
                    self.worst_button_active = False
                    self.country_button_active = False
                    self.exit_button_active = False

            # genre_button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.genre_button_active == False:
                    if self.genre_button_rect.collidepoint(mx, my):
                        self.genre_button_active = True
                else:
                    if self.genre_button_rect.collidepoint(mx, my):
                        self.genre_button_active = False

            # genre buttons
            if self.genre_button_active == True:
                self.all_genre_buttons_active = True
                self.all_country_buttons_active = False

            # to_watch_button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.to_watch_button_active == False:
                    if self.to_watch_button_rect.collidepoint(mx, my):
                        self.to_watch_button_active = True
                        self.already_seen_button_active = False
                else:
                    if self.to_watch_button_rect.collidepoint(mx, my):
                        self.to_watch_button_active = False
            
            # already_seen_button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.already_seen_button_active == False:
                    if self.already_seen_button_rect.collidepoint(mx, my):
                        self.already_seen_button_active = True
                        self.to_watch_button_active = False
                else:
                    if self.already_seen_button_rect.collidepoint(mx, my):
                        self.already_seen_button_active = False

            # top_button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.top_button_active == False:
                    if self.top_button_rect.collidepoint(mx, my):
                        self.top_button_active = True
                        self.worst_button_active = False
                else:
                    if self.top_button_rect.collidepoint(mx, my):
                        self.top_button_active = False

            # worst_button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.worst_button_active == False:    
                    if self.worst_button_rect.collidepoint(mx, my):
                        self.worst_button_active = True
                        self.top_button_active = False

                else:
                    if self.worst_button_rect.collidepoint(mx, my):
                        self.worst_button_active = False

            # country_button           
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.country_button_active == False:    
                    if self.country_button_rect.collidepoint(mx, my):
                        self.country_button_active = True
                else:
                    if self.country_button_rect.collidepoint(mx, my):
                        self.country_button_active = False
            
            # exit_button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.exit_button_rect.collidepoint(mx, my):
                    self.exit_button_active = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.exit_button_rect.collidepoint(mx, my):
                    self.exit_button_active = False
                    sys.exit()

            # Botónes de género
            if self.all_genre_buttons_active:
                
                # Action
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.action_button_rect.collidepoint(mx, my):
                        self.action_button_active = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.action_button_rect.collidepoint(mx, my):
                        self.action_button_active = False
                        self.all_genre_buttons_active = False
                        self.genre_button_active = False

                # Comedy
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.comedy_button_rect.collidepoint(mx, my):
                        self.comedy_button_active = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.comedy_button_rect.collidepoint(mx, my):
                        self.comedy_button_active = False
                        self.all_genre_buttons_active = False
                        self.genre_button_active = False
                
                # Science fiction
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.science_fiction_button_rect.collidepoint(mx, my):
                        self.science_fiction_button_active = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.science_fiction_button_rect.collidepoint(mx, my):
                        self.science_fiction_button_active = False
                        self.all_genre_buttons_active = False
                        self.genre_button_active = False
                
                # Drama
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.drama_button_rect.collidepoint(mx, my):
                        self.drama_button_active = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.drama_button_rect.collidepoint(mx, my):
                        self.drama_button_active = False
                        self.all_genre_buttons_active = False
                        self.genre_button_active = False
                
                # Fanatasy
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.fantasy_button_rect.collidepoint(mx, my):
                        self.fantasy_button_active = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.fantasy_button_rect.collidepoint(mx, my):
                        self.fantasy_button_active = False
                        self.all_genre_buttons_active = False
                        self.genre_button_active = False
                
                # Melodrama
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.melodrama_button_rect.collidepoint(mx, my):
                        self.melodrama_button_active = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.action_button_rect.collidepoint(mx, my):
                        self.action_button_active = False
                        self.all_genre_buttons_active = False
                        self.genre_button_active = False
                
                # Musical
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.action_button_rect.collidepoint(mx, my):
                        self.action_button_active = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.action_button_rect.collidepoint(mx, my):
                        self.action_button_active = False
                        self.all_genre_buttons_active = False
                        self.genre_button_active = False
                
                # Romance
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.action_button_rect.collidepoint(mx, my):
                        self.action_button_active = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.action_button_rect.collidepoint(mx, my):
                        self.action_button_active = False
                        self.all_genre_buttons_active = False
                        self.genre_button_active = False
                
                # Suspense
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.action_button_rect.collidepoint(mx, my):
                        self.action_button_active = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.action_button_rect.collidepoint(mx, my):
                        self.action_button_active = False
                        self.all_genre_buttons_active = False
                        self.genre_button_active = False

                # Terror
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.action_button_rect.collidepoint(mx, my):
                        self.action_button_active = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.action_button_rect.collidepoint(mx, my):
                        self.action_button_active = False
                        self.all_genre_buttons_active = False
                        self.genre_button_active = False

                # Documentary
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.action_button_rect.collidepoint(mx, my):
                        self.action_button_active = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.action_button_rect.collidepoint(mx, my):
                        self.action_button_active = False
                        self.all_genre_buttons_active = False
                        self.genre_button_active = False

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

        # Dibuja los botónes de género por pantalla
        if self.all_genre_buttons_active == True:
            self.screen.blit(action_button, (200, 70))
            self.screen.blit(science_fiction_button, (200, 130))
            self.screen.blit(comedy_button, (200, 190))
            self.screen.blit(drama_button, (200, 250))
            self.screen.blit(fantasy_button, (200, 310))
            self.screen.blit(melodrama_button, (200, 370))
            self.screen.blit(musical_button, (200, 430))
            self.screen.blit(romance_button, (200, 490))
            self.screen.blit(suspense_button, (200, 550))
            self.screen.blit(terror_button, (200, 610))
            self.screen.blit(documentary_button, (200, 670))

    
# TODO - Hacer los boleanos de los generos y dibujarlos por pantalla
# - Tambien para buscar los paises ya que son muchos es mejor dejar que el usuario escriba el pais que quiera buscar. 
# Poner todos los paises que quiero en una base de datos y ver si concuerdan con lo que el usuario, escribe, si es asi,
# poner una condicion que busque por el nombre del pais todas las peliculas