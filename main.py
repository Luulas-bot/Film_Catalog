# Imports
import pygame
import sys
from Constants.Constants import (
    LIGHTBLUE, size_login, WHITE, clock, fps, BLUE, GRAY, LIGHTGRAY, size_sign_up, size_main_menu
)
from Windows.Sign_up import Sign_up
from Windows.main_menu import Main_menu
from DataBase.Database_Connection import c, e

# Inicialización de pygame
pygame.init()

# Clase de la pantalla de Login
class Login():
    
    def __init__(self, size):
        self.size = size
    
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
        self.bienvenido = self.font1.render("Bienvenido", True, LIGHTBLUE)
        self.username = self.font2.render("Usuario", True, LIGHTBLUE)
        self.password = self.font2.render("Contraseña", True, LIGHTBLUE)
        self.new_user = self.font3.render("¿No tienes un usuario todavia?", True, LIGHTBLUE)
        self.sign_up_corr = self.font4.render("El usuario se ha creado correctamente", True, LIGHTBLUE)
        self.wrong_user_text = self.font4.render("El usuario o la contraseña son incorrectos", True, LIGHTBLUE)
        
        # Variables modificables del texto entrado por el usuario
        self.username_text = ""
        self.password_text = ""
        self.hidden_password = ""

        # Textboxes
        self.user_text_box = pygame.Rect(100, 200, 300, 50)
        self.pass_text_box = pygame.Rect(100, 320, 300, 50)
        self.new_user_hitbox = pygame.Rect(250, 480, 250, 30)
        
        # Boleanos para saber si las textboxes están activas o no
        self.user_textbox_active = False
        self.pass_textbox_active = False

        # Boleanos para manejar los mensajes al usuario
        self.sign_up_corr_bol = False
        self.wrong_user = False

        # Colores de las Textboxes
        self.color_user_textbox = LIGHTGRAY
        self.color_pass_textbox = LIGHTGRAY

    # Dibuja por pantalla los elementos que se quieren
    def draw_on_screen(self):
        self.screen.fill(GRAY)
            
        self.select_draw_color_textbox()
            
        # Se dibujan por pantalla los títulos y subtítulos
        self.screen.blit(self.bienvenido, (60, 50))
        self.screen.blit(self.username, (100, 170))
        self.screen.blit(self.password, (100, 290))
        self.screen.blit(self.new_user, (250, 480))
            
        # Se dibuja por pantalla las teclas que presiona el usuario
        text_surface1 = self.text_box_font1.render(self.username_text, True, BLUE)
        self.screen.blit(text_surface1, (107, 218))
        text_surface2 = self.text_box_font2.render(self.hidden_password, True, BLUE)
        self.screen.blit(text_surface2, (107, 338))

        # Se dibuja por pantalla que se ha creado un nuevo usuario
        if su.new_user_created_text >= 1:
            if self.sign_up_corr_bol:
                self.screen.blit(self.sign_up_corr, (50, 410))
        
        # Se dibuja por pantalla si el usuario o las contraseñas son incorrectas
        if self.wrong_user:
            self.screen.blit(self.wrong_user_text, (25, 410))
    
    # Mecánicas del enter
    def enter_mechanics(self):
        try:
            if self.event.type == pygame.KEYDOWN:
                if self.event.key == pygame.K_RETURN:
                    if self.pass_textbox_active:
                        self.password_text = self.password_text[:-1]
                        self.hidden_password = self.hidden_password[:-1]
                    if self.user_textbox_active:
                        self.username_text = self.username_text[:-1]
                    e.select_login(self.username_text, self.password_text)
                    if str(self.username_text) == str(e.user_sl[0]):
                        self.done = False
                        return self.run_main_menu()
        except IndexError:
            self.sign_up_corr_bol = False
            self.wrong_user = True

    # Mecánicas del taburador
    def tab_mechanics(self):
        if self.user_textbox_active:
            if self.event.type == pygame.KEYDOWN:
                if self.event.key == pygame.K_TAB:
                    self.username_text = self.username_text[:-1]
                    self.user_textbox_active = False
                    self.pass_textbox_active = True
        elif self.pass_textbox_active:
            if self.event.type == pygame.KEYDOWN:
                if self.event.key == pygame.K_TAB:
                    self.hidden_password = self.hidden_password[:-1]
                    self.pass_textbox_active = False
                    self.user_textbox_active = True

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
        if self.event.type == pygame.MOUSEBUTTONUP:
            if self.new_user_hitbox.collidepoint(self.event.pos): 
                self.done = False
                return self.run_sign_up()
    
    # Función que registra lo que el usuario escribe y lo guarda en una variable
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

    # Cambia y dibuja el color de las textboxes dependiendo si están activas o no
    def select_draw_color_textbox(self):
        if self.user_textbox_active:
            self.color_user_textbox = WHITE
        else:
            self.color_user_textbox = LIGHTGRAY
        if self.pass_textbox_active:
            self.color_pass_textbox = WHITE
        else:
            self.color_pass_textbox = LIGHTGRAY

        pygame.draw.rect(self.screen, self.color_user_textbox, self.user_text_box, 0, 5)
        pygame.draw.rect(self.screen, self.color_pass_textbox, self.pass_text_box, 0, 5)

    # Corre el loop para generar la ventana del menú principal
    def run_main_menu(self):
        bol_main_menu = True   

        m = Main_menu(size_main_menu)
        for i in [self.font1, self.font2, self.font3, self.font4, self.text_box_font1, self.text_box_font2]:
            del i    
        while bol_main_menu:
            m.events()
            m.draw_on_screen()
            
            pygame.display.flip()
            clock.tick(fps)
            

    # Corre el loop para generar la ventana de Sign Up
    def run_sign_up(self):
        bol_sign_up = True   

        su = Sign_up(size_sign_up)
        for i in [self.font1, self.font2, self.font3, self.font4, self.text_box_font1, self.text_box_font2]:
            del i    

        while bol_sign_up:
            su.events()
            su.draw_on_screen() 

            # Condición para la creación de una nueva ventana de Login luego el Sign Up
            if su.new_user_created >= 1:
                su.new_user_created -= 1
                lg.sign_up_corr_bol = True
                lg.wrong_user = False
                lg.username_text = ""
                lg.password_text = ""
                lg.hidden_password = ""
                lg.run_login()
                for i in [su.font1, su.font2, su.font4, su.font5, su.font6, su.text_box_font2, su.text_box_font1]:
                    del i
                break
            
            # Condición para retornar al menú de login
            if su.escape == 1:
                su.escape -= 1
                lg.username_text = ""
                lg.password_text = ""
                lg.hidden_password = ""
                lg.sign_up_corr_bol = False
                lg.wrong_user = False
                lg.run_login()
                for i in [su.font1, su.font2, su.font4, su.font5, su.font6, su.text_box_font2, su.text_box_font1]:
                    del i
                break

            pygame.display.flip()
            clock.tick(fps)

su = Sign_up(size_sign_up)

lg = Login(size_login)
lg.run_login()

pygame.quit()

