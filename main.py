import sys
import pygame as pg
import screeninfo as si
import random as rd

from bord import Bord
from speler import Speler
from dobbelButton import Dobbel

FPS = 60
COLORS = []
MONITOR = []
for m in si.get_monitors():
    MONITOR.append(m)
SCREEN_SIZE = (MONITOR[0].width, MONITOR[0].height)
BACKGROUND = pg.image.load("Ganzenbord_Template_TransCrop6.png")

b = Bord()
s = Speler(10, 10, 10, 50, 80)
d = Dobbel()

all_sprites = pg.sprite.Group()
all_sprites.add(s)


class App(object):
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.done = False
        self.number = ''

    def update(self):
        """
        All updates to all actors occur here.
        Exceptions include things that are direct results of events which
        may occasionally occur in the event loop.
        For example, updates based on held keys should be found here, but
        updates to single KEYDOWN events would be found in the event loop.
        """
        all_sprites.update()

    def render(self):
        """
        All calls to drawing functions here.
        No game logic.
        """
        
        b.get_shitlist()
        s.get_spelerPositions()
        self.screen.fill((255,255,255))
        if len(COLORS) == 0: b.set_colors(COLORS)
        b.set_polygons(self.screen, COLORS)
        self.screen.blit(BACKGROUND, [0,0])
        s.set_xy(self.screen)
        all_sprites.draw(self.screen)
        d.shape(self.screen, pg.mouse.get_pos())
        d.message_display(self.screen, self.number)

        pg.display.update()


    def event_loop(self):
        """
        Event handling here.  Only things that are explicit results of the
        given events should be found here.  Do not confuse the event and update
        phases.
        """
        #mouse = pg.mouse.get_pos()
        for event in pg.event.get():
            
            if event.type == pg.MOUSEBUTTONDOWN and d.shape(self.screen, pg.mouse.get_pos()) == True:
                self.number = str(rd.randint(1,6))
                s.set_location(int(self.number))
            if event.type == pg.QUIT:
               self.done = True
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


def main():
    """
    Prepare pygame and the display and create an App instance.
    Call the app instance's main_loop function to begin the App.
    """
    pg.init()
    pg.display.set_mode(SCREEN_SIZE, pg.FULLSCREEN)
    App().main_loop()
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()