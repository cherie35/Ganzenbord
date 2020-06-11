import sys
import pygame as pg
import main

black = (0, 0, 0)
white = (255, 255, 255)


def game_intro():
    screen_x = 0
    screen_size = main.SCREEN_SIZE
    introbkgd = pg.image.load("images/mountains.png").convert()
    clock = pg.time.Clock()
    largetext = pg.font.Font('fonts/freesansbold.ttf', 115)

    intro = True
    while intro:
        for event in pg.event.get():
           if event.type == pg.QUIT:
               pg.quit()
               quit()

        #moving background
        rel_x = screen_x % introbkgd.get_rect().width
        main.SCREEN.blit(introbkgd, (rel_x - introbkgd.get_rect().width, 0))
        if rel_x < screen_size[0]:
            main.SCREEN.blit(introbkgd, (rel_x, 0))
        screen_x -= 1


        #Titel
        text_objects("Data Gans", largetext, (screen_size[0]/2), (screen_size[1]/5))
        pg.display.update()
        clock.tick(120)
    

def text_objects(text, font, center_x, center_y):
    textsurface = font.render(text, True, black)
    textrect = textsurface.get_rect()
    textrect.center = (center_x, center_y)
    main.SCREEN.blit(textsurface, textrect)
    #return textsurface, textsurface.get_rect()