import pygame
import sys
import random


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
def creearePchet():
    simboluri = ['♠', '♥', '♦', '♣']  # Folosește nume complete
    valori = ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A']
    pachet = [f"{valoare}_of_{simbol}" for valoare in valori for simbol in simboluri]
    random.shuffle(pachet)
    return pachet
def valoareCarti(carte):
    if carte in ['J','Q','K']:
        return 10
    elif carte=='A':
        return 11
    else:
        return int(carte)
def calculeazaScor(mana):
    scor = 0
    numar_asi = 0

    for carte in mana:
        value = carte.split('_of_')[0]
        if value == 'A':
            numar_asi += 1
        scor += valoareCarti(value)

    while scor > 21 and numar_asi > 0:
        scor -= 10
        numar_asi -= 1

    return scor
def deseneazaCarteJucator(x, y, valoare, simbol):
    pygame.draw.rect(screen, WHITE, (x, y, 70, 100))
    pygame.draw.rect(screen, BLACK, (x, y, 70, 100), 2)

    culoare = RED if simbol in ['♥', '♦'] else BLACK
    mesaj(valoare, culoare, x + 10, y + 10)
    mesaj(simbol[0].upper(), culoare, x + 10, y + 40)
def deseneazaCarteDealer(x, y, valoare, simbol):
    pygame.draw.rect(screen, WHITE, (x, y, 70, 100))
    pygame.draw.rect(screen, BLACK, (x, y, 70, 100), 2)

    culoare = RED if simbol in ['♥', '♦'] else BLACK
    mesaj(valoare, culoare, x + 43, y + 10)
    mesaj(simbol[0].upper(), culoare, x + 44, y + 40)
def deseneazaCarteIntorsa(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, 70, 100))
    pygame.draw.rect(screen, BLACK, (x, y, 70, 100), 2)
    mesaj("?", BLACK, x + 25, y + 40)
def mana(jucator, dealer, carte_dealer=False):
    if len(dealer) > 0:
        valoare, simbol = dealer[0].split('_of_')
        deseneazaCarteDealer(600, 170, valoare, simbol)
    if len(dealer) > 1:
        if carte_dealer:
            valoare, simbol = dealer[1].split('_of_')
            deseneazaCarteDealer(560, 170, valoare, simbol)
        else:
            deseneazaCarteIntorsa(560, 170)
    if len(dealer) > 2:
        valoare, simbol = dealer[2].split('_of_')
        deseneazaCarteDealer(520, 170, valoare, simbol)
    if len(dealer) > 3:
        valoare, simbol = dealer[3].split('_of_')
        deseneazaCarteDealer(480, 170, valoare, simbol)
    if len(dealer) > 4:
        valoare, simbol = dealer[4].split('_of_')
        deseneazaCarteDealer(440, 170, valoare, simbol)
    if len(dealer) > 5:
        valoare, simbol = dealer[5].split('_of_')
        deseneazaCarteDealer(400, 170, valoare, simbol)
    if len(dealer) > 6:
        valoare, simbol = dealer[6].split('_of_')
        deseneazaCarteDealer(360, 170, valoare, simbol)
    if len(dealer) > 7:
        valoare, simbol = dealer[7].split('_of_')
        deseneazaCarteDealer(320, 170, valoare, simbol)

    if len(jucator) > 0:
        valoare, simbol = jucator[0].split('_of_')
        deseneazaCarteJucator(340, 330, valoare, simbol)
    if len(jucator) > 1:
        valoare, simbol = jucator[1].split('_of_')
        deseneazaCarteJucator(380, 330, valoare, simbol)
    if len(jucator) > 2:
        valoare, simbol = jucator[2].split('_of_')
        deseneazaCarteJucator(420, 330, valoare, simbol)
    if len(jucator) > 3:
        valoare, simbol = jucator[3].split('_of_')
        deseneazaCarteJucator(460, 330, valoare, simbol)
    if len(jucator) > 4:
        valoare, simbol = jucator[4].split('_of_')
        deseneazaCarteJucator(500, 330, valoare, simbol)
    if len(jucator) > 5:
        valoare, simbol = jucator[5].split('_of_')
        deseneazaCarteJucator(540, 330, valoare, simbol)
    if len(jucator) > 6:
        valoare, simbol = jucator[6].split('_of_')
        deseneazaCarteJucator(580, 330, valoare, simbol)
    if len(jucator) > 7:
        valoare, simbol = jucator[7].split('_of_')
        deseneazaCarteJucator(640, 330, valoare, simbol)

#meniuJoc
def IncepeJocul():
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("BlackJack")

    pachet = creearePchet()
    mana_jucator = []
    mana_dealer = []

    mana_jucator.append(pachet.pop())
    mana_dealer.append(pachet.pop())
    mana_jucator.append(pachet.pop())
    mana_dealer.append(pachet.pop())

    running_new = True
    carte_dealer = False
    double_apasat=False

    while running_new:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_new = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if verificare(mouse_x, mouse_y, 850, 50, 98, 50):
                    meniu()
                elif verificare(mouse_x, mouse_y, 640, 450, 98, 50):  # HIT - merge perfect
                    mana_jucator.append(pachet.pop())
                    scor_jucator = calculeazaScor(mana_jucator)
                    #actualizare ecran
                    screen.blit(imagine_fundal, (0, 0))
                    buton(850, 50, 98, 50, RED, "IESIRE", BLACK)
                    buton(640, 450, 98, 50, GRAY, "   HIT", BLACK)
                    buton(270, 450, 98, 50, GRAY, "STAND", BLACK)
                    buton(445, 450, 120, 50, GRAY, "DOUBLE", BLACK)
                    mesaj("DEALER", BLACK, 450, 50)
                    mesaj("CARTILE MELE", BLACK, 415, 500)
                    mana(mana_jucator, mana_dealer, carte_dealer)
                    mesaj(f"Scor: {calculeazaScor(mana_jucator)}", BLACK, 460, 540)
                    mesaj(f"Scor Dealer: {calculeazaScor(mana_dealer[:1]) if not carte_dealer else calculeazaScor(mana_dealer)}", BLACK, 420, 90)
                    pygame.display.flip()
                    #
                    pygame.time.delay(700)
                    if scor_jucator > 21:
                        mesaj("Bust! Ai depășit 21.", RED, 430, 280)
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        running_new = False
                elif verificare(mouse_x, mouse_y, 270, 450, 98, 50):  # STAND
                    carte_dealer = True
                    scor_dealer = calculeazaScor(mana_dealer)
                    while scor_dealer < 17:

                        mana_dealer.append(pachet.pop())
                        scor_dealer = calculeazaScor(mana_dealer)

                        #actualizare ecran
                        screen.blit(imagine_fundal, (0, 0))
                        buton(850, 50, 98, 50, RED, "IESIRE", BLACK)
                        buton(640, 450, 98, 50, GRAY, "   HIT", BLACK)
                        buton(270, 450, 98, 50, GRAY, "STAND", BLACK)
                        buton(445, 450, 120, 50, GRAY, "DOUBLE", BLACK)
                        mesaj("DEALER", BLACK, 450, 50)
                        mesaj("CARTILE MELE", BLACK, 415, 500)
                        mana(mana_jucator, mana_dealer, carte_dealer)
                        mesaj(f"Scor: {calculeazaScor(mana_jucator)}", BLACK, 460, 540)
                        mesaj(f"Scor Dealer: {calculeazaScor(mana_dealer)}", BLACK, 420, 90)
                        pygame.display.flip()
                        pygame.time.delay(1000)
                        #


                    scor_jucator = calculeazaScor(mana_jucator)
                    if scor_dealer > 21 or scor_jucator > scor_dealer:
                        mesaj("Ai câștigat!", GREEN, 430, 280)
                    elif scor_jucator == scor_dealer:
                        mesaj("Egalitate!", GRAY, 430, 280)
                    else:
                        mesaj("Dealerul câștigă!", RED, 430, 280)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    running_new = False
                elif verificare(mouse_x, mouse_y, 445, 450, 120, 50) and not double_apasat: # DOUBLE-merge perfect
                    double_apasat=True
                    carte_dealer=True
                    mana_jucator.append(pachet.pop())
                    scor_jucator = calculeazaScor(mana_jucator)
                    scor_dealer = calculeazaScor(mana_dealer)
                    # actualizare ecran
                    screen.blit(imagine_fundal, (0, 0))
                    buton(850, 50, 98, 50, RED, "IESIRE", BLACK)
                    buton(640, 450, 98, 50, GRAY, "   HIT", BLACK)
                    buton(270, 450, 98, 50, GRAY, "STAND", BLACK)
                    buton(445, 450, 120, 50, GRAY, "DOUBLE", BLACK)
                    mesaj("DEALER", BLACK, 450, 50)
                    mesaj("CARTILE MELE", BLACK, 415, 500)
                    mana(mana_jucator, mana_dealer, carte_dealer)
                    mesaj(f"Scor: {calculeazaScor(mana_jucator)}", BLACK, 460, 540)
                    mesaj(f"Scor Dealer: {calculeazaScor(mana_dealer)}", BLACK, 420, 90)
                    pygame.display.flip()
                    #
                    pygame.time.delay(1000)
                    if scor_jucator > 21:
                        mesaj("Ai depasit 21! Dealerul castiga!", RED, 430, 280)
                    else:
                        scor_jucator = calculeazaScor(mana_jucator)
                        while scor_dealer < 17:
                            mana_dealer.append(pachet.pop())
                            scor_dealer = calculeazaScor(mana_dealer)
                            # actualizare ecran
                            screen.blit(imagine_fundal, (0, 0))
                            buton(850, 50, 98, 50, RED, "IESIRE", BLACK)
                            buton(640, 450, 98, 50, GRAY, "   HIT", BLACK)
                            buton(270, 450, 98, 50, GRAY, "STAND", BLACK)
                            buton(445, 450, 120, 50, GRAY, "DOUBLE", BLACK)
                            mesaj("DEALER", BLACK, 450, 50)
                            mesaj("CARTILE MELE", BLACK, 415, 500)
                            mana(mana_jucator, mana_dealer, carte_dealer)
                            mesaj(f"Scor: {calculeazaScor(mana_jucator)}", BLACK, 460, 540)
                            mesaj(f"Scor Dealer: {calculeazaScor(mana_dealer)}", BLACK, 420, 90)
                            pygame.display.flip()
                            #
                            pygame.time.delay(1000)

                        if scor_dealer > 21 or scor_jucator > scor_dealer:
                            mesaj("Ai câștigat!", GREEN, 430, 280)
                        elif scor_jucator == scor_dealer:
                            mesaj("Egalitate!", GRAY, 430, 280)
                        else:
                            mesaj("Dealerul câștigă!", RED, 430, 280)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    running_new = False

        screen.blit(imagine_fundal, (0, 0))

        buton(850, 50, 98, 50, RED, "IESIRE", BLACK)
        buton(640, 450, 98, 50, GRAY, "   HIT", BLACK)
        buton(270, 450, 98, 50, GRAY, "STAND", BLACK)
        buton(445, 450, 120, 50, GRAY, "DOUBLE", BLACK)
        mesaj("DEALER", BLACK, 450, 50)
        mesaj("CARTILE MELE", BLACK, 415, 500)

        mana(mana_jucator, mana_dealer, carte_dealer)
        mesaj(f"Scor: {calculeazaScor(mana_jucator)}", BLACK, 460, 540)
        mesaj(f"Scor Dealer: {calculeazaScor(mana_dealer[:1]) if not carte_dealer else calculeazaScor(mana_dealer)}",BLACK, 420, 90)

        pygame.display.flip()

    pygame.time.delay(1000)
    IncepeJocul()

#meniu principal
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