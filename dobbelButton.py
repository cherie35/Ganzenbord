import pygame as pg
import main
import roundrects


class Dobbel():
    def __init__(self):
        self.bright_green = (0, 255, 0)
        self.amazing_orange = (248, 169, 40)
        self.orange = (244, 145, 6)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.position = (1570, 935, 100, 50)
        self.button = pg.Rect(self.position)
        self.dice_position = (1720, 910)
        self.one = pg.image.load("1.png")
        self.two = pg.image.load("2.png")
        self.three = pg.image.load("3.png")
        self.four = pg.image.load("4.png")
        self.five = pg.image.load("5.png")
        self.six = pg.image.load("6.png")



    def hover(self, screen, mouse):
        if 1570 + 50 > mouse[0] > 1570 and 935 + 50 > mouse[1] > 935:
            roundrects.AAfilledRoundedRect(screen, self.button, self.amazing_orange)
            return True
        else:
            roundrects.AAfilledRoundedRect(screen, self.button, self.orange)
            return False


    def message_display(self, screen, text):
        smallText = pg.font.Font("freesansbold.ttf", 20)
        textSurface = smallText.render(text, True, self.white)
        textRect = textSurface.get_rect()
        textRect.center = ((1570+(100/2)), (935+(50/2)))
        screen.blit(textSurface, textRect)

    def text_objects(self, text, font):
        textSurface = font.render(text, True, (0,0,0))
        return textSurface, textSurface.get_rect()

    def roll_outcome(self, screen, number):
        if (number == "1"):
            screen.blit(self.one, self.dice_position)
        elif (number == "2"):
            screen.blit(self.two, self.dice_position)
        elif (number == "3"):
            screen.blit(self.three, self.dice_position)
        elif (number == "4"):
            screen.blit(self.four, self.dice_position)
        elif (number == "5"):
            screen.blit(self.five, self.dice_position)
        elif (number == "6"):
            screen.blit(self.six, self.dice_position)




