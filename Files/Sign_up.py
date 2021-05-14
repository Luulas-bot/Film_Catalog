import pygame
import sys
from Files.Constants import WHITE, BLUE, GRAY, LIGHTGRAY, color_re_pass_textbox

class Sign_up():

    def __init__(self, size):
        self.size_sign_up = size
        self.init_stats()

    def init_stats(self):
        self.screen = pygame.display.set_mode(self.size_sign_up)
        
        # Fuentes y renderizados de los textos estáticos
        font1 = pygame.font.SysFont("consolas", 40, bold = True)
        font3 = pygame.font.SysFont("consolas", 40, bold = True)
        font2 = pygame.font.SysFont("consolas", 30, bold = True)
        font4 = pygame.font.SysFont("consolas", 20, bold = True)
        self.text_box_font1 = pygame.font.SysFont("consolas", 20)
        self.text_box_font2 = pygame.font.SysFont("consolas", 20)
        self.new_user_title = font1.render("Crea un nuevo", True, BLUE)
        self.new_user_title_2 = font1.render("usuario y contraseña", True, BLUE)
        self.username = font2.render("Nuevo usuario", True, BLUE)
        self.password = font2.render("Contraseña", True, BLUE)
        self.re_password = font4.render("Re-escriba la contraseña", True, BLUE)
        
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
    
    def events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # Condiciones que registran la si está presionado o no una textbox
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.user_text_box.collidepoint(event.pos):
                        self.user_textbox_active = True
                    else:
                        self.user_textbox_active = False  
                    if self.pass_text_box.collidepoint(event.pos):
                        self.pass_textbox_active = True
                    else:
                        self.pass_textbox_active = False 
                    if self.re_pass_text_box.collidepoint(event.pos):
                        self.re_pass_textbox_active = True
                    else:
                        self.re_pass_textbox_active = False

                # Condiciones que registran lo que presiona el usuario y lo guardan en las variables.
                if self.user_textbox_active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            self.username_text = self.username_text[:-1]
                        elif len(self.username_text) < 26:
                            self.username_text += event.unicode
                if self.pass_textbox_active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            self.password_text = self.password_text[:-1]
                        elif len(self.password_text) < 26:
                            self.password_text += event.unicode
                if self.pass_textbox_active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            self.hidden_password = self.hidden_password[:-1]
                        elif len(self.hidden_password) < 26:
                            self.hidden_password += "*"
                if self.re_pass_textbox_active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            self.re_password_text = self.re_password_text[:-1]
                        elif len(self.re_password_text) < 26:
                            self.re_password_text += event.unicode
                if self.re_pass_textbox_active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            self.re_hidden_password = self.re_hidden_password[:-1]
                        elif len(self.re_hidden_password) < 26:
                            self.re_hidden_password += "*"

    def draw_on_screen(self):
        self.screen.fill(WHITE)
            
        # Cambio del color de las textboxes dependiendo si están presionadas o no
        if self.user_textbox_active:
            color_user_textbox = GRAY
        else:
            color_user_textbox = LIGHTGRAY
        if self.pass_textbox_active:
            color_pass_textbox = GRAY
        else:
            color_pass_textbox = LIGHTGRAY
        if self.re_pass_textbox_active:
            color_re_pass_textbox = GRAY
        else:
            color_re_pass_textbox = LIGHTGRAY

        # Se dibujan por pantalla las textboxes
        pygame.draw.rect(self.screen, color_user_textbox, self.user_text_box)
        pygame.draw.rect(self.screen, color_pass_textbox, self.pass_text_box)
        pygame.draw.rect(self.screen, color_re_pass_textbox, self.re_pass_text_box)
            
        # Se dibujan por pantalla los títulos y subtítulos
        self.screen.blit(self.new_user_title, (110, 30))
        self.screen.blit(self.new_user_title_2, (30, 70))
        self.screen.blit(self.username, (100, 140))
        self.screen.blit(self.password, (100, 240))
        self.screen.blit(self.re_password, (100, 350))
            
        # Se dibuja por pantalla las teclas que presiona el usuario
        text_surface1 = self.text_box_font1.render(self.username_text, True, BLUE)
        self.screen.blit(text_surface1, (107, 188))
        text_surface2 = self.text_box_font2.render(self.hidden_password, True, BLUE)
        self.screen.blit(text_surface2, (107, 293))
        text_surface3 = self.text_box_font1.render(self.re_hidden_password, True, BLUE)
        self.screen.blit(text_surface3, (107, 393))
 
