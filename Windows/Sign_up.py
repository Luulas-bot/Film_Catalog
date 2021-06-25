# Imports
import pygame
import sys
from Constants.Constants import (
    WHITE, BLUE, GRAY, LIGHTGRAY, LIGHTBLUE
)
from DataBase.Database_Connection import c, e
from sqlalchemy.exc import IntegrityError

# Inicialización de pygame
pygame.init()

# Creación de una clase que va a ser usada posteriormente para las textboxes
class Su_Textbox():

    def __init__(self, text, rect):
        self.text = text
        self.rect = pygame.Rect(rect)
        self.state = False
        self.color = LIGHTGRAY

# Definición de la clase que es toda la ventana
class Sign_up():

    # Función constructora
    def __init__(self, size):
        self.size_sign_up = size
        self.init_stats()

    # Función que setea las variables inciales
    def init_stats(self):
       
        pygame.display.quit()
        self.screen = pygame.display.set_mode(self.size_sign_up)
        pygame.display.set_caption("Sign Up")
        
        # Fuentes y renderizados de los textos estáticos
        self.font1 = pygame.font.SysFont("consolas", 40, bold = True)
        self.font2 = pygame.font.SysFont("consolas", 30, bold = True)
        self.font4 = pygame.font.SysFont("consolas", 20, bold = True)
        self.text_box_font1 = pygame.font.SysFont("consolas", 20)
        self.text_box_font2 = pygame.font.SysFont("consolas", 20)
        self.new_user_title = self.font1.render("Crea un nuevo", True, LIGHTBLUE)
        self.new_user_title_2 = self.font1.render("usuario y contraseña", True, LIGHTBLUE)
        self.username_title = self.font2.render("Nuevo usuario", True, LIGHTBLUE)
        self.password_title = self.font2.render("Contraseña", True, LIGHTBLUE)
        self.re_password_title = self.font4.render("Re-escriba la contraseña", True, LIGHTBLUE)

        # Fuentes y textos del Sign Up correctamente con sus errores
        self.font5 = pygame.font.SysFont("consolas", 20, bold = True)
        self.font6 = pygame.font.SysFont("consolas", 17, bold = True)
        self.text1 = self.font5.render("Las contraseñas no concuerdan", True, LIGHTBLUE)
        self.text2 = self.font6.render("La contraseña debe ser mayor a 6 carácteres", True, LIGHTBLUE)
        self.text3 = self.font6.render("El campo 'Usuario' no puede estar en blanco", True, LIGHTBLUE)
        self.text4 = self.font5.render("El nombre de usuario ya está ocupado", True, LIGHTBLUE)

        # Boleanos de los errores
        self.pass_no_match = False
        self.pass_no_min = False
        self.user_no_min = False

        self.username = Su_Textbox("", (100, 170, 300, 50))
        self.password = Su_Textbox("", (100, 270, 300, 50))
        self.re_password = Su_Textbox("", (100, 370, 300, 50))

        # Variables modificables del texto entrado por el usuario
        self.hidden_password = ""
        self.re_hidden_password = ""       
        
        # Boleanos para saber si salta determinado error
        self.user_error = False

        # Variable que registra si se ha creado un usuario
        self.new_user_created = 0
        self.new_user_created_text = 0

        # Variable que registra si se sale de la ventana o no
        self.escape = 0

    # Función que registra los eventos
    def events(self):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                sys.exit()

            self.get_textbox_press()
            self.get_user_text()
            self.tab_mechanics()
            self.enter_mechanics()
            self.esc_mechanics()

    # Función que dibuja por pantalla los elementos
    def draw_on_screen(self):
        self.screen.fill(GRAY)

        self.select_draw_color_textbox()
            
        # Se dibujan por pantalla los títulos y subtítulos
        self.screen.blit(self.new_user_title, (110, 30))
        self.screen.blit(self.new_user_title_2, (30, 70))
        self.screen.blit(self.username_title, (100, 140))
        self.screen.blit(self.password_title, (100, 240))
        self.screen.blit(self.re_password_title, (100, 350))
            
        self.draw_user_text()
        self.draw_errors()

    # Condiciones que registran la si está presionado o no una textbox
    def get_textbox_press(self):
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            if self.username.rect.collidepoint(self.event.pos):
                self.username.state = True
            else:
                self.username.state = False
            if self.password.rect.collidepoint(self.event.pos):
                self.password.state = True
            else:
                self.password.state = False
            if self.re_password.rect.collidepoint(self.event.pos):
                self.password.state = True
            else:
                self.password.state = False

    # Condición que registra el enter
    def enter_mechanics(self):
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_RETURN:
                if self.username.state:
                    self.sign_up_data()
                    self.username.text = self.username.text[:-1]
                if self.password.state:
                    self.sign_up_data()
                    self.password.text = self.password.text[:-1]
                    self.hidden_password = self.hidden_password[:-1]
                elif self.re_password.state:
                    self.re_password.text = self.re_password.text[:-1]
                    self.re_hidden_password = self.re_hidden_password[:-1]
                    self.sign_up_data()

    # Escribe el teto ingresado por el usuario en una variable y maneja el bug del backspace
    def get_user_text(self):
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_BACKSPACE and self.username.state:
                self.username.text = self.username.text[:-1]
            elif self.username.state and len(self.username.text) < 26:
                self.username.text += self.event.unicode
            if self.event.key == pygame.K_BACKSPACE and self.password.state:
                self.password.text = self.password.text[:-1]
                self.hidden_password = self.hidden_password[:-1]
            elif self.password.state and len(self.password.text) < 26:
                self.password.text += self.event.unicode
                self.hidden_password += "*"
            if self.event.key == pygame.K_BACKSPACE and self.re_password.state:
                self.re_password.text = self.re_password.text[:-1]
                self.re_hidden_password = self.re_hidden_password[:-1]
            elif self.re_password.state and len(self.re_password.text) < 26:
                self.re_password.text += self.event.unicode
                self.re_hidden_password += "*"   

    # Condiciones que registran si son válidas las entradas del usuario, la contraseña y la confirmación de la contraseña
    def sign_up_data(self):
        try:
            if len(self.password.text) > 6: 
                if self.password.text == self.re_password.text:
                    if len(self.username.text) > 0:
                        e.insert_sign_up(self.username.text, self.password.text)
                        self.new_user_created += 1
                        self.new_user_created_text += 1
                        self.username.text = ""
                        self.password.text = ""
                        self.hidden_password = ""
                        self.re_password.text = ""
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
                if self.username.state:
                    self.username.text = self.username.text[:-1]
                    self.username.state = False
                    self.password.state = True
                    self.re_password.state = False
                elif self.password.state:
                    self.password.text = self.password.text[:-1]
                    self.hidden_password = self.hidden_password[:-1]
                    self.password.state = False
                    self.username.state = False
                    self.re_password.state = True
                elif self.re_password.state:
                    self.re_password.text = self.re_password.text[:-1]
                    self.re_hidden_password = self.re_hidden_password[:-1]
                    self.password.state = False
                    self.username.state = True
                    self.re_password.state = False

    # mecánicas del escape
    def esc_mechanics(self):
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_ESCAPE:
                self.escape += 1

    # Cambio del color de las textboxes dependiendo si están presionadas o no y se las diubja
    def select_draw_color_textbox(self):
        if self.username.state:
            self.username.color = WHITE
        else:
            self.username.color = LIGHTGRAY
        if self.password.state:
            self.password.color = WHITE
        else:
            self.password.color = LIGHTGRAY
        if self.re_password.state:
            self.re_password.color = WHITE
        else:
            self.re_password.color = LIGHTGRAY

        pygame.draw.rect(self.screen, self.username.color, self.username.rect, 0, 5)
        pygame.draw.rect(self.screen, self.password.color, self.password.rect, 0, 5)
        pygame.draw.rect(self.screen, self.re_password.color, self.re_password.rect, 0, 5)

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
        if len(self.username.text) >= 1:    
            text_surface1 = self.text_box_font1.render(self.username.text, True, BLUE)
            self.screen.blit(text_surface1, (107, 188))
        if len(self.password.text) >= 1:    
            text_surface2 = self.text_box_font2.render(self.hidden_password, True, BLUE)
            self.screen.blit(text_surface2, (107, 293))
        if len(self.re_password.text) >= 1:    
            text_surface3 = self.text_box_font1.render(self.re_hidden_password, True, BLUE)
            self.screen.blit(text_surface3, (107, 393))

pygame.quit()