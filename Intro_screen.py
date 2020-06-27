import sys
import pygame as pg
import main

black = (0, 0, 0)
white = (255, 255, 255)
brown = (210, 105, 30)

class Introscreen(object):
    def __init__(self):

        self.clock = pg.time.Clock()
        self.introbkgd = pg.image.load("mountains.png").convert()
        self.screen_x = 0
        self.screen_size = main.SCREEN_SIZE
        self.introloop = True
        self.hiscore = True
        self.rules = True
        self.largetext = pg.font.Font('freesansbold.ttf', 115)
        self.font_name = pg.font.match_font('verdana')

    def game_intro(self):

        while self.introloop:
            for event in pg.event.get():
               if event.type == pg.QUIT:
                   pg.quit()
                   quit()
    
            self.moving_background()
    
    
            #Titel
            self.text_objects("Data Gans", self.largetext, (self.screen_size[0]/2), (self.screen_size[1]/6))
    
            #Buttons
            self.button("Start", (self.screen_size[0] / 2), (self.screen_size[1] / 2.5), 200, 75, white, brown)
            self.button("Regels", (self.screen_size[0] / 2), (self.screen_size[1] / 2), 200, 75, white, brown, self.rules_screen)
            self.button("Hiscore", (self.screen_size[0] / 2), (self.screen_size[1] / 1.65), 200, 75, white, brown, self.hiscore_screen)
            self.button("Quit", (self.screen_size[0] - 250), (self.screen_size[1] / 1.1), 200, 75, white, brown, self.quitgame)
            pg.display.update()
            self.clock.tick(60)

    def draw_text(self, surf, text, size, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, white)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    def text_objects(self, text, font, center_x, center_y):
        textsurface = font.render(text, True, black)
        textrect = textsurface.get_rect()
        textrect.center = (center_x, center_y)
        main.SCREEN.blit(textsurface, textrect)
    
    def button(self, msg, x, y, width, height, inactivecolor, activecolor, action=None):
        smalltext = pg.font.Font('freesansbold.ttf', 50)
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

            #draw background rectangle
            rect = pg.Rect(500, 500, 1600, 750)
            rect.center = (self.screen_size[0] / 2, self.screen_size[1] / 2 - 60)
            pg.draw.rect(main.SCREEN, brown, rect)


            self.draw_text(main.SCREEN, 'REGELS', 63, (self.screen_size[0] - 1600), self.screen_size[1] / 6)
            self.draw_text(main.SCREEN, 'De bedoeling van het spel is om als eerste op hokje 63 uit te komen. ', 20,
                      (self.screen_size[0] - 1380), self.screen_size[1] / 2.95)
            self.draw_text(main.SCREEN,
                      'Elke speler mag per beurt met de dobbelstenen gooien en de pion zoveel hokjes verplaatsen als er ogen gegooid worden.',
                      20, (self.screen_size[0] - 1120), self.screen_size[1] / 2.7)
            self.draw_text(main.SCREEN,
                      'Wie te veel ogen gooit en daardoor voorbij 63 zou komen, moet vanaf 63 weer teruglopen. ', 20,
                      (self.screen_size[0] - 1270), self.screen_size[1] / 2.5)
            self.draw_text(main.SCREEN, 'Het is dan mogelijk dat de speler op het hokje 58 of 52 terechtkomt.', 20,
                      (self.screen_size[0] - 1388), self.screen_size[1] / 2.3)
            self.draw_text(main.SCREEN,
                      'Komt de speler bij het terugtellen op een hokje met een gans, dan telt de speler het gegooide aantal ogen terug.',
                      20, (self.screen_size[0] - 1165), self.screen_size[1] / 2.15)
            self.draw_text(main.SCREEN, 'Het speelbord heeft een aantal hokjes met een speciale betekenis:', 20,
                      (self.screen_size[0] - 1370), self.screen_size[1] / 1.8)
            self.draw_text(main.SCREEN, '- Pipeline   >   ga verder naar 12', 20, (self.screen_size[0] - 1472),
                      self.screen_size[1] / 1.72)
            self.draw_text(main.SCREEN, '- Lag   >   sla 1 beurt over', 20, (self.screen_size[0] - 1505), self.screen_size[1] / 1.67)
            self.draw_text(main.SCREEN, '- Geen RAM vrij   >   sla 2 beurten over', 20, (self.screen_size[0] - 1438),
                      self.screen_size[1] / 1.62)
            self.draw_text(main.SCREEN, '- Blue screen of death   >   ga terug naar 39', 20, (self.screen_size[0] - 1415),
                      self.screen_size[1] / 1.57)
            self.draw_text(main.SCREEN, '- Privacy schending. Je hebt een rechtszaak!   >   sla 2 beurten over', 20,
                      (self.screen_size[0] - 1295), self.screen_size[1] / 1.52)
            self.draw_text(main.SCREEN, '- Server crash   >   ga terug naar begin', 20, (self.screen_size[0] - 1440),
                      self.screen_size[1] / 1.48)

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