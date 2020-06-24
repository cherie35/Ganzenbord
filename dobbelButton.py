import pygame as pg


class Dobbel():
    def __init__(self):
        self.bright_green = (0,255,0)
        self.green = (0,200,0)
        self.black = (0,0,0)


    def hover(self, screen, mouse):
        if 1570 + 50 > mouse[0] > 1570 and 970 + 50 > mouse[1] > 970:
            pg.draw.rect(screen, self.bright_green, (1570,970,50,50), 0)
            return True
        else:
            pg.draw.rect(screen, self.green, (1570,970,50,50), 0)
            return False


    def message_display(self, screen, text):
        smallText = pg.font.Font("freesansbold.ttf", 30)
        textSurface = smallText.render(text, True, self.black)
        textRect = textSurface.get_rect()
        textRect.center = ((1570+(50/2)), (970+(50/2)))
        screen.blit(textSurface, textRect)


    def text_objects(self, text, font):
        textSurface = font.render(text, True, (0,0,0))
        return textSurface, textSurface.get_rect()