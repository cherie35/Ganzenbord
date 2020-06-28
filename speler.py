import pygame as pg
import main
import Quizbehaviour as Quizb
import overview

class Speler(pg.sprite.Sprite):

    def __init__(self, height, width, margin, row, column):
        self.height = height
        self.width = width
        self.margin = margin
        self.row = row
        self.column = column

        self.quizbehaviour = Quizb.Quizbehaviour()
        self.trick = traps.Traps()
        self.askquestion = False
        self.numberofturns = 0

        self.positions = self.get_spelerPositions()
        self.traps = [12,18,31,42,52,58] # Niet dezelfde traps als in bord.py
        self.location = 0
        self.xy = []
        self.tussen = []
        self.reverse = []
        self.overview = overview.overview()

        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("Data-beestje2.png")
        self.rect =  self.image.get_rect()
        self.rect.center = (650, 290)#(490, 910)#(570, 350)


    def set_xy(self, screen):
        if len(self.xy) < 65:
            for index in range(0, len(self.positions),1):
                for rw in range(self.row):
                    for clmn in range(self.column):
                        if [rw, clmn] == self.positions[index] and len(self.xy) < 65:
                            x, y = (self.margin + self.width) * clmn + self.margin, (self.margin + self.height) * rw + self.margin
                            self.xy.append([x, y])


    def set_location(self, worp):
        self.blit = 30
        if self.location+worp > 63:
            for step in range(self.location+1, 63+1, 1):
                self.tussen.append(self.xy[step])
            for step in range(62, 63-(worp - (len(self.tussen)-1)), -1):
                print("in set_location if-loop")
                self.reverse.append(self.xy[step])
                print("stappen toegevoegd aan reverse lijst")
            self.location = 63 - (self.location + worp - 63)
        elif worp < 0:
            for step in range(self.location, (self.location+worp)-1, -1):
                self.reverse.append(self.xy[step])
            self.location += worp
        else:
            print("set_location else")
            for step in range(self.location, self.location+worp+1, 1):
                self.tussen.append(self.xy[step])
            self.location += worp
            print("new location: {}".format(self.location))
        self.askquestion = True
        self.numberofturns += 1
    

    def movement(self, colors, screen):
        if self.tussen != []:
            if [self.rect.center[0], self.rect.center[1]] != self.tussen[0]:
                diffX = self.xy[self.xy.index(self.tussen[0])][0] - self.xy[self.xy.index(self.tussen[0]) -1][0]
                diffY = self.xy[self.xy.index(self.tussen[0])][1] - self.xy[self.xy.index(self.tussen[0]) -1][1]
                if diffX == 0: self.rect.center = (self.rect.center[0] , self.rect.center[1] + (diffY / 10))
                if diffY == 0: self.rect.center = (self.rect.center[0] + (diffX / 10), self.rect.center[1])
                if diffX != 0 and diffY != 0: self.rect.center = (self.rect.center[0] + (diffX / 10), self.rect.center[1] + (diffY / 10))
            else:
                del(self.tussen[0])

        if self.tussen == [] and self.reverse != []:
            print("in reverse lijst")
            if [self.rect.center[0], self.rect.center[1]] != self.reverse[0]:
                diffX = self.xy[self.xy.index(self.reverse[0]) +1][0] - self.xy[self.xy.index(self.reverse[0])][0]
                diffY = self.xy[self.xy.index(self.reverse[0]) +1][1] - self.xy[self.xy.index(self.reverse[0])][1]
                if diffX == 0: self.rect.center = (self.rect.center[0] , self.rect.center[1] - (diffY / 10))
                if diffY == 0: self.rect.center = (self.rect.center[0] - (diffX / 10), self.rect.center[1])
                if diffX != 0 and diffY != 0: self.rect.center = (self.rect.center[0] - (diffX / 10), self.rect.center[1] - (diffY / 10))
            else:
                del(self.reverse[0])
        if self.tussen == [] and self.reverse == [] and self.location == 63:
            self.rect.center = (490, 910)
            self.location = 0
            self.overview.overview(self.numberofturns, self.location, self)

        if self.tussen == [] and self.reverse == [] and self.location != 0 and self.askquestion and self.location != 63:
            self.quizbehaviour.quiz_popup(colors[self.location - 1])

        if self.tussen == [] and self.reverse == [] and self.location in self.traps:
            if self.location == self.traps[0]: self.set_location(-6)
            if self.location == self.traps[1]: self.set_location(int(self.location/ -2))
            if self.location == self.traps[2]: self.overloadBG(screen)
            if self.location == self.traps[3]: self.set_location(-5)
            if self.location == self.traps[4]: self.secureBG(screen)
            if self.location == self.traps[5]: self.set_location(-58)
            
        if self.tussen == [] and self.reverse == [] and self.location == 63: print("Woohoo! Finished :D")

        if self.tussen == [] and self.reverse == [] and self.location != 0 and self.askquestion:
            print("vraag wordt gesteld")
            self.quizbehaviour.quiz_popup(colors[self.location - 1], self.location)
            self.askquestion = False
=======
        if self.tussen == [] and self.reverse == [] and self.location in self.traps: 
                print("location in traps")
                self.trick.set_trap(self.location)#actie = self.trick.set_trap(self.location)
                #self.set_location(actie)
        else:   print("loop wordt meegenomen, maar is False")
        if self.tussen == [] and self.reverse == [] and self.location != 0 and self.location not in self.traps and self.askquestion:
                self.quizbehaviour.quiz_popup(colors[self.location - 1])
                self.askquestion = False
>>>>>>> Stashed changes

    def secureBG(self, screen):
        if self.blit != 0:
            text_rect = pg.draw.rect(screen, (0,0,0), (550, 100, 900, 100), 0)
            image = pg.image.load("Security_bg2.png").convert()
            image.set_colorkey((0,0,0))
            screen.blit(image, (0,0))
            self.blit -= 1
            pg.display.update()

    def overloadBG(self, screen):
        if self.blit != 0:
            text_rect = pg.draw.rect(screen, (0,0,0), (900, 400, 600, 300), 0)
            image = pg.image.load("Overload_bg.png").convert()
            image.set_colorkey((0,0,0))
            screen.blit(image, (0,0))
            self.blit -= 1
            pg.display.update()

    def get_spelerPositions(self):
        self.positions = [[45,24],[45,32],[45,36],[45,40],[45,44],[45,48],
                         [45,53],[45,57],[45,61],[43,66],[40,70],[37,72],[33,74],[29,75],
                         [25,75],[20,74],[16,73],[13,71],[9,67],[7,60],[7,56],[7,52],[7,48],
                         [7,44],[7,40],[7,36],[7,32],[8,27],[11,24],[14,22],[17,20],[21,19],
                         [26,19],[30,20],[33,22],[36,25],[38,28],[39,32],[39,36],[39,40],
                         [39,44],[39,48],[39,53],[39,57],[39,61],[35,65],[31,68],[27,69],
                         [24,70],[20,68],[16,65],[14,60],[14,54],[14,49],[14,44],[14,39],
                         [14,35],[14,32],[17,28],[23,26],[28,26],[31,29],[32,33],[25,47]]
        return self.positions