# Imports
import pygame
import sys
from Constants.constants import LIGHTBLUE, size_login, WHITE, clock, fps, BLUE, GRAY, LIGHTGRAY, size_sign_up, size_main_menu
from SmallWindows import SignUp
from MainWindow import MainMenu
from Database_manager import dm

# Inicialización de pygame
pygame.init()

# Clase de la pantalla de Login
class Login():
    
    # Función constructora
    def __init__(self, size, db_manager):
        self.size = size
        self.dm = db_manager

    # Función que corre la pantalla del login
    def run_login(self):
        self.done = True
        
        self.init_stats()

        # Bucle principal
        while self.done:
            lg.events()
            lg.draw_on_screen()

            pygame.display.flip()
            clock.tick(fps)
   
    # Función que registra los eventos
    def events(self):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                sys.exit()

            self.get_textbox_press()               
            self.get_user_text()
            self.tab_mechanics()
            self.enter_mechanics()
    
    # Función que determina las variables iniciales
    def init_stats(self):
        
        # Creación de la variable de la clase Sign-Up
        self.su = SignUp(size_sign_up, self.dm)

        pygame.display.quit()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Login")

        # Fuentes y renderizados de los textos estáticos
        self.font1 = pygame.font.SysFont("consolas", 70, bold = True)
        self.font2 = pygame.font.SysFont("consolas", 30, bold = True)
        self.font3 = pygame.font.SysFont("consolas", 15, bold = True)
        self.font4 = pygame.font.SysFont("consolas", 20, bold = True)
        self.text_box_font1 = pygame.font.SysFont("consolas", 20)
        self.text_box_font2 = pygame.font.SysFont("consolas", 20)
        self.bienvenido_title = self.font1.render("Bienvenido", True, LIGHTBLUE)
        self.username_title = self.font2.render("Usuario", True, LIGHTBLUE)
        self.password_title = self.font2.render("Contraseña", True, LIGHTBLUE)
        self.new_user_title = self.font3.render("¿No tienes un usuario todavia?", True, LIGHTBLUE)
        self.signup_verified_title = self.font4.render("El usuario se ha creado correctamente", True, LIGHTBLUE)
        self.wrong_user_error = self.font4.render("El usuario o la contraseña son incorrectos", True, LIGHTBLUE)
        
        # Variables modificables del texto entrado por el usuario
        self.username_text = ""
        self.password_text = ""
        self.hidden_password = ""

        # Textboxes
        self.user_textbox_rect = pygame.Rect(100, 200, 300, 50)
        self.pass_textbox_rect = pygame.Rect(100, 320, 300, 50)
        self.new_user_hitbox = pygame.Rect(250, 480, 250, 30)
        
        # Boleanos para saber si las textboxes están activas o no
        self.user_textbox_bol = False
        self.pass_textbox_bol = False

        # Boleanos para manejar los mensajes al usuario
        self.signup_verified = False
        self.wrong_user_bol = False

        # Colores de las Textboxes
        self.color_user_textbox = LIGHTGRAY
        self.color_pass_textbox = LIGHTGRAY

    # Dibuja por pantalla los elementos que se quieren
    def draw_on_screen(self):
        self.screen.fill(GRAY)
            
        self.change_color_textbox()

        # Se dibujan por pantalla las textboxes
        pygame.draw.rect(self.screen, self.color_user_textbox, self.user_textbox_rect, 0, 5)
        pygame.draw.rect(self.screen, self.color_pass_textbox, self.pass_textbox_rect, 0, 5)
            
        # Se dibujan por pantalla los títulos y subtítulos
        self.screen.blit(self.bienvenido_title, (60, 50))
        self.screen.blit(self.username_title, (100, 170))
        self.screen.blit(self.password_title, (100, 290))
        self.screen.blit(self.new_user_title, (250, 480))
            
        # Se dibuja por pantalla las teclas que presiona el usuario
        self.username_surface = self.text_box_font1.render(self.username_text, True, BLUE)
        self.screen.blit(self.username_surface, (107, 218))
        self.password_surface = self.text_box_font2.render(self.hidden_password, True, BLUE)
        self.screen.blit(self.password_surface, (107, 338))

        # Se dibuja por pantalla que se ha creado un nuevo usuario
        if self.su.new_user_created >= 1:
            if self.signup_verified:
                self.screen.blit(self.signup_verified_title, (50, 410))
        
        # Se dibuja por pantalla si el usuario o las contraseñas son incorrectas
        if self.wrong_user_bol:
            self.screen.blit(self.wrong_user_error, (25, 410))
    
    # Mecánicas del enter
    def enter_mechanics(self):
        try:
            if self.event.type == pygame.KEYDOWN:
                if self.event.key == pygame.K_RETURN:
                    if self.pass_textbox_bol:
                        self.password_text = self.password_text[:-1]
                        self.hidden_password = self.hidden_password[:-1]
                    if self.user_textbox_bol:
                        self.username_text = self.username_text[:-1]
                    self.dm.select_login(self.username_text, self.password_text)
                    if str(self.username_text) == str(self.dm.user_sl[0]):
                        self.done = False
                        return self.run_main_menu()
        except IndexError:
            self.signup_verified = False
            self.wrong_user_bol = True

    # Mecánicas del taburador
    def tab_mechanics(self):
        if self.user_textbox_bol:
            if self.event.type == pygame.KEYDOWN:
                if self.event.key == pygame.K_TAB:
                    self.username_text = self.username_text[:-1]
                    self.user_textbox_bol = False
                    self.pass_textbox_bol = True
        elif self.pass_textbox_bol:
            if self.event.type == pygame.KEYDOWN:
                if self.event.key == pygame.K_TAB:
                    self.hidden_password = self.hidden_password[:-1]
                    self.pass_textbox_bol = False
                    self.user_textbox_bol = True

    # Condiciones que registran si está presionado o no una textbox
    def get_textbox_press(self):
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            if self.user_textbox_rect.collidepoint(self.event.pos):
                self.user_textbox_bol = True
            else:
                self.user_textbox_bol = False  
            if self.pass_textbox_rect.collidepoint(self.event.pos):
                self.pass_textbox_bol = True
            else:
                self.pass_textbox_bol = False
        if self.event.type == pygame.MOUSEBUTTONUP:
            if self.new_user_hitbox.collidepoint(self.event.pos): 
                self.done = False
                return self.run_sign_up()
    
    # Función que registra lo que el usuario escribe y lo guarda en una variable
    def get_user_text(self):
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_BACKSPACE and self.user_textbox_bol:
                self.username_text = self.username_text[:-1]
            elif self.user_textbox_bol and len(self.username_text) < 26:
                self.username_text += self.event.unicode
            if self.event.key == pygame.K_BACKSPACE and self.pass_textbox_bol:
                self.password_text = self.password_text[:-1]
                self.hidden_password = self.hidden_password[:-1]
            elif self.pass_textbox_bol and len(self.password_text) < 26:
                self.password_text += self.event.unicode
                self.hidden_password += "*"

    # Cambia el color de las textboxes dependiendo si están activas o no
    def change_color_textbox(self):
        if self.user_textbox_bol:
            self.color_user_textbox = WHITE
        else:
            self.color_user_textbox = LIGHTGRAY
        if self.pass_textbox_bol:
            self.color_pass_textbox = WHITE
        else:
            self.color_pass_textbox = LIGHTGRAY

    # Corre el loop para generar la ventana del menú principal
    def run_main_menu(self):
        bol_main_menu = True   

        self.mm = MainMenu(size_main_menu)

        while bol_main_menu:
            self.mm.events()
            self.mm.draw_on_screen()
            
            pygame.display.flip()
            clock.tick(fps)
            

    # Corre el loop para generar la ventana de Sign Up
    def run_sign_up(self):
        bol_sign_up = True   

        self.su = SignUp(size_sign_up, dm)

        while bol_sign_up:
            self.su.events()
            self.su.draw_on_screen() 

            # Condición para la creación de una nueva ventana de Login luego el Sign Up
            if self.su.new_user_created >= 1:
                self.su.new_user_created -= 1
                lg.signup_verified = True
                lg.wrong_user_error = False
                lg.username_text = ""
                lg.password_text = ""
                lg.hidden_password = ""
                lg.run_login()
                break
            
            # Condición para retornar al menú de login
            if self.su.escape == 1:
                self.su.escape -= 1
                lg.username_text = ""
                lg.password_text = ""
                lg.hidden_password = ""
                lg.signup_verified = False
                lg.wrong_user_error = False
                lg.run_login()
                break

            pygame.display.flip()
            clock.tick(fps)

lg = Login(size_login, dm)
lg.run_login()

pygame.quit()

