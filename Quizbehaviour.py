import pygame as pg
import main
import json
import random
import roundrects

black = (0, 0, 0)
white = (255, 255, 255)
brown = (210, 105, 30)
red = (255, 0, 0)
green = (124, 252, 0)
yellow = (255, 255, 0)

correctanwsers = 0
questionsasked = 0
hiscore = [correctanwsers, questionsasked]

class Quizbehaviour(object):
    def __init__(self):
        self.screen_size = main.SCREEN_SIZE
        self.clock = pg.time.Clock()
        self.quiz = True
        self.quizrectsize = (self.screen_size[0] / 2, self.screen_size[1] / 4)
        self.quizrectcenterpos = (self.screen_size[0] / 2, self.screen_size[1] / 6)
        self.answerrectsize = (self.screen_size[0] / 2, self.screen_size[1] / 10)
        self.answerrectcenterpos = (self.screen_size[0] / 5, self.screen_size[1] / 2)
        self.font = pg.font.Font('freesansbold.ttf', 20)
        self.lefttextpadding = 50
        self.largetext = pg.font.Font('freesansbold.ttf', 60)
        self.color = ""

        #Load questions from JSON and assign them per category to variables
        with open("Questions.json") as f:
            self.questiondata = json.load(f)
        self.yellow_questions = self.questiondata["geel"].copy()
        self.blue_questions = self.questiondata["blauw"].copy()
        self.aqua_questions = self.questiondata["aqua"].copy()
        self.paars_questions = self.questiondata["paars"].copy()

        self.questioncolors = {
            "geel": self.yellow_questions,
            "blauw": self.blue_questions,
            "paars": self.aqua_questions,
            "aqua": self.paars_questions
        }

        self.lookuprgb = {
            (240,78,152): "paars",
            (0,191,179): "aqua",
            (0, 119, 204): "blauw",
            (254, 197, 20): "geel",
            (72, 72, 72): "grijs"
        }


    def quiz_popup(self, color):
        self.quiz = True

        self.color = self.lookuprgb[color]
        self.question_bg = pg.image.load("Questions_bg.png")

        if self.color == "grijs":
            self.quiz = False
        else:

            questiondata = self.questioncolors[self.color]
            random.shuffle(questiondata)


            text = questiondata[0]['question']

            #put answers in a list and shuffle the list, so that answers aren't in the same position every time
            correctanswer = questiondata[0]['correctanswer']
            answer2 = questiondata[0]['answer2']
            answer3 = questiondata[0]['answer3']
            answerlist = [correctanswer,answer2,answer3]
            random.shuffle(answerlist)


        while self.quiz:
            for event in pg.event.get():
               if event.type == pg.QUIT:
                   pg.quit()
                   quit()



            ##draw question rectangle
            rect = pg.Rect(self.screen_size[0] / 10, self.screen_size[1] / 10, self.quizrectsize[0], self.quizrectsize[1])
            main.SCREEN.blit(self.question_bg, (1,1))
            rect.center = self.quizrectcenterpos
            roundrects.AAfilledRoundedRect(main.SCREEN, rect, brown)

            #draw text on the question rect
            self.blit_text(main.SCREEN, text, (self.quizrectcenterpos[0] / 2 + self.lefttextpadding, self.quizrectcenterpos[1] - self.quizrectsize[1] / 2 + 50), self.font)


            #draw answer buttons
            padding = 0
            for answer in answerlist:

                self.button(answer,(self.screen_size[0] / 2), (self.screen_size[1] / 2.3 + padding),self.answerrectsize[0],self.answerrectsize[1], white, brown, questiondata, correctanswer)
                padding += 200

            self.show_score()

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


    def button(self, msg, x, y, width, height, inactivecolor, activecolor, questions, correctanswer=None, ):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        rect = pg.Rect(x, y, width, height)
        rect.center = (x, y)

        # button click functionality
        if x + (width / 2) > mouse[0] > x - (width / 2) and y + (height / 2) > mouse[1] > y - (height / 2):
            roundrects.AAfilledRoundedRect(main.SCREEN, rect, activecolor)
            if click[0] == 1:
                if msg == correctanswer:
                    self.answered_correctly()
                    roundrects.AAfilledRoundedRect(main.SCREEN, rect, green)
                    self.remove_askedquestion(questions, self.color)


                else:
                    self.answered_wrong()
                    roundrects.AAfilledRoundedRect(main.SCREEN, rect, red)

                self.blit_text(main.SCREEN, msg,
                               ((x - width / 2 + self.lefttextpadding), y - self.lefttextpadding / 2), self.font)

                pg.display.update()
                self.clock.tick(60)
                pg.time.delay(1000)
                self.quiz = False

        else:
            roundrects.AAfilledRoundedRect(main.SCREEN, rect, inactivecolor)

        self.blit_text(main.SCREEN,msg,((x - width / 2 + self.lefttextpadding),y - self.lefttextpadding / 2),self.font)

    def answered_correctly(self):
        global hiscore
        hiscore[0] += 1
        hiscore[1] += 1

    def answered_wrong(self):
        global hiscore
        hiscore[1] += 1

    def remove_askedquestion(self, questions, color):
        if len(questions) > 1:
            questions.pop(0)
        else:
            questions.extend(self.questiondata[color])
            questions.pop(0)

    def show_score(self):
        if hiscore[1] == 0:
            self.text_objects("0%", self.largetext, 1800, 50, white)
        else:
            if 100 / hiscore[1] * hiscore[0] > 75:
                self.text_objects(str(round(100 / hiscore[1] * hiscore[0])) + "%", self.largetext, 1800, 50, green)
            elif 100 / hiscore[1] * hiscore[0] <= 25:
                self.text_objects(str(round(100 / hiscore[1] * hiscore[0])) + "%", self.largetext, 1800, 50, red)
            elif 25 < 100 / hiscore[1] * hiscore[0] <= 75:
                self.text_objects(str(round(100 / hiscore[1] * hiscore[0])) + "%", self.largetext, 1800, 50, yellow)


    def text_objects(self, text, font, center_x, center_y, color):
        textsurface = font.render(text, True, color)
        textrect = textsurface.get_rect()
        textrect.center = (center_x, center_y)
        main.SCREEN.blit(textsurface, textrect)
