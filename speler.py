import pygame as pg

class Speler(pg.sprite.Sprite):
    # sprite voor de speler(s)

    def __init__(self, height, width, margin, row, column):
        self.height = height
        self.width = width
        self.margin = margin
        self.row = row
        self.column = column
        self.location = 0
        self.xy = []

        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("Data-beestje2.png")
        self.rect =  self.image.get_rect()
        self.rect.center = (490, 910)

    def set_xy(self, screen):
        if len(self.xy) < 65:
            for index in range(0, len(self.positions),1):
                for rw in range(self.row):
                    for clmn in range(self.column):
                        if [rw, clmn] == self.positions[index] and len(self.xy) < 65:
                            x, y = (self.margin + self.width) * clmn + self.margin, (self.margin + self.height) * rw + self.margin
                            self.xy.append([x, y])

    def set_location(self, worp):
        #print("Current locatie index: {}\nMet positie:  {}\n".format(self.location, self.xy[self.location]))
        self.location += worp
        #print("Worp locatie index:    {}\nMet positie:  {}\n\n".format(self.location, self.xy[self.location]))
        self.rect.center = (self.xy[self.location][0], self.xy[self.location][1])
        #self.rect.x += 5

    def get_spelerPositions(self):
        self.positions = [[45,24],[45,32],[45,36],[45,40],[45,44],[45,48],
                         [45,53],[45,57],[45,61],[43,66],[40,70],[37,72],[33,74],[29,75],
                         [25,75],[20,74],[16,73],[13,71],[9,67],[7,60],[7,56],[7,52],[7,48],
                         [7,44],[7,40],[7,36],[7,32],[8,27],[11,24],[14,22],[17,20],[21,19],
                         [26,19],[30,20],[33,22],[36,25],[38,28],[39,32],[39,36],[39,40],
                         [39,44],[39,48],[39,53],[39,57],[39,61],[35,65],[31,68],[27,69],
                         [24,70],[20,68],[16,65],[14,60],[14,54],[14,49],[14,44],[14,39],
                         [14,35],[14,32],[17,28],[23,26],[28,26],[31,29],[32,33],[25,47]]