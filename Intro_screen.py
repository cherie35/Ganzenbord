import sys
import pygame as pg
import main

black = (0, 0, 0)
white = (255, 255, 255)
brown = (210, 105, 30)


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
        text_objects("Data Gans", largetext, (screen_size[0]/2), (screen_size[1]/6))

        #Buttons
        button("Start", (screen_size[0] / 2), (screen_size[1] / 2.5), 200, 75, white, brown)
        button("Regels", (screen_size[0] / 2), (screen_size[1] / 2), 200, 75, white, brown)
        button("Hiscore", (screen_size[0] / 2), (screen_size[1] / 1.65), 200, 75, white, brown)

        pg.display.update()
        clock.tick(60)
    

def text_objects(text, font, center_x, center_y):
    textsurface = font.render(text, True, black)
    textrect = textsurface.get_rect()
    textrect.center = (center_x, center_y)
    main.SCREEN.blit(textsurface, textrect)


def button(msg,x,y,width,height,inactivecolor,activecolor):
    smalltext = pg.font.Font('fonts/freesansbold.ttf', 50)
    mouse = pg.mouse.get_pos()
    rect = pg.Rect(x, y, width, height)
    rect.center = (x, y)
    if x + width > mouse[0] > x - width and y + height > mouse[1] > y - height:
        pg.draw.rect(main.SCREEN, activecolor, rect)
    else:
        pg.draw.rect(main.SCREEN, inactivecolor, rect)

    text_objects(msg, smalltext, x, y)

