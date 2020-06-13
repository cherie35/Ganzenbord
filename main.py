import sys
import pygame as pg
import screeninfo as si
from bord import Bord

MONITOR = []
for m in si.get_monitors():
    MONITOR.append(m)
SCREEN_SIZE = (MONITOR[0].width, MONITOR[0].height)
BACKGROUND = pg.image.load("Ganzenbord_Template_TransCrop6.png")
FPS = 60

positions = [[45,24],[45,32],[45,36],[45,40],[45,44],[45,48],
[45,53],[45,57],[45,61],[43,66],[40,70],[37,72],[33,74],[29,75],
[25,75],[20,74],[16,73],[13,71],[9,67],[7,60],[7,56],[7,52],[7,48],
[7,44],[7,40],[7,36],[7,32],[8,27],[11,24],[14,22],[17,20],[21,19],
[26,19],[30,20],[33,22],[36,25],[38,28],[39,32],[39,36],[39,40],
[39,44],[39,48],[39,53],[39,57],[39,61],[35,65],[31,68],[27,69],
[24,70],[20,68],[16,65],[14,60],[14,54],[14,49],[14,44],[14,39],
[14,35],[14,32],[17,28],[23,26],[28,26],[31,29],[32,33],[25,47]]


class App(object):
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.done = False

    def update(self):
        """
        All updates to all actors occur here.
        Exceptions include things that are direct results of events which
        may occasionally occur in the event loop.
        For example, updates based on held keys should be found here, but
        updates to single KEYDOWN events would be found in the event loop.
        """
        pass

    def render(self):
        """
        All calls to drawing functions here.
        No game logic.
        """
        self.screen.fill((255, 255, 255))
        self.screen.blit(BACKGROUND, [0,0])

        b = Bord(10, 10, 10, 50, 80)
        b.set_steps(63)
        b.set_grid(positions, self.screen)

        pg.display.update()

    def event_loop(self):
        """
        Event handling here.  Only things that are explicit results of the
        given events should be found here.  Do not confuse the event and update
        phases.
        """
        for event in pg.event.get():
           if event.type == pg.QUIT:
               self.done = True

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