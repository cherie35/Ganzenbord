import pygame as pg
import main
import pygame.freetype as freetype

black = (0, 0, 0)
white = (255, 255, 255)
brown = (210, 105, 30)

class Quizbehaviour(object):
    def __init__(self):
        self.screen_size = main.SCREEN_SIZE
        self.clock = pg.time.Clock()
        self.quiz = True
        self.quizrectsize = (self.screen_size[0] / 2, self.screen_size[1] / 2)
        self.quizrectcenterpos = (self.screen_size[0] / 2, self.screen_size[1] / 3)

    def quiz_popup(self):
        font = pg.font.Font('fonts/freesansbold.ttf', 20)
        text = "This is a really long sentence with a couple of breaks.\nSometimes it will break even if there isn't a break " \
               "in the sentence, but that's because the text is too long to fit the screen. but that wont stop me now bla bla bal\nIt can look strange sometimes.\n" \
               "This function doesn't check if the text is too high to fit on the height of the surface though, so sometimes " \
               "text will disappear underneath the surface"

        while self.quiz:
            for event in pg.event.get():
               if event.type == pg.QUIT:
                   pg.quit()
                   quit()

            rect = pg.Rect(self.screen_size[0] / 10, self.screen_size[1] / 10, self.quizrectsize[0], self.quizrectsize[1])
            rect.center = self.quizrectcenterpos
            pg.draw.rect(main.SCREEN, brown, rect)
            self.blit_text(main.SCREEN, text, (self.quizrectcenterpos[0] / 2, self.quizrectcenterpos[1] - self.quizrectsize[1] / 2), font)
            pg.display.update()
            self.clock.tick(60)




    def blit_text(self,surface, text, pos, font, color=pg.Color('black')):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = (self.screen_size[0] - (self.screen_size[0] - (self.quizrectcenterpos[0] + self.quizrectsize[0] / 2)), 600)
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.