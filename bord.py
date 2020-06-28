import pygame as pg
import random as rd

class Bord:
    def __init__(self):
        self.shitlist = self.get_shitlist()
        self.traps = [5,18,30,41,51,57]

    def set_colors(self, colors):
        choices = [(240,78,152), (0,191,179), (0,119,204), (254,197,20), (166, 214,  117)]
        for key in self.shitlist:
            if key > 0:
                prev_color = colors[key-1]
                new_color = rd.choice(choices)
                while prev_color == new_color: new_color = rd.choice(choices)
                colors.append(new_color)
            else:
                colors.append(rd.choice(choices))
        for key in self.shitlist:
            if key in self.traps:
                colors[key] = (72,72,72)

    def set_polygons(self, screen, colors):
        start = [(384, 846),(545, 847),(544, 826),(560, 827),(623, 897),(556, 967),(543, 965),(543, 947),(382, 942)]
        pg.draw.polygon(screen, (255,255,255), start, 0)
        for key in self.shitlist:
            pg.draw.polygon(screen, colors[key], self.shitlist.get(key), 0)


    def get_shitlist(self):
        """
        0: [(384, 846),(545, 847),(544, 826),(560, 827),(623, 897),(556, 967),(543, 965),(543, 947),(382, 942)],
        tegel nr -1 ivm set_polygons waar de key bij 0 moet beginnen door een lijst
        """
        self.shitlist = {0: [(567,831),(693,846),(695,968),(564,968),(625,897)],
                         1: [(697, 847),(775, 848),(775, 967),(696, 964)],
                         2: [(778, 847),(850, 849),(852, 962),(777, 967)],
                         3: [(858, 848),(931, 849),(930, 966),(857, 967)],
                         4: [(937, 846),(1021, 848),(1022, 965),(938, 965)],
                         5: [(1025, 847),(1118, 850),(1119, 967),(1023, 966)],
                         6: [(1123, 849),(1192, 849),(1201, 964),(1124, 963)],
                         7: [(1189, 847),(1249, 835),(1298, 949),(1202, 970)],
                         8: [(1250, 836),(1333, 788),(1412, 880),(1364, 920),(1296, 947)],
                         9: [(1339, 786),(1384, 738),(1474, 815),(1413, 879)],
                         10: [(1419, 681),(1387, 734),(1477, 808),(1522, 732)],
                         11: [(1421, 675),(1442, 619),(1550, 653),(1525, 727)],
                         12: [(1442, 613),(1452, 555),(1565, 557),(1548, 646)],
                         13: [(1452, 551),(1444, 470),(1557, 445),(1565, 553)],
                         14: [(1445, 462),(1427, 404),(1534, 361),(1557, 439)],
                         15: [(1426, 398),(1395, 347),(1492, 276),(1532, 354)],
                         16: [(1397, 340),(1356, 294),(1438, 209),(1491, 272)],
                         17: [(1355, 292),(1252, 233),(1303, 117),(1377, 153),(1438, 207)],
                         18: [(1254, 229),(1164, 218),(1173, 95),(1245, 98),(1304, 119)],
                         19: [(1175, 98),(1087, 96),(1090, 216),(1164, 216)],
                         20: [(1084, 98),(1011, 98),(1012, 214),(1085, 214)],
                         21: [(1012, 214),(936, 213),(934, 97),(1011, 97)],
                         22: [(934, 99),(843, 99),(844, 214),(934, 214)],
                         23: [(841, 98),(770, 98),(766, 215),(840, 215)],
                         24: [(767, 95),(692, 98),(691, 214),(765, 215)],
                         25: [(626, 227),(689, 217),(690, 91),(632, 96),(584, 107)],
                         26: [(580, 108),(493, 154),(564, 261),(627, 227)],
                         27: [(564, 261),(487, 155),(428, 216),(525, 301)],
                         28: [(425, 219),(523, 303),(491, 355),(377, 292)],
                         29: [(378, 296),(494, 354),(475, 407),(349, 376)],
                         30: [(475, 412),(350, 379),(337, 476),(470, 475)],
                         31: [(469, 480),(339, 481),(357, 582),(478, 543)],
                         32: [(356, 587),(479, 548),(500, 594),(387, 663)],
                         33: [(500, 600),(390, 669),(442, 739),(532, 645)],
                         34: [(536, 648),(446, 741),(517, 798),(578, 686)],
                         35: [(581, 689),(639, 715),(604, 836),(520, 803)],
                         36: [(641, 715),(608, 835),(695, 842),(694, 721)],
                         37: [(695, 721),(774, 722),(774, 839),(695, 841)],
                         38: [(776, 722),(852, 723),(850, 841),(777, 839)],
                         39: [(854, 721),(934, 723),(933, 840),(854, 839)],
                         40: [(936, 722),(1020, 723),(1021, 840),(935, 840)],
                         41: [(1022, 720),(1118, 723),(1118, 841),(1023, 839)],
                         42: [(1123, 722),(1182, 721),(1216, 837),(1122, 843)],
                         43: [(1183, 719),(1229, 698),(1308, 802),(1271, 827),(1214, 840)],
                         44: [(1236, 693),(1308, 804),(1364, 760),(1403, 705),(1290, 632)],
                         45: [(1314, 580),(1296, 628),(1403, 701),(1437, 615)],
                         46: [(1318, 527),(1448, 523),(1436, 612),(1315, 574)],
                         47: [(1309, 473),(1434, 433),(1449, 519),(1317, 522)],
                         48: [(1288, 422),(1396, 346),(1433, 424),(1309, 469)],
                         49: [(1286, 421),(1219, 360),(1279, 243),(1352, 291),(1394, 345)],
                         50: [(1221, 361),(1165, 343),(1187, 221),(1236, 224),(1278, 242)],
                         51: [(1184, 220),(1166, 343),(1035, 342),(1037, 220)],
                         52: [(1036, 222),(945, 221),(943, 341),(1035, 340)],
                         53: [(946, 222),(844, 221),(847, 339),(941, 341)],
                         54: [(766, 222),(840, 223),(842, 341),(764, 341)],
                         55: [(763, 223),(675, 223),(691, 345),(764, 341)],
                         56: [(672, 219),(586, 246),(651, 362),(690, 345)],
                         57: [(651, 365),(583, 249),(522, 301),(492, 354),(477, 410),(604, 444),(622, 397)],
                         58: [(605, 443),(475, 408),(475, 551),(607, 505)],
                         59: [(605, 504),(484, 554),(528, 640),(623, 539)],
                         60: [(622, 544),(529, 638),(601, 694),(656, 578)],
                         61: [(658, 578),(600, 696),(646, 715),(709, 717),(708, 596)]}
        return self.shitlist