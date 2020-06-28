import pygame as pg
import speler as speler

class Traps:
    def __init__(self):
        self.traps = [11,18,30,41,51,57]
        #self.speler = speler.Speler.set_location()

    def set_trap(self, location):
        if location == self.traps[0]: self.incompleteData()
        if location == self.traps[1]: self.duplicateData()
        if location == self.traps[2]: self.muchData()
        if location == self.traps[3]: self.organizationData()
        if location == self.traps[4]: self.secureData()
        if location == self.traps[5]: self.deathData(location)

    def incompleteData(self):
        pass

    def duplicateData(self):
        pass

    def muchData(self):
        pass

    def organizationData(self):
        pass

    def secureData(self):
        pass

    def deathData(self, location):
        print("deathData")
        return location* -1
        """
        print("in deathData")
        print("stappen terug: {}".format(location))
        print("negative: {}".format(-location))
        self.speler(self, -location)
        """