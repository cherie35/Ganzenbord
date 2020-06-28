import pygame as pg
import speler as speler

class Traps:
    def __init__(self):
        self.reverse = []
        self.traps = [12,18,31,42,52,58] # Niet dezelfde traps als in bord.py
        #self.speler = speler.Speler.set_location()

    def set_trap(self, location, rect, xy):
        if location == self.traps[0]: self.incompleteData(location, rect, xy)
        if location == self.traps[1]: self.duplicateData()
        if location == self.traps[2]: self.muchData()
        if location == self.traps[3]: self.organizationData()
        if location == self.traps[4]: self.secureData()
        if location == self.traps[5]: self.deathData(location, rect, xy)

    def incompleteData(self, location, rect, xy):
        print("incomplete trap")

    def duplicateData(self):
        print("duplicate trap")

    def muchData(self):
        print("too much data trap")

    def organizationData(self):
        print("unorganized trap")

    def secureData(self):
        print("unsecure trap")

    def deathData(self, location, rect, xy):
        print("deathData")
        if self.reverse == []: 
            for step in range(location, 0, -1): self.reverse.append(xy[step])
            location = 0
        print(self.reverse)
        if self.reverse != []:
            print("reverse is gevuld")
            if [rect[0], rect[1]] != self.reverse[0]:
                diffX = xy[xy.index(self.reverse[0]) +1][0] - xy[xy.index(self.reverse[0])][0]
                diffY = xy[xy.index(self.reverse[0]) +1][1] - xy[xy.index(self.reverse[0])][1]
                if diffX == 0: 
                    rect = (rect[0] , rect[1] - (diffY / 10))
                    print("Y moved")
                if diffY == 0: 
                    rect = (rect[0] - (diffX / 10), rect[1])
                    print("X moved")
                if diffX != 0 and diffY != 0: 
                    rect = (rect[0] - (diffX / 10), rect[1] - (diffY / 10))
                    print("XY moved")
                print("rect center check")
            else:
                print("niet verplaatst")
                del(self.reverse[0])
                if len(self.reverse) == 0: location