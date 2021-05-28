import pygame
import sys
from Files.Constants import (
    WHITE, BLUE, GRAY, LIGHTGRAY, LIGHTBLUE, color_user_textbox, color_pass_textbox, color_re_pass_textbox
)
from Files.Database_Connection import c, e
from sqlalchemy.exc import IntegrityError

class Sign_up():

    # Función constructora
    def __init__(self, size):
        self.size_sign_up = size
        self.init_stats()

    # Función que setea las variables inciales
    def init_stats(self):
        self.screen = pygame.display.set_mode(self.size_sign_up)
        
        # Fuentes y renderizados de los textos estáticos
        font1 = pygame.font.SysFont("consolas", 40, bold = True)
        font2 = pygame.font.SysFont("consolas", 30, bold = True)
        font4 = pygame.font.SysFont("consolas", 20, bold = True)
        self.text_box_font1 = pygame.font.SysFont("consolas", 20)
        self.text_box_font2 = pygame.font.SysFont("consolas", 20)
        self.new_user_title = font1.render("Crea un nuevo", True, LIGHTBLUE)
        self.new_user_title_2 = font1.render("usuario y contraseña", True, LIGHTBLUE)
        self.username = font2.render("Nuevo usuario", True, LIGHTBLUE)
        self.password = font2.render("Contraseña", True, LIGHTBLUE)
        self.re_password = font4.render("Re-escriba la contraseña", True, LIGHTBLUE)

        # Fuentes y textos del Sign Up correctamente con sus errores
        font5 = pygame.font.SysFont("consolas", 20, bold = True)
        font6 = pygame.font.SysFont("consolas", 17, bold = True)
        self.text1 = font5.render("Las contraseñas no concuerdan", True, LIGHTBLUE)
        self.text2 = font6.render("La contraseña debe ser mayor a 6 carácteres", True, LIGHTBLUE)
        self.text3 = font6.render("El campo 'Usuario' no puede estar en blanco", True, LIGHTBLUE)
        self.text4 = font5.render("El nombre de usuario ya está ocupado", True, LIGHTBLUE)

        # Boleanos de los errores
        self.pass_no_match = False
        self.pass_no_min = False
        self.user_no_min = False

        # Variables modificables del texto entrado por el usuario
        self.username_text = ""
        self.password_text = ""
        self.hidden_password = ""
        self.re_password_text = ""
        self.re_hidden_password = ""

        # Textboxes
        self.user_text_box = pygame.Rect(100, 170, 300, 50)
        self.pass_text_box = pygame.Rect(100, 270, 300, 50)
        self.re_pass_text_box = pygame.Rect(100, 370, 300, 50)        
        
        # Boleanos para saber si las textboxes están activas o no
        self.user_textbox_active = False
        self.pass_textbox_active = False
        self.re_pass_textbox_active = False
        self.user_error = False

        # Variable que registra si se ha creado un usuario
        self.new_user_created = 0
        self.new_user_created_text = 0
    
    # Función que registra los eventos
    def events(self):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                sys.exit()

            self.get_textbox_press()
            self.get_user_text()
            self.tab_mechanics()
            self.enter_mechanics()
        

    # Función que dibuja por pantalla los elementos
    def draw_on_screen(self):
        self.screen.fill(GRAY)

        self.select_draw_color_textbox()
            
        # Se dibujan por pantalla los títulos y subtítulos
        self.screen.blit(self.new_user_title, (110, 30))
        self.screen.blit(self.new_user_title_2, (30, 70))
        self.screen.blit(self.username, (100, 140))
        self.screen.blit(self.password, (100, 240))
        self.screen.blit(self.re_password, (100, 350))
            
        self.draw_user_text()
        self.draw_errors()

    # Condiciones que registran la si está presionado o no una textbox
    def get_textbox_press(self):
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            if self.user_text_box.collidepoint(self.event.pos):
                self.user_textbox_active = True
            else:
                self.user_textbox_active = False
            if self.pass_text_box.collidepoint(self.event.pos):
                self.pass_textbox_active = True
            else:
                self.pass_textbox_active = False
            if self.re_pass_text_box.collidepoint(self.event.pos):
                self.re_pass_textbox_active = True
            else:
                self.re_pass_textbox_active = False

    # Condición que registra el enter
    def enter_mechanics(self):
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_RETURN:
                if self.user_textbox_active:
                    self.sign_up_data()
                    self.username_text = self.username_text[:-1]
                if self.pass_textbox_active:
                    self.sign_up_data()
                    self.password_text = self.password_text[:-1]
                    self.hidden_password = self.hidden_password[:-1]
                elif self.re_pass_textbox_active:
                    self.re_password_text = self.re_password_text[:-1]
                    self.re_hidden_password = self.re_hidden_password[:-1]
                    self.sign_up_data()

    # Escribe el teto ingresado por el usuario en una variable y maneja el bug del backspace
    def get_user_text(self):
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_BACKSPACE and self.user_textbox_active:
                self.username_text = self.username_text[:-1]
            elif self.user_textbox_active and len(self.username_text) < 26:
                self.username_text += self.event.unicode
            if self.event.key == pygame.K_BACKSPACE and self.pass_textbox_active:
                self.password_text = self.password_text[:-1]
                self.hidden_password = self.hidden_password[:-1]
            elif self.pass_textbox_active and len(self.password_text) < 26:
                self.password_text += self.event.unicode
                self.hidden_password += "*"
            if self.event.key == pygame.K_BACKSPACE and self.re_pass_textbox_active:
                self.re_password_text = self.re_password_text[:-1]
                self.re_hidden_password = self.re_hidden_password[:-1]
            elif self.re_pass_textbox_active and len(self.re_password_text) < 26:
                self.re_password_text += self.event.unicode
                self.re_hidden_password += "*"   

    # Condiciones que registran si son válidas las entradas del usuario, la contraseña y la confirmación de la contraseña
    def sign_up_data(self):
        try:
            if len(self.password_text) > 6: 
                if self.password_text == self.re_password_text:
                    if len(self.username_text) > 0:
                        e.insert(self.username_text, self.password_text)
                        self.new_user_created += 1
                        self.new_user_created_text += 1
                        self.username_text = ""
                        self.password_text = ""
                        self.hidden_password = ""
                        self.re_password_text = ""
                        self.re_hidden_password = ""
                            
                    else:
                        self.user_no_min = True
                        self.pass_no_min = False
                        self.pass_no_match = False
                        self.user_error = False
                else:
                    self.pass_no_match = True
                    self.pass_no_min = False
                    self.user_no_min = False
                    self.user_error = False
            else:
                self.pass_no_min = True
                self.pass_no_match = False
                self.user_no_min = False
                self.user_error = False
        except IntegrityError:
            self.pass_no_min = False
            self.pass_no_match = False
            self.user_no_min = False
            self.user_error = True
            c.session.rollback()
        
    # Mecánicas del taburador
    def tab_mechanics(self):
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_TAB:
                if self.user_textbox_active:
                    self.username_text = self.username_text[:-1]
                    self.user_textbox_active = False
                    self.pass_textbox_active = True
                    self.re_pass_textbox_active = False
                elif self.pass_textbox_active:
                    self.password_text = self.password_text[:-1]
                    self.hidden_password = self.hidden_password[:-1]
                    self.pass_textbox_active = False
                    self.user_textbox_active = False
                    self.re_pass_textbox_active = True
                elif self.re_pass_textbox_active:
                    self.re_password_text = self.re_password_text[:-1]
                    self.re_hidden_password = self.re_hidden_password[:-1]
                    self.pass_textbox_active = False
                    self.user_textbox_active = True
                    self.re_pass_textbox_active = False

    # Cambio del color de las textboxes dependiendo si están presionadas o no y se las diubja
    def select_draw_color_textbox(self):
        if self.user_textbox_active:
            color_user_textbox = WHITE
        else:
            color_user_textbox = LIGHTGRAY
        if self.pass_textbox_active:
            color_pass_textbox = WHITE
        else:
            color_pass_textbox = LIGHTGRAY
        if self.re_pass_textbox_active:
            color_re_pass_textbox = WHITE
        else:
            color_re_pass_textbox = LIGHTGRAY

        pygame.draw.rect(self.screen, color_user_textbox, self.user_text_box, 0, 5)
        pygame.draw.rect(self.screen, color_pass_textbox, self.pass_text_box, 0, 5)
        pygame.draw.rect(self.screen, color_re_pass_textbox, self.re_pass_text_box, 0, 5)

    # Dibuja los errores por pantalla
    def draw_errors(self):
        if self.pass_no_match:
            self.screen.blit(self.text1, (90, 450))
        if self.pass_no_min:
            self.screen.blit(self.text2, (60, 450))
        if self.user_no_min:
            self.screen.blit(self.text3, (60, 450))
        if self.user_error:
            self.screen.blit(self.text4, (60, 450))

    # Se dibuja por pantalla las teclas que presiona el usuario
    def draw_user_text(self):
        if len(self.username_text) >= 1:    
            text_surface1 = self.text_box_font1.render(self.username_text, True, BLUE)
            self.screen.blit(text_surface1, (107, 188))
        if len(self.password_text) >= 1:    
            text_surface2 = self.text_box_font2.render(self.hidden_password, True, BLUE)
            self.screen.blit(text_surface2, (107, 293))
        if len(self.re_password_text) >= 1:    
            text_surface3 = self.text_box_font1.render(self.re_hidden_password, True, BLUE)
            self.screen.blit(text_surface3, (107, 393))