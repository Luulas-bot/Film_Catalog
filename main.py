# Imports
import pygame
import sys
import pyodbc
from Files.Constants import size_login, WHITE, clock, fps, BLUE, GREY, LIGHTGREY, color_user_textbox, color_pass_textbox

# Inicialización de pygame
pygame.init()

# Clase de la pantalla de Login
class Login():
    
    def __init__(self, size):
        self.size = size
    
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

                # Condiciones que registran lo que presiona el usuario y lo guardan en las variables.
                if self.user_textbox_active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            self.username_text = self.username_text[:-1]
                        elif len(self.username_text) < 17:
                            self.username_text += event.unicode
                if self.pass_textbox_active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            self.password_text = self.password_text[:-1]
                        elif len(self.password_text) < 17:
                            self.password_text += event.unicode
                if self.pass_textbox_active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            self.hidden_password = self.hidden_password[:-1]
                        elif len(self.hidden_password) < 17:
                            self.hidden_password += "*"
                
    # Función principal del login
    def init_stats(self):
        self.screen = pygame.display.set_mode(self.size)
        
        # Fuentes y renderizados de los textos estáticos
        font1 = pygame.font.SysFont("consolas", 70, bold = True)
        font2 = pygame.font.SysFont("consolas", 30, bold = True)
        font3 = pygame.font.SysFont("consolas", 30, bold = True)
        self.text_box_font1 = pygame.font.SysFont("consolas", 20)
        self.text_box_font2 = pygame.font.SysFont("consolas", 20)
        self.bienvenido = font1.render("Bienvenido", True, BLUE)
        self.username = font2.render("Username", True, BLUE)
        self.password = font2.render("Password", True, BLUE)
        
        # Variables modificables del texto entrado por el usuario
        self.username_text = ""
        self.password_text = ""
        self.hidden_password = ""

        # Textboxes
        self.user_text_box = pygame.Rect(150, 200, 200, 50)
        self.pass_text_box = pygame.Rect(150, 320, 200, 50)
        
        # Boleanos para saber si las textboxes están activas o no
        self.user_textbox_active = False
        self.pass_textbox_active = False

    def draw_on_screen(self):
        self.screen.fill(WHITE)
            
        # Cambio del color de las textboxes dependiendo si están presionadas o no
        if self.user_textbox_active:
            color_user_textbox = GREY
        else:
            color_user_textbox = LIGHTGREY
        if self.pass_textbox_active:
            color_pass_textbox = GREY
        else:
            color_pass_textbox = LIGHTGREY

        # Se dibujan por pantalla las textboxes
        pygame.draw.rect(self.screen, color_user_textbox, self.user_text_box)
        pygame.draw.rect(self.screen, color_pass_textbox, self.pass_text_box)
            
        # Se dibujan por pantalla los títulos y subtítulos
        self.screen.blit(self.bienvenido, (60, 50))
        self.screen.blit(self.username, (150, 170))
        self.screen.blit(self.password, (150, 290))
            
        # Se dibuja por pantalla las teclas que presiona el usuario
        text_surface1 = self.text_box_font1.render(self.username_text, True, BLUE)
        self.screen.blit(text_surface1, (157, 218))
        text_surface2 = self.text_box_font2.render(self.hidden_password, True, BLUE)
        self.screen.blit(text_surface2, (157, 338))

# Creacion de un objeto de la clase y definicion de las variables
lg = Login(size_login)
lg.init_stats()
done = True

# Bucle principal
while done:
     lg.events()
     lg.draw_on_screen()

     pygame.display.flip()
     clock.tick(fps)


