import numpy as np
import pygame
import sys


pygame.init()

#dimensiuni
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Joc de BlackJack")
font=pygame.font.SysFont("Arial", 30)
#dimensiuni


# Culori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
# Culori

imagine_fundal = pygame.image.load("imagine.png")
imagine_fundal = pygame.transform.scale(imagine_fundal, (screen_width, screen_height))


def mesaj(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))
def buton(x, y, width, height, color, text, text_color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    mesaj(text, text_color, x + 10, y + 10)
def verificare(px, py, rect_x, rect_y, rect_width, rect_height):
    return rect_x <= px <= rect_x + rect_width and rect_y <= py <= rect_y + rect_height
def IncepeJocul():
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("BlackJack")

    running_new = True
    while running_new:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_new = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if verificare(mouse_x, mouse_y, 850, 50, 98, 50):
                    pygame.quit()
                    sys.exit()
                elif verificare(mouse_x, mouse_y, 850, 275, 98, 50):
                    print("Jocul incepe")
                elif verificare(mouse_x, mouse_y, 640, 450, 98, 50):
                    print("HIT")
                elif verificare(mouse_x, mouse_y, 270, 450, 98, 50):
                    print("STAND")
                elif verificare(mouse_x, mouse_y, 445, 450, 98, 50):
                    print("DOUBLE")



        screen.blit(imagine_fundal, (0, 0))


        buton(850, 50, 98, 50, RED, "IESIRE", BLACK)
        buton(850,275,98,50,GREEN,"START",BLACK)
        buton(640, 450, 98, 50, GRAY, "   HIT", BLACK)
        buton(270,450,98,50,GRAY,"STAND",BLACK)
        buton(445,450,120,50,GRAY,"DOUBLE",BLACK)
        mesaj("DEALER", BLACK, 450, 50)
        mesaj("CARTILE MELE", BLACK, 415, 500)

        pygame.display.flip()

    # Revenire fereastra initiala
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("BlackJack")


#meniu
def meniu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if verificare(mouse_x, mouse_y, 450, 250, 200, 50):
                    IncepeJocul()


                elif verificare(mouse_x, mouse_y, 450, 350, 200, 50):
                    pygame.quit()
                    sys.exit()

        screen.blit(imagine_fundal, (0, 0))

        mesaj("BlackJack", BLACK, 450, 50)
        mesaj("Alege o opțiune:", BLACK, 400, 190)
        buton(450, 250, 200, 50, GREEN, "Incepe jocul", BLACK)
        buton(450, 350, 200, 50, RED, "Inchide jocul", BLACK)

        pygame.display.flip()



meniu()