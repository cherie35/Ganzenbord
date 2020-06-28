from Highscore import Highscore as HS
import main
import pygame as pg
import Quizbehaviour
import roundrects
import Intro_screen

black = (0, 0, 0)
white = (255, 255, 255)
brown = (210, 105, 30)

class overview():
    
    def __init__(self):
        self.question_bg = pg.image.load("Questions_bg.png")
        self.overviewbool = True
        self.clock = pg.time.Clock()
        self.highscore = HS()
        
    def overview(self, turns, location, speler):
        self.overviewbool = True
        while self.overviewbool:
            for event in pg.event.get():
               if event.type == pg.QUIT:
                   pg.quit()
                   quit()





            mouse = pg.mouse.get_pos()
            click = pg.mouse.get_pressed()

            main.SCREEN.blit(self.question_bg, (1,1))

            self.draw_text(main.SCREEN, 'UIGESPEELD!', 63, (main.SCREEN_SIZE[0] / 2), main.SCREEN_SIZE[1] / 6, black)

            self.draw_text(main.SCREEN, 'aantal gestelde vragen:', 40, (main.SCREEN_SIZE[0] / 3), main.SCREEN_SIZE[1] / 3, black)
            self.draw_text(main.SCREEN, str(Quizbehaviour.hiscore[1]), 40, (main.SCREEN_SIZE[0] / 3 + 450), main.SCREEN_SIZE[1] / 3, black)

            self.draw_text(main.SCREEN, 'aantal goed beantwoorde vragen:', 40, (main.SCREEN_SIZE[0] / 3), main.SCREEN_SIZE[1] / 2.5, black)
            self.draw_text(main.SCREEN, str(Quizbehaviour.hiscore[0]), 40, (main.SCREEN_SIZE[0] / 3 + 450), main.SCREEN_SIZE[1] / 2.5, black)

            self.draw_text(main.SCREEN, 'aantal beurten:', 40, (main.SCREEN_SIZE[0] / 3), main.SCREEN_SIZE[1] / 2.12, black)
            self.draw_text(main.SCREEN, str(turns), 40, (main.SCREEN_SIZE[0] / 3 + 450), main.SCREEN_SIZE[1] / 2.12, black)

            self.highscore.save_high_score(Quizbehaviour.hiscore[1], Quizbehaviour.hiscore[0], turns)

            rect = pg.Rect((main.SCREEN_SIZE[0] / 2), (main.SCREEN_SIZE[1] / 1.2), 500, 100)
            rect.center = (main.SCREEN_SIZE[0] / 2, main.SCREEN_SIZE[1] / 1.2)
            if (main.SCREEN_SIZE[0] / 2) + (500 / 2) > mouse[0] > (main.SCREEN_SIZE[0] / 2) - (500 / 2) and (main.SCREEN_SIZE[1] / 1.2) + (100 / 2) > mouse[1] > (main.SCREEN_SIZE[1] / 1.2) - (100 / 2):
                roundrects.AAfilledRoundedRect(main.SCREEN, rect, brown)
                if click[0] == 1:
                    self.overviewbool = False
                    speler.numberofturns = 0

                    Quizbehaviour.hiscore[0] = 0
                    Quizbehaviour.hiscore[1] = 0

                    Intro_screen.Introscreen().game_intro()
            else:
                roundrects.AAfilledRoundedRect(main.SCREEN, rect, white)
            self.draw_text(main.SCREEN, 'Terug naar hoofdmenu', 40, (main.SCREEN_SIZE[0] / 2), main.SCREEN_SIZE[1] / 1.235, black)

            pg.display.update()
            self.clock.tick(60)

    def draw_text(self, surf, text, size, x, y, color):
        font = pg.font.Font('freesansbold.ttf', size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)
