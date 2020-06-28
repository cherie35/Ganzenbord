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

    def save_high_score(self, fact_1, fact_2, fact_3):
        score = int(((fact_1 / fact_2) * 500 - fact_3))
        if score <= 0:
            score = 0
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
        except IOError:
            print("Unable to save the high score.")




