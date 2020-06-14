import random as rdm
import pygame as pg

pg.init()
BACKGROUND = pg.Color("darkslategray")
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
FPS = 60
DICE = 0
DICE = 0
DICE_POS = (SCREEN_WIDTH - 200, SCREEN_HEIGHT - 170)
ROLL_POS = DICE_POS
gameDisplay = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()
status = False
black = 0, 0, 0
white = 255, 255, 255
one = pg.image.load("assets/dice/1.png")
two = pg.image.load("assets/dice/2.png")
three = pg.image.load("assets/dice/3.png")
four = pg.image.load("assets/dice/4.png")
five = pg.image.load("assets/dice/5.png")
six = pg.image.load("assets/dice/6.png")

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

def roll_msg():
     msg = "You rolled " + str(DICE) + "."
     print(msg)

rolled = False
while status == False:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            status = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:

                DICE = roll_dice()
            rolled = True

    gameDisplay.fill(BACKGROUND)

    display_dice(DICE)
    if (rolled):
        roll_msg()
        rolled = False
    pg.display.update()
    clock.tick(60)

pg.quit()
quit()