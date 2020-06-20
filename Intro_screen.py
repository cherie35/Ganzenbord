import sys
import pygame as pg
import main

black = (0, 0, 0)
white = (255, 255, 255)
brown = (210, 105, 30)

class Introscreen(object):
    def __init__(self):

        self.clock = pg.time.Clock()
        self.introbkgd = pg.image.load("images/mountains.png").convert()
        self.screen_x = 0
        self.screen_size = main.SCREEN_SIZE
        self.introloop = True
        self.hiscore = True
        self.rules = True
    
    def game_intro(self):
        largetext = pg.font.Font('fonts/freesansbold.ttf', 115)
    
        while self.introloop:
            for event in pg.event.get():
               if event.type == pg.QUIT:
                   pg.quit()
                   quit()
    
            self.moving_background()
    
    
            #Titel
            self.text_objects("Data Gans", largetext, (self.screen_size[0]/2), (self.screen_size[1]/6))
    
            #Buttons
            self.button("Start", (self.screen_size[0] / 2), (self.screen_size[1] / 2.5), 200, 75, white, brown)
            self.button("Regels", (self.screen_size[0] / 2), (self.screen_size[1] / 2), 200, 75, white, brown, self.rules_screen)
            self.button("Hiscore", (self.screen_size[0] / 2), (self.screen_size[1] / 1.65), 200, 75, white, brown, self.hiscore_screen)
            self.button("Quit", (self.screen_size[0] - 250), (self.screen_size[1] / 1.1), 200, 75, white, brown, self.quitgame)
            pg.display.update()
            self.clock.tick(60)

    def text_objects(self, text, font, center_x, center_y):
        textsurface = font.render(text, True, black)
        textrect = textsurface.get_rect()
        textrect.center = (center_x, center_y)
        main.SCREEN.blit(textsurface, textrect)
    
    def button(self, msg, x, y, width, height, inactivecolor, activecolor, action=None):
        smalltext = pg.font.Font('fonts/freesansbold.ttf', 50)
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        rect = pg.Rect(x, y, width, height)
        rect.center = (x, y)
        if x + (width / 2) > mouse[0] > x - (width / 2) and y + (height / 2) > mouse[1] > y - (height / 2):
            pg.draw.rect(main.SCREEN, activecolor, rect)
            if click[0] == 1:
                if msg == "Start":
                    self.introloop = False
                    self.rules = False
                    self.hiscore = False
                else:
                    action()
        else:
            pg.draw.rect(main.SCREEN, inactivecolor, rect)
    
        self.text_objects(msg, smalltext, x, y)
    
    def quitgame(self):
        pg.quit()
        quit()
    
    def rules_screen(self):
    
        while self.rules:
            for event in pg.event.get():
               if event.type == pg.QUIT:
                   pg.quit()
                   quit()
    
            self.moving_background()
    
            self.button("Terug", (self.screen_size[0] / 10), (self.screen_size[1] / 1.1), 200, 75, white, brown, self.game_intro)
    
    
            pg.display.update()
            self.clock.tick(60)
    
    
    def hiscore_screen(self):

        while self.hiscore:
            for event in pg.event.get():
               if event.type == pg.QUIT:
                   pg.quit()
                   quit()

            self.moving_background()
    
            self.button("Terug", (self.screen_size[0] / 10), (self.screen_size[1] / 1.1), 200, 75, white, brown, self.game_intro)
    
    
            pg.display.update()
            self.clock.tick(60)
    
    
    def moving_background(self):
        # moving background
        rel_x = self.screen_x % self.introbkgd.get_rect().width
        main.SCREEN.blit(self.introbkgd, (rel_x - self.introbkgd.get_rect().width, 0))
        if rel_x < self.screen_size[0]:
            main.SCREEN.blit(self.introbkgd, (rel_x, 0))
        self.screen_x -= 1