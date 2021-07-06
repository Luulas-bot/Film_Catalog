# Imports
import pygame
import sys
from Constants.constants import GRAY, BLUE, WHITE, LIGHTGRAY, LIGHTBLUE
from Classes import EditTexts, EditDescription, EditButtons
from sqlalchemy.exc import DataError
from Database_manager import dm

# Inicialización de pygame
pygame.init()

# Clase de la ventana
class Edit():

    # Función constructora
    def __init__(self, size, dm):
        self.size = size
        self.init_stats()

    # Inicializa las stats inciales
    def init_stats(self):
        self.dm = dm
        
        pygame.display.quit()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Edit")

        # Fuentes
        self.font1 = pygame.font.SysFont("consolas", 20, bold = True)
        self.font2 = pygame.font.SysFont("consolas", 15, bold = True)
        self.name_title = self.font1.render("Nombre de la película", True, LIGHTBLUE)
        self.date_title = self.font1.render("Fecha", True, LIGHTBLUE)
        self.country_title = self.font1.render("Nacionalidad", True, LIGHTBLUE)
        self.description_title = self.font1.render("Descripción", True, LIGHTBLUE)
        self.genre_title = self.font1.render("Género", True, LIGHTBLUE)
        self.rating_title = self.font1.render("Rating", True, LIGHTBLUE)
        self.delete_text = self.font2.render("BORRAR", True, BLUE)

        # Variable que define si se toca la tecla escape o no
        self.escape = 0

        # Las textboxes junto con sus textos
        self.name_text = EditTexts((55, 57), f"{self.dm.movie_name_edit}", (50, 50, 500, 30), (50, 50), (55, 57))
        self.date_text = EditTexts((55, 132), f"{self.dm.movie_date_edit}", (50, 125, 500, 30), (50, 100), (55, 132))
        self.country_text = EditTexts ((55, 207), f"{self.dm.movie_country_edit}", (50, 200, 200, 30), (50, 150), (55, 207))
        self.genre_text = EditTexts((305, 207),f"{self.dm.movie_genre_edit}", (300, 200, 200, 30), (200, 150), (305, 207))
        self.rating = EditTexts((55, 607), f"{self.dm.movie_rating_edit}", (50, 600, 500, 30), (50, 600), (55, 607))
        self.description_text = EditDescription((55, 282), f"{self.dm.movie_description_edit[:61]}", (50, 275, 500, 275), (50, 200))
        self.description_text2 = EditDescription((55, 300), f"{self.dm.movie_description_edit[61:122]}", (50, 275, 500, 275), (50, 200))
        self.description_text3 = EditDescription((55, 318), f"{self.dm.movie_description_edit[122:183]}", (50, 275, 500, 275), (50, 200))
        self.description_text4 = EditDescription((55, 336), f"{self.dm.movie_description_edit[183:244]}", (50, 275, 500, 275), (50, 200))
        self.description_text5 = EditDescription((55, 354), f"{self.dm.movie_description_edit[244:305]}", (50, 275, 500, 275), (50, 200))
        self.description_text6 = EditDescription((55, 372), f"{self.dm.movie_description_edit[305:366]}", (50, 275, 500, 275), (50, 200))
        self.description_text7 = EditDescription((55, 390), f"{self.dm.movie_description_edit[366:427]}", (50, 275, 500, 275), (50, 200))
        self.description_text8 = EditDescription((55, 408), f"{self.dm.movie_description_edit[427:488]}", (50, 275, 500, 275), (50, 200))
        self.description_text9 = EditDescription((55, 426), f"{self.dm.movie_description_edit[488:549]}", (50, 275, 500, 275), (50, 200))
        self.description_text10 = EditDescription((55, 444), f"{self.dm.movie_description_edit[549:610]}", (50, 275, 500, 275), (50, 200))
        self.description_text11 = EditDescription((55, 462), f"{self.dm.movie_description_edit[610:671]}", (50, 275, 500, 275), (50, 200))
        self.description_text12 = EditDescription((55, 480), f"{self.dm.movie_description_edit[671:732]}", (50, 275, 500, 275), (50, 200))
        self.description_text13 = EditDescription((55, 498), f"{self.dm.movie_description_edit[732:793]}", (50, 275, 500, 275), (50, 200))
        self.description_text14 = EditDescription((55, 516), f"{self.dm.movie_description_edit[793:854]}", (50, 275, 500, 275), (50, 200))
        self.description_text15 = EditDescription((55, 534), f"{self.dm.movie_description_edit[854:915]}", (50, 275, 500, 275), (50, 200))

        # Variable única que define si la description_tx está o no apretada
        self.description_state = False

        # Listas de los textos y textboxes
        self.texts_list = []
        self.description_list = []
        self.description_list_text = []

        for i in EditDescription.description_list_temp:
            self.description_list.append(i)

        for i in EditTexts.texts_list_temp:
            self.texts_list.append(i)

        # Índice principal para indexar los reglones de la descripción
        self.index = 0

        # Tick
        self.tick_rect = pygame.Rect(550, 550, 30, 30)
        self.tick = pygame.image.load("Images/tick.png")

        # Lista de todos los botónes de la ventana
        self.edit_buttons_list = []

        # Buttons
        self.delete_button = EditButtons((30, 650, 100, 30), "DELETE", (57, 658))
        self.to_watch_button = EditButtons((140, 650, 100, 30), "TO WATCH", (156, 658))
        self.already_seen_button = EditButtons((250, 650, 100, 30), "ALREADY SEEN", (252, 658))
        self.top_button = EditButtons((360, 650, 100, 30), "TOP", (398, 658))
        self.worst_button = EditButtons((470, 650, 100, 30), "WORST", (498, 658))
        
        for button in EditButtons.temp_list:
            self.edit_buttons_list.append(button)        

    # Función que registra los eventos de la ventana
    def events(self):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                sys.exit()
            
            # Obtiene la posición del mouse
            self.mx, self.my = pygame.mouse.get_pos()

            self.get_tx_state()
            self.write_user_mecs()
            self.tab_mechanics()
            self.enter_mechanics()
            self.esc_mechanics()
            self.get_tick()
            self.get_buttons_press()
            self.edit_buttons_SQL()

    # Función que dibuja por pantalla todo
    def draw_on_screen(self):
        self.screen.fill(GRAY)

        # Bliteo de los títulos
        self.screen.blit(self.name_title, (50, 30))
        self.screen.blit(self.date_title, (50, 105))
        self.screen.blit(self.country_title, (50, 180))
        self.screen.blit(self.genre_title, (300, 180))
        self.screen.blit(self.description_title, (50, 255))
        self.screen.blit(self.rating_title, (50, 578))

        self.change_tx_color()

        # Bliteo del texto que escribe el usuario por pantalla
        for t in self.texts_list:
            self.text_surface = self.font2.render(t.text, True, BLUE)
            self.screen.blit(self.text_surface, t.text_coords) 

        self.description_display()

        # Dibuja por pantalla el tick
        self.screen.blit(self.tick, (550, 550))

        # Dibuja por pantalla el botón de delete
        for b in self.edit_buttons_list:
            pygame.draw.rect(self.screen, b.color, b.rect, 0, 5)
            self.screen.blit(b.text, b.text_coords)

    # Cambia el color de las textboxes dependiendo si están activas o no
    def change_tx_color(self):
        for tx in self.texts_list:
            tx.change_color()

        if self.description_state == True:
            self.color_movie_description_tx = WHITE
        else:
            self.color_movie_description_tx = LIGHTGRAY

        # Esta parte de abajo cambia el color de los botones, no de las textboxes
        for b in self.edit_buttons_list:
            b.change_color()

        # Dibuja las textboxes con su color por pantalla
        for tx in self.texts_list:
            pygame.draw.rect(self.screen, tx.color, tx.tx_rect, 0, 5)
        
        pygame.draw.rect(self.screen, self.color_movie_description_tx, self.description_text.tx_rect, 0, 5)

    # Define si están activas o no las textboxes
    def get_tx_state(self):
        for tx in self.texts_list:
            if self.event.type == pygame.MOUSEBUTTONDOWN:
                if tx.tx_rect.collidepoint(self.mx, self.my):
                    tx.state = True
                else:
                    tx.state = False

                if self.description_text.tx_rect.collidepoint(self.mx, self.my):
                    self.description_state = True
                else:
                    self.description_state = False

    # Mecánicas del escape
    def esc_mechanics(self):
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_ESCAPE:
                EditTexts.texts_list_temp.clear()
                EditDescription.description_list_temp.clear()
                self.escape += 1

    # Mecánicas del enter
    def enter_mechanics(self):
        for t in self.texts_list:
            if self.event.type == pygame.KEYDOWN:
                if self.event.key == pygame.K_RETURN:
                    if t.state and len(t.text) != 0:
                        t.text = t.text[:-1]
                        
                    if self.description_state and len(self.description_list[self.index].text) != 0 and self.index < 14:
                        self.index += 1
                        self.description_list[self.index - 1].text = self.description_list[self.index - 1].text[:-1]

    # Mecánicas para registrar lo que escribe el usuario
    def write_user_mecs(self):
        if self.event.type == pygame.KEYDOWN:
            for b in self.texts_list[:2]:
                if self.event.key == pygame.K_BACKSPACE and b.state:
                    b.text = b.text[:-1]
                elif b.state and len(b.text) < 61:
                    b.text += self.event.unicode
            for d in self.texts_list[2:4]:
                if self.event.key == pygame.K_BACKSPACE and d.state:
                    d.text = d.text[:-1]
                elif d.state and len(d.text) < 61:
                    d.text += self.event.unicode
            if self.event.key == pygame.K_BACKSPACE and self.rating.state:
                self.rating.text = self.rating.text[:-1]
            elif self.rating.state and len(self.rating.text) <= 60:
                self.rating.text += self.event.unicode
            
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
                    self.description_state = True
                elif self.description_state:
                    self.description_list[self.index].text = self.description_list[self.index].text[:-1]
                    self.description_state = False
                    self.rating.state = True
                elif self.rating.state:   
                    self.rating.text = self.rating.text[:-1]
                    self.rating.state = False
                    self.name_text.state = True

    # Mecánicas de la inserción del texto del usuario en la descripción
    def description_mechanics(self):
        if self.event.key == pygame.K_BACKSPACE and self.description_state:
            self.description_list[self.index].text = self.description_list[self.index].text[:-1]
            if self.index < 14 and len(self.description_list[self.index].text) == 0 and self.index != 0:
                self.index -= 1
        elif self.description_state and len(self.description_list[self.index].text) < 61:
            self.description_list[self.index].text += self.event.unicode
        elif len(self.description_list[self.index].text) > 59 and self.index < 14 and self.description_state:
            self.description_list[self.index].state = True
            self.description_list[self.index - 1].state = False
            self.index += 1
        
    # Muestra las líneas de la descripción por pantalla
    def description_display(self): 
        for i in self.description_list:   
            self.surface = self.font2.render(i.text, True, (47, 86, 233))
            self.screen.blit(self.surface, (i.blit_coords))

    # Registra si se aprieta el tick
    def get_tick(self):
        try:
            if self.event.type == pygame.MOUSEBUTTONDOWN:
                if self.tick_rect.collidepoint(self.mx, self.my):
                    for t in self.texts_list:
                        if t.state:
                            t.text = t.text[:-1]
                        
                    if self.description_state:
                        self.description_list[self.index].text = self.description_list[self.index].text[:-1] 
                    for i in EditDescription.description_list_temp:
                        self.description_list_text.append(i.text)
                    self.dm.update_name = self.name_text.text
                    self.dm.update_date = self.date_text.text
                    self.dm.update_countryid = self.country_text.text
                    self.dm.update_genre_id = self.genre_text.text
                    self.dm.update_description = " ".join(self.description_list_text)
                    self.dm.update_rating = self.rating.text
                    self.description_list_text.clear()
                    self.dm.update_changes()
                    EditTexts.texts_list_temp.clear()
                    EditDescription.description_list_temp.clear()
                    self.escape += 1
        except DataError:
            self.dm.cn.session.rollback()

    # Registra si se aprieta un botón y en ese caso cuál
    def get_buttons_press(self):
        for b in self.edit_buttons_list:
            if b.rect.collidepoint(self.mx, self.my):
                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    b.state = True
                elif self.event.type == pygame.MOUSEBUTTONUP:
                    b.state = False
            
    # Llama a la función correspondiente para seleccionar los datos determinados de la db, dependiendo que botón se apretó
    def edit_buttons_SQL(self):
        if self.delete_button.state == True:
            self.dm.delete_movies()
            self.escape += 1
        elif self.to_watch_button.state == True:
            self.dm.assign_filter('already_seen', 'to_watch')
        elif self.already_seen_button.state == True:
            self.dm.assign_filter('to_watch', 'already_seen')
        elif self.top_button.state == True:
            self.dm.assign_filter('worst', 'top_button')
        elif self.worst_button.state == True:
            self.dm.assign_filter('top_button', 'worst')

pygame.quit()
