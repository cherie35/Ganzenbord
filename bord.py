import pygame as pg

class Bord:

    def __init__(self, height, width, margin, row, column):
        self.height = height
        self.width = width
        self.margin = margin
        self.row = row
        self.column = column
        self.steps = []
        self.xy = []

    def set_steps(self, amount):
        for step in range(0, amount+1 ,1):
            self.steps.append(step)

    def get_steps(self):
        return self.steps

    def set_grid(self, positions, screen):
        for rw in range(self.row):
            for clmn in range(self.column):
                if [rw,clmn] in positions:
                    x, y = (self.margin + self.width) * clmn + self.margin, (self.margin + self.height) * rw + self.margin
                    self.xy.append([x, y])
                    pg.draw.rect(screen, (0,255,0),[x, y, self.width, self.height])
              
    def get_grid(self):
        return self.grid

    def set_location(self): 
        pass

    def get_location(self, step):
        return self.xy[step]