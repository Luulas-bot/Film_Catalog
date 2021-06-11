import pygame
import sys
from Files.Constants import (
    WHITE, BLUE, GRAY, LIGHTGRAY, clock, fps, size_add_new
)
from Files.New_movie import AddMovie
from Files.Buttons import Buttons, Genre_Buttons
from Files.Movies import Movies
from Files.Database_Connection import e

pygame.init()

class Main_menu():

    # Función constructora
    def __init__(self, size):
        self.size = size
        self.init_stats()

    # Función alterna para correr el main_menu
    def run_main_menu(self):

        bol_main_menu = True   

        self.init_stats()

        while bol_main_menu:
            self.events()
            self.draw_on_screen()
        
            pygame.display.flip()
        
    # Función que determina las variables iniciales
    def init_stats(self):
        
        pygame.display.quit()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Sign Up")
        
        # Boleano para saber si los botones de los géneros están presionados o no
        self.all_genre_buttons_active = False

        # Variables de la textbox de los países
        self.text_box_font = pygame.font.SysFont("consolas", 20)
        self.country_text = ""
        self.country_textbox_active = False
        self.country_textbox = pygame.Rect(200, 625, 300, 50)

        # Botones
        self.all_button = Buttons("Images/all_button.png", "Images/all_pressed_button.png", (0, 0, 200, 100), (0, 0))
        self.genre_button = Buttons("Images/genre_button.png", "Images/genre_pressed_button.png", (0, 100, 200, 100), (0, 100))
        self.to_watch_button = Buttons("Images/to_watch_button.png", "Images/to_watch_pressed_button.png", (0, 200, 200, 100), (0, 200))
        self.already_seen_button = Buttons("Images/already_seen_button.png", "Images/already_seen_pressed_button.png", (0, 300, 200, 100), (0, 300))
        self.top_button = Buttons("Images/top_button.png", "Images/top_pressed_button.png", (0, 400, 200, 100), (0, 400))
        self.worst_button = Buttons("Images/worst_button.png", "Images/worst_pressed_button.png", (0, 500, 200, 100), (0, 500))
        self.country_button = Buttons("Images/country_button.png", "Images/country_pressed_button.png", (0, 600, 200, 100), (0, 600))
        self.exit_button = Buttons("Images/exit_button.png", "Images/exit_pressed_button.png", (0, 700, 200, 100), (0, 700))
        self.add_button = Buttons("Images/add_new_button.png", "Images/add_new_pressed_button.png", (900, 0, 200, 100), (900, 0))

        self.button_list = []

        for i in Buttons.buttons_list_temp:
            self.button_list.append(i)

        # Botónes de género
        self.action_button = Genre_Buttons("Images/action_button.png", "Images/action_pressed_button.png", (200, 70, 120, 60), (200, 70))
        self.science_fiction_button = Genre_Buttons("Images/science_fiction.png", "Images/science_fiction_pressed_button.png", (200, 130, 120, 60), (200, 130))
        self.comedy_button = Genre_Buttons("Images/comedy_button.png", "Images/comedy_pressed_button.png", (200, 190, 120, 60), (200, 190))
        self.drama_button = Genre_Buttons("Images/drama_button.png", "Images/drama_pressed_button.png", (200, 250, 120, 60), (200, 250))
        self.fantasy_button = Genre_Buttons("Images/fantasy_button.png", "Images/fantasy_pressed_button.png", (200, 310, 120, 60), (200, 310))
        self.melodrama_button = Genre_Buttons("Images/melodrama_button.png", "Images/melodrama_pressed_button.png", (200, 370, 120, 60), (200, 370))
        self.musical_button = Genre_Buttons("Images/musical_button.png", "Images/musical_pressed_button.png", (200, 430, 120, 60), (200, 430))
        self.romance_button = Genre_Buttons("Images/romance_button.png", "Images/romance_pressed_button.png", (200, 490, 120, 60), (200, 490))
        self.suspense_button = Genre_Buttons("Images/suspense_button.png", "Images/suspense_pressed_button.png", (200, 550, 120, 60), (200, 550))
        self.terror_button = Genre_Buttons("Images/terror_button.png", "Images/terror_pressed_button.png", (200, 610, 120, 60), (200, 610))
        self.documentary_button = Genre_Buttons("Images/documentary_button.png", "Images/documentary_pressed_button.png", (200, 670, 120, 60), (200, 670))

        self.genre_button_list = []

        for i in Genre_Buttons.genre_buttons_list_temp:
            self.genre_button_list.append(i)

        self.index = 0
        
        e.select_movies_to_display()

        self.init_movies()

        # Flecha para cambiar de página
        self.arrow_right = pygame.image.load("Images/arrow_right.png")
        self.arrow_right_rect = pygame.Rect(1050, 380, 40, 40)

    # Función que registra los eventos
    def events(self):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                sys.exit()
            
            # Obtiene la posición del mouse
            self.mx, self.my = pygame.mouse.get_pos()
            
            self.get_main_button_press()
            self.get_add_button_press()
            self.get_all_buttons_press()
            self.country_textbox_mechanics()
            self.get_genre_button_press()
            self.exit_button_mecs()
            self.get_arrow_right()

            # Registra si el genre_button está activo o no y descativa los botones de los géneros
            if self.genre_button.state == False:
                self.all_genre_buttons_active = False

    # Función que dibuja por pantalla los elementos
    def draw_on_screen(self):
        self.screen.fill(GRAY)

        self.draw_buttons()
        self.draw_genre_buttons()

        self.all_sprites_list.update()
        self.all_sprites_list.draw(self.screen)

        self.draw_country_text()

        self.screen.blit(self.arrow_right, (1050, 380))

        self.blit_movies()
                
    # Crea una textbox para determinar el país que se usará como filtro
    def country_textbox_mechanics(self):    
        
        # Registra todas las formas en las cuales el usuario puede activar o desactivar la textbox
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            if self.country_button.rect.collidepoint(self.mx, self.my):
                if self.country_button.state:
                    self.all_genre_buttons_active = False
                    self.genre_button.state = False
                    self.country_textbox_active = True
                elif self.country_button.state == False:
                    self.country_textbox_active = False   
        if self.event.type == pygame.KEYDOWN and self.country_textbox_active:
            if self.event.key == pygame.K_ESCAPE:
                self.country_textbox_active = False
                self.country_text = ""
                self.country_button.state = False
            if self.event.key == pygame.K_RETURN:
                self.country_textbox_active = False
                self.country_text = ""
                self.country_button.state = False

        # Registra lo que presiona el usuario y lo guarda en una variable    
        if self.country_textbox_active:
            if self.event.type == pygame.KEYDOWN:
                if self.event.key == pygame.K_BACKSPACE:
                    self.country_text = self.country_text[:-1]
                elif len(self.country_text) < 26:
                    self.country_text += self.event.unicode

    # Registra el presionado de todos los botones
    def get_all_buttons_press(self):
        for button in self.button_list[1:-1]:    
            if self.event.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(self.mx, self.my):
                    button.state = not button.state
                    if button == self.to_watch_button and self.to_watch_button.state:
                        self.already_seen_button.state = False
                    if button == self.already_seen_button and self.already_seen_button:
                        self.to_watch_button.state = False
                    if button == self.top_button and self.top_button.state:
                        self.worst_button.state = False
                    if button == self.worst_button and self.worst_button.state:
                        self.top_button.state = False
                    if button == self.genre_button and self.genre_button.state:
                        self.country_button.state = False
                        self.all_genre_buttons_active = True
                        self.country_textbox_active = False
                    if button == self.country_button and self.country_button.state:
                        self.genre_button.state = False

    # Registra si algún botón de género es presionado   
    def get_genre_button_press(self):
        for button in self.genre_button_list:
            if self.event.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(self.mx, self.my):
                    button.state = not button.state
            if self.event.type == pygame.MOUSEBUTTONUP:
                if button.rect.collidepoint(self.mx, self.my):
                    button.state = not button.state
                    self.genre_button.state = False
                    self.all_genre_buttons_active = False

    # Registra si se presionó o no el all_button (en este caso llamado el main)
    def get_main_button_press(self):
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            if self.all_button.rect.collidepoint(self.mx, self.my):
                self.all_button.state = True
        elif self.event.type == pygame.MOUSEBUTTONUP:
            if self.all_button.rect.collidepoint(self.mx, self.my):
                for button in self.button_list:
                    button.state = False
                    self.all_genre_buttons_active = False
                    self.country_textbox_active = False
                
    # Mecánicas del exit_button
    def exit_button_mecs(self):
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            if self.exit_button.rect.collidepoint(self.mx, self.my):
                self.exit_button.state = True
        elif self.event.type == pygame.MOUSEBUTTONUP:
            if self.exit_button.rect.collidepoint(self.mx, self.my):
                self.exit_button.state = False
                sys.exit()

    # Mecánicas del add_button
    def get_add_button_press(self):
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            if self.add_button.rect.collidepoint(self.mx, self.my):
                self.add_button.state = True
        elif self.event.type == pygame.MOUSEBUTTONUP:
            if self.add_button.rect.collidepoint(self.mx, self.my):
                for button in self.button_list:
                    button.state = False
                    self.all_genre_buttons_active = False
                    self.country_textbox_active = False
                return self.run_add_new_movie()

    # Dibuja los botones por pantalla
    def draw_buttons(self):
        for button in self.button_list:
            if button.state == True:
                self.screen.blit(button.pressed_button, button.coords)
            else:
                self.screen.blit(button.button, button.coords)

    # Dibuja los botones de género por pantalla
    def draw_genre_buttons(self):
        for button in self.genre_button_list:
            if self.all_genre_buttons_active:
                if button.state == True:
                    self.screen.blit(button.pressed_button, button.coords)
                else:
                    self.screen.blit(button.button, button.coords)

    # Dibuja el texto ingresado por el usuario en la textbox de los países
    def draw_country_text(self):
        if self.country_textbox_active:
            pygame.draw.rect(self.screen, WHITE, self.country_textbox, 0, 5)
            text_surface = self.text_box_font.render(self.country_text, True, BLUE)
            self.screen.blit(text_surface, (207, 645))

    def get_arrow_right(self):
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            if self.arrow_right_rect.collidepoint(self.mx, self.my):
                self.index += 6
                self.init_movies()
    
    def init_movies(self):
        self.all_sprites_list = pygame.sprite.Group()
        self.movie = Movies("Images/movies_rect.png", (290, 120), e.movies_display_name[self.index], e.movies_display_genre_name[self.index], (300, 130), (300, 170))
        self.movie2 = Movies("Images/movies_rect.png", (540, 120), e.movies_display_name[self.index + 1], e.movies_display_genre_name[self.index + 1], (550, 130), (550, 170))
        self.movie3 = Movies("Images/movies_rect.png", (800, 120), e.movies_display_name[self.index + 2], e.movies_display_genre_name[self.index + 2], (810, 130), (810, 170))
        self.movie4 = Movies("Images/movies_rect.png", (290, 450), e.movies_display_name[self.index + 3], e.movies_display_genre_name[self.index + 3], (300, 460), (300, 500))
        self.movie5 = Movies("Images/movies_rect.png", (540, 450), e.movies_display_name[self.index + 4], e.movies_display_genre_name[self.index + 4], (550, 460), (550, 500))
        self.movie6 = Movies("Images/movies_rect.png", (800, 450), e.movies_display_name[self.index + 5], e.movies_display_genre_name[self.index + 5], (810, 460), (810, 500))

        for i in Movies.movies_list_temp:
            self.all_sprites_list.add(i)
        
    # Se dibujan por pantalla las películas
    def blit_movies(self):
        self.screen.blit(self.movie.name_blit, (self.movie.blit_coords_name))
        self.screen.blit(self.movie.genre_blit, (self.movie.blit_coords_genre))
        self.screen.blit(self.movie2.name_blit, (self.movie2.blit_coords_name))
        self.screen.blit(self.movie2.genre_blit, (self.movie2.blit_coords_genre))
        self.screen.blit(self.movie3.name_blit, (self.movie3.blit_coords_name))
        self.screen.blit(self.movie3.genre_blit, (self.movie3.blit_coords_genre))
        self.screen.blit(self.movie4.name_blit, (self.movie4.blit_coords_name))
        self.screen.blit(self.movie4.genre_blit, (self.movie4.blit_coords_genre))
        self.screen.blit(self.movie5.name_blit, (self.movie5.blit_coords_name))
        self.screen.blit(self.movie5.genre_blit, (self.movie5.blit_coords_genre))
        self.screen.blit(self.movie6.name_blit, (self.movie6.blit_coords_name))
        self.screen.blit(self.movie6.genre_blit, (self.movie6.blit_coords_genre))
        
    # Corre el menú para crear una nueva película
    def run_add_new_movie(self):

        am = AddMovie(size_add_new)

        while True:
            am.events()
            am.draw_on_screen()

            if am.escape >= 1:
                del self.text_box_font
                self.run_main_menu()
                break

            pygame.display.flip()
            clock.tick(fps)

pygame.quit()