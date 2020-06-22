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

correctanwsers = 0
questionsasked = 0
hiscore = [correctanwsers,questionsasked]

class Quizbehaviour(object):
    def __init__(self):
        self.screen_size = main.SCREEN_SIZE
        self.clock = pg.time.Clock()
        self.quiz = True
        self.quizrectsize = (self.screen_size[0] / 2, self.screen_size[1] / 4)
        self.quizrectcenterpos = (self.screen_size[0] / 2, self.screen_size[1] / 6)
        self.answerrectsize = (self.screen_size[0] / 2, self.screen_size[1] / 10)
        self.answerrectcenterpos = (self.screen_size[0] / 5, self.screen_size[1] / 2)
        self.font = pg.font.Font('fonts/freesansbold.ttf', 20)
        self.lefttextpadding = 50

        #Load questions from JSON and assign them per category to variables
        with open("Questions.json") as f:
            self.questiondata = json.load(f)
        self.red_questions = self.questiondata["red"]
        self.blue_questions = self.questiondata["blue"]

        self.questioncolors = {
            "red": self.red_questions,
            "blue": self.blue_questions
        }


    def quiz_popup(self, color):

        questionnumber = 0 #placeholder, has to be a random question from the json

        questiondata = self.questioncolors.get(color)
        random.shuffle(questiondata)


        text = questiondata[questionnumber]['question']

        #put answers in a list and shuffle the list, so that it's ready for blitting
        correctanswer = questiondata[questionnumber]['correctanswer']
        answer2 = questiondata[questionnumber]['answer2']
        answer3 = questiondata[questionnumber]['answer3']
        answerlist = [correctanswer,answer2,answer3]
        random.shuffle(answerlist)

        self.quiz = True
        while self.quiz:
            for event in pg.event.get():
               if event.type == pg.QUIT:
                   pg.quit()
                   quit()



            ##draw question rectangle
            rect = pg.Rect(self.screen_size[0] / 10, self.screen_size[1] / 10, self.quizrectsize[0], self.quizrectsize[1])
            rect.center = self.quizrectcenterpos
            roundrects.AAfilledRoundedRect(main.SCREEN, rect, brown)

            #draw text on the question rect
            self.blit_text(main.SCREEN, text, (self.quizrectcenterpos[0] / 2 + self.lefttextpadding, self.quizrectcenterpos[1] - self.quizrectsize[1] / 2 + 50), self.font)


            #draw answer buttons
            padding = 0
            for answer in answerlist:

                self.button(answer,(self.screen_size[0] / 2), (self.screen_size[1] / 2.3 + padding),self.answerrectsize[0],self.answerrectsize[1], white, brown, questiondata, correctanswer)
                padding += 200

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
                    self.remove_askedquestion(questions)


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

    def remove_askedquestion(self,questions):
        if questions:
            questions.pop(0)
