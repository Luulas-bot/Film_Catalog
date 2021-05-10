import pygame
import sys
import pyodbc
from Files.Constants import size, WHITE, screen, clock, fps

pygame.init()

class Login():
    def init(self):
        pass

    def login(self):
        
        done = True

        while done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            screen.fill(WHITE)

            pygame.display.flip()
            clock.tick(fps)

lg = Login()
lg.login()

