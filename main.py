import sys
import pygame as pg
import Intro_screen
import Quizbehaviour as Quizb
#import screeninfo as si
import random as rd

from bord import Bord
from speler import Speler
from dobbelButton import Dobbel

SCREEN_SIZE = (1920, 1080)
SCREEN = pg.display.set_mode(SCREEN_SIZE)

DICE = 0
rolled = False

FPS = 60
#COLORS = []
MONITOR = []
#for m in si.get_monitors():
#    MONITOR.append(m)
#    print(MONITOR[0])
#SCREEN_SIZE = (MONITOR[0].width, MONITOR[0].height)
#SCREEN = pg.display.set_mode(SCREEN_SIZE)
BACKGROUND = pg.image.load("bord.png")

b = Bord()
d = Dobbel()





class App(object):
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.done = False
        self.colors = []
        self.quizbehaviour = Quizb.Quizbehaviour()
        self.introbkgd = pg.image.load("mountains.png").convert()
        self.screen_x = 0
        self.s = Speler(10, 10, 10, 50, 80)

        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(self.s)

        self.number = ''


    def update(self):
        """
        All updates to all actors occur here.
        Exceptions include things that are direct results of events which
        may occasionally occur in the event loop.
        For example, updates based on held keys should be found here, but
        updates to single KEYDOWN events would be found in the event loop.
        """
        self.all_sprites.update()

    def render(self):
        """
        All calls to drawing functions here.
        No game logic.
        """

        self.moving_background()
        if len(self.colors) == 0: b.set_colors(self.colors)
        b.set_polygons(self.screen, self.colors)
        self.screen.blit(BACKGROUND, [0,0])
        self.s.set_xy(self.screen)
        self.all_sprites.draw(self.screen)
        d.hover(self.screen, pg.mouse.get_pos())
        d.message_display(self.screen, "Roll")
        d.roll_outcome(self.screen, self.number)
        self.s.movement(self.colors)

        self.quizbehaviour.show_score()

        pg.display.update()


    def event_loop(self):
        """
        Event handling here.  Only things that are explicit results of the
        given events should be found here.  Do not confuse the event and update
        phases.
        """

        for event in pg.event.get():

            keys = pg.key.get_pressed()
            if event.type == pg.QUIT:
                self.done = True
            if keys[pg.K_g]:
                self.quizbehaviour.quiz_popup((254, 197, 20))
            if keys[pg.K_p]:
                print("Questions:" + str(Quizb.hiscore[1]) + " correct answers:" + str(Quizb.hiscore[0]))
            if keys[pg.K_i]:
                Intro_screen.Introscreen().game_intro()
            if event.type == pg.MOUSEBUTTONDOWN and d.hover(self.screen, pg.mouse.get_pos()) == True:
                self.number = str(rd.randint(1, 6))
                self.s.set_location(int(63))


        pg.display.update()



    def main_loop(self):
        """
        Main loop for your whole app.  This doesn't need to be touched until
        you start writing framerate independant games.
        """
        while not self.done:
            self.event_loop()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def moving_background(self):
        # moving background
        rel_x = self.screen_x % self.introbkgd.get_rect().width
        SCREEN.blit(self.introbkgd, (rel_x - self.introbkgd.get_rect().width, 0))
        if rel_x < SCREEN_SIZE[0]:
            SCREEN.blit(self.introbkgd, (rel_x, 0))
        self.screen_x -= 1


def main():
    """
    Prepare pygame and the display and create an App instance.
    Call the app instance's main_loop function to begin the App.
    """
    pg.init()
    Intro_screen.Introscreen().game_intro()
    App().main_loop()
    pg.quit()
    sys.exit()



if __name__ == "__main__":
    main()