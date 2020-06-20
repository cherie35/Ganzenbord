import sys
import pygame as pg
import Intro_screen

BACKGROUND = pg.Color("darkslategray")
SCREEN_SIZE = (1920, 1080)
FPS = 60
SCREEN = pg.display.set_mode(SCREEN_SIZE)

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
        self.screen.fill(BACKGROUND)
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
    Intro_screen.Introscreen().game_intro()
    App().main_loop()
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()