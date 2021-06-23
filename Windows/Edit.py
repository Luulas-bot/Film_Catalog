import pygame
import sys
from Constants.Constants import GRAY, BLUE, WHITE, LIGHTGRAY, LIGHTBLUE
from Classes.Edit_Texts import Edit_Texts, Edit_Description
from DataBase.Database_Connection import e, c
from sqlalchemy.exc import DataError, IntegrityError
from Classes.Edit_Buttons import Edit_Buttons

class Edit():

    def __init__(self, size):
        self.size = size
        self.init_stats()

    def init_stats(self):
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

        self.name_text = Edit_Texts((55, 57), f"{e.movie_name_edit}", (50, 50, 500, 30), (50, 50), (55, 57))
        self.date_text = Edit_Texts((55, 132), f"{e.movie_date_edit}", (50, 125, 500, 30), (50, 100), (55, 132))
        self.country_text = Edit_Texts ((55, 207), f"{e.movie_country_edit}", (50, 200, 200, 30), (50, 150), (55, 207))
        self.genre_text = Edit_Texts((305, 207),f"{e.movie_genre_edit}", (300, 200, 200, 30), (200, 150), (305, 207))
        self.rating = Edit_Texts((55, 607), f"{e.movie_rating_edit}", (50, 600, 500, 30), (50, 600), (55, 607))
        self.description_text = Edit_Description((55, 282), f"{e.movie_description_edit[:61]}", (50, 275, 500, 275), (50, 200))
        self.description_text2 = Edit_Description((55, 300), f"{e.movie_description_edit[61:122]}", (50, 275, 500, 275), (50, 200))
        self.description_text3 = Edit_Description((55, 318), f"{e.movie_description_edit[122:183]}", (50, 275, 500, 275), (50, 200))
        self.description_text4 = Edit_Description((55, 336), f"{e.movie_description_edit[183:244]}", (50, 275, 500, 275), (50, 200))
        self.description_text5 = Edit_Description((55, 354), f"{e.movie_description_edit[244:305]}", (50, 275, 500, 275), (50, 200))
        self.description_text6 = Edit_Description((55, 372), f"{e.movie_description_edit[305:366]}", (50, 275, 500, 275), (50, 200))
        self.description_text7 = Edit_Description((55, 390), f"{e.movie_description_edit[366:427]}", (50, 275, 500, 275), (50, 200))
        self.description_text8 = Edit_Description((55, 408), f"{e.movie_description_edit[427:488]}", (50, 275, 500, 275), (50, 200))
        self.description_text9 = Edit_Description((55, 426), f"{e.movie_description_edit[488:549]}", (50, 275, 500, 275), (50, 200))
        self.description_text10 = Edit_Description((55, 444), f"{e.movie_description_edit[549:610]}", (50, 275, 500, 275), (50, 200))
        self.description_text11 = Edit_Description((55, 462), f"{e.movie_description_edit[610:671]}", (50, 275, 500, 275), (50, 200))
        self.description_text12 = Edit_Description((55, 480), f"{e.movie_description_edit[671:732]}", (50, 275, 500, 275), (50, 200))
        self.description_text13 = Edit_Description((55, 498), f"{e.movie_description_edit[732:793]}", (50, 275, 500, 275), (50, 200))
        self.description_text14 = Edit_Description((55, 516), f"{e.movie_description_edit[793:854]}", (50, 275, 500, 275), (50, 200))
        self.description_text15 = Edit_Description((55, 534), f"{e.movie_description_edit[854:915]}", (50, 275, 500, 275), (50, 200))

        self.description_state = False

        self.texts_list = []
        self.description_list = []
        self.description_list_text = []

        for i in Edit_Description.description_list_temp:
            self.description_list.append(i)

        for i in Edit_Texts.texts_list_temp:
            self.texts_list.append(i)

        self.index = 0

        # Tick
        self.tick_rect = pygame.Rect(550, 550, 30, 30)
        self.tick = pygame.image.load("Images/tick.png")

        self.edit_buttons_list = []

        # Buttons
        self.delete_button = Edit_Buttons((30, 650, 100, 30), "DELETE", (57, 658))
        self.to_watch_button = Edit_Buttons((140, 650, 100, 30), "TO WATCH", (156, 658))
        self.already_seen_button = Edit_Buttons((250, 650, 100, 30), "ALREADY SEEN", (252, 658))
        self.top_button = Edit_Buttons((360, 650, 100, 30), "TOP", (398, 658))
        self.worst_button = Edit_Buttons((470, 650, 100, 30), "WORST", (498, 658))
        
        for button in Edit_Buttons.temp_list:
            self.edit_buttons_list.append(button)        

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

    def draw_on_screen(self):
        self.screen.fill(GRAY)

        self.screen.blit(self.name_title, (50, 30))
        self.screen.blit(self.date_title, (50, 105))
        self.screen.blit(self.country_title, (50, 180))
        self.screen.blit(self.genre_title, (300, 180))
        self.screen.blit(self.description_title, (50, 255))
        self.screen.blit(self.rating_title, (50, 578))

        self.change_tx_color()

        for t in self.texts_list:
            self.text_surface = self.font2.render(t.text, True, BLUE)
            self.screen.blit(self.text_surface, t.text_coords) 

        self.description_display()

        # Dibuja por pantalla el tick
        self.screen.blit(self.tick, (550, 550))

        # Dibuja por pantalla el boton de delete
        for b in self.edit_buttons_list:
            pygame.draw.rect(self.screen, b.color, b.rect, 0, 5)
            self.screen.blit(b.text, b.text_coords)

    def change_tx_color(self):
        for tx in self.texts_list:
            tx.change_color()

        if self.description_state == True:
            self.color_movie_description_tx = WHITE
        else:
            self.color_movie_description_tx = LIGHTGRAY

        # Esta parte de abajo cambia el color de los botones, no de ls tx
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

    def esc_mechanics(self):
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_ESCAPE:
                Edit_Texts.texts_list_temp.clear()
                Edit_Description.description_list_temp.clear()
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

    def write_user_mecs(self):
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
            if self.event.key == pygame.K_BACKSPACE and self.rating.state:
                self.rating.text = self.rating.text[:-1]
            elif self.rating.state and len(self.rating.text) <= 60:
                self.rating.text += self.event.unicode
            
            self.description_mechanics()

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

    def get_tick(self):
        try:
            if self.event.type == pygame.MOUSEBUTTONDOWN:
                if self.tick_rect.collidepoint(self.mx, self.my):
                    for t in self.texts_list:
                        if t.state:
                            t.text = t.text[:-1]
                        
                    if self.description_state:
                        self.description_list[self.index].text = self.description_list[self.index].text[:-1] 
                    for i in Edit_Description.description_list_temp:
                        self.description_list_text.append(i.text)
                    e.update_name = self.name_text.text
                    e.update_date = self.date_text.text
                    e.update_countryid = self.country_text.text
                    e.update_genre_id = self.genre_text.text
                    e.update_description = " ".join(self.description_list_text)
                    e.update_rating = self.rating.text
                    self.description_list_text.clear()
                    e.update_changes()
                    Edit_Texts.texts_list_temp.clear()
                    Edit_Description.description_list_temp.clear()
                    self.escape += 1
        except DataError:
            c.session.rollback()

    def get_buttons_press(self):
        for b in self.edit_buttons_list:
            if b.rect.collidepoint(self.mx, self.my):
                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    b.state = True
                elif self.event.type == pygame.MOUSEBUTTONUP:
                    b.state = False
            
    def edit_buttons_SQL(self):
        if self.delete_button.state == True:
            e.delete_movies()
            self.escape += 1
        elif self.to_watch_button.state == True:
            e.assign_to_watch()
        elif self.already_seen_button.state == True:
            e.assign_already_seen()
        elif self.top_button.state == True:
            e.assign_top()
        elif self.worst_button.state == True:
            e.assign_worst()
