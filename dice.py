import random as rdm
import pygame as pg

pg.init()
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
DICE = 0
DICE_POS = (SCREEN_WIDTH - 200, SCREEN_HEIGHT - 170)
ROLL_POS = DICE_POS
gameDisplay = pg.display.set_mode(SCREEN_SIZE)
status = False
black = 0, 0, 0
white = 255, 255, 255
one = pg.image.load("1.png")
two = pg.image.load("2.png")
three = pg.image.load("3.png")
four = pg.image.load("4.png")
five = pg.image.load("5.png")
six = pg.image.load("6.png")


def roll_dice():
    number = rdm.randrange(1, 6);
    return number

def display_dice(dice):
    roll_outcome(dice)

def roll_outcome(dice_digit):
    if (dice_digit == 1):
        gameDisplay.blit(one, DICE_POS)
    elif (dice_digit == 2):
        gameDisplay.blit(two, DICE_POS)
    elif (dice_digit == 3):
        gameDisplay.blit(three, DICE_POS)
    elif (dice_digit == 4):
        gameDisplay.blit(four, DICE_POS)
    elif (dice_digit == 5):
        gameDisplay.blit(five, DICE_POS)
    elif (dice_digit == 6):
        gameDisplay.blit(six, DICE_POS)

def draw_text(surf, text, size, x, y):
    font             = pg.font.Font(font_name, size)
    text_surface     = font.render(text, True, white)
    text_rect        = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def game_menu():
    draw_text(gameDisplay, 'REGELS', 63, (SCREEN_WIDTH - 1600), SCREEN_HEIGHT / 6)
    draw_text(gameDisplay, 'De bedoeling van het spel is om als eerste op hokje 63 uit te komen. ', 20, (SCREEN_WIDTH - 1380), SCREEN_HEIGHT / 2.95)
    draw_text(gameDisplay, 'Elke speler mag per beurt met de dobbelstenen gooien en de pion zoveel hokjes verplaatsen als er ogen gegooid worden.', 20, (SCREEN_WIDTH - 1120), SCREEN_HEIGHT / 2.7)
    draw_text(gameDisplay, 'Wie te veel ogen gooit en daardoor voorbij 63 zou komen, moet vanaf 63 weer teruglopen. ', 20, (SCREEN_WIDTH - 1270), SCREEN_HEIGHT / 2.5)
    draw_text(gameDisplay, 'Het is dan mogelijk dat de speler op het hokje 58 of 52 terechtkomt.', 20, (SCREEN_WIDTH - 1388), SCREEN_HEIGHT / 2.3)
    draw_text(gameDisplay, 'Komt de speler bij het terugtellen op een hokje met een gans, dan telt de speler het gegooide aantal ogen terug.', 20, (SCREEN_WIDTH - 1165), SCREEN_HEIGHT / 2.15)
    draw_text(gameDisplay, 'Het speelbord heeft een aantal hokjes met een speciale betekenis:', 20, (SCREEN_WIDTH - 1370), SCREEN_HEIGHT / 1.8)
    draw_text(gameDisplay, '- Pipeline   >   ga verder naar 12', 20, (SCREEN_WIDTH - 1472), SCREEN_HEIGHT / 1.72)
    draw_text(gameDisplay, '- Lag   >   sla 1 beurt over', 20, (SCREEN_WIDTH - 1505), SCREEN_HEIGHT / 1.67)
    draw_text(gameDisplay, '- Geen RAM vrij   >   sla 2 beurten over', 20, (SCREEN_WIDTH - 1438), SCREEN_HEIGHT / 1.62)
    draw_text(gameDisplay, '- Blue screen of death   >   ga terug naar 39', 20, (SCREEN_WIDTH - 1415), SCREEN_HEIGHT / 1.57)
    draw_text(gameDisplay, '- Privacy schending. Je hebt een rechtszaak!   >   sla 2 beurten over', 20, (SCREEN_WIDTH - 1295), SCREEN_HEIGHT / 1.52)
    draw_text(gameDisplay, '- Server crash   >   ga terug naar begin', 20, (SCREEN_WIDTH - 1440), SCREEN_HEIGHT / 1.48)

def roll_msg():
     msg = str(DICE)
     print(msg)

font_name = pg.font.match_font('verdana')


