import pygame as pg
import pickle
from os import path

top_scores = []

class Highscore():
    def __init__(self):
        self.white = (255, 255, 255)
        self.file_name = "high_score.txt"
        self.highscore = 0
        self.dir = path.dirname(__file__)
        self.file = path.join(self.dir, self.file_name)
        self.current_highscore = self.get_high_score()

    def get_high_score(self):
        high_score = 0

        try:
            high_score_file = open(self.file_name, "r")
            high_score = int(high_score_file.read())
            high_score_file.close()
            return high_score
        except IOError:

            print("There is no high score yet.")

        return high_score

    def calc_score(self, fact_1, fact_2, fact_3):
        score = int(((fact_1 / fact_2) * 150 - fact_3))
        return score

    def save_high_score(self, fact_1, fact_2, fact_3):
        score = self.calc_score(fact_1, fact_2, fact_3)
        if score <= self.current_highscore:
            print("you did not surpass the current highscore. Try again!")
            return

        if score <= 0:
            score = 0

            print("ISSA GOOSE EGG! you did not surpass the current highscore. Try again!")
            try:
                high_score_file = open("high_score.txt", "w")
                high_score_file.write(str(score))
                high_score_file.close()
            except IOError:
                print("Unable to save the high score.")
        try:
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(str(score))
            high_score_file.close()

            print("new highscore saved")
        except IOError:
            print("Unable to save the high score.")




