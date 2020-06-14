import sys
import pygame as pg
import main

black = (0, 0, 0)
white = (255, 255, 255)
brown = (210, 105, 30)

clock = pg.time.Clock()
introbkgd = pg.image.load("images/mountains.png").convert()
screen_x = 0
screen_size = main.SCREEN_SIZE

def game_intro():
    largetext = pg.font.Font('fonts/freesansbold.ttf', 115)

    intro = True
    while intro:
        for event in pg.event.get():
           if event.type == pg.QUIT:
               pg.quit()
               quit()

        moving_background()


        #Titel
        text_objects("Data Gans", largetext, (screen_size[0]/2), (screen_size[1]/6))

        #Buttons
        button("Start", (screen_size[0] / 2), (screen_size[1] / 2.5), 200, 75, white, brown)
        button("Regels", (screen_size[0] / 2), (screen_size[1] / 2), 200, 75, white, brown, rules_screen)
        button("Hiscore", (screen_size[0] / 2), (screen_size[1] / 1.65), 200, 75, white, brown, hiscore_screen)

        pg.display.update()
        clock.tick(60)
    

def text_objects(text, font, center_x, center_y):
    textsurface = font.render(text, True, black)
    textrect = textsurface.get_rect()
    textrect.center = (center_x, center_y)
    main.SCREEN.blit(textsurface, textrect)


def button(msg, x, y, width, height, inactivecolor, activecolor, action=None):
    smalltext = pg.font.Font('fonts/freesansbold.ttf', 50)
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    rect = pg.Rect(x, y, width, height)
    rect.center = (x, y)
    if x + (width / 2) > mouse[0] > x - (width / 2) and y + (height / 2) > mouse[1] > y - (height / 2):
        pg.draw.rect(main.SCREEN, activecolor, rect)
        if click[0] == 1 and action != None:
            action()
    else:
        pg.draw.rect(main.SCREEN, inactivecolor, rect)

    text_objects(msg, smalltext, x, y)

def rules_screen():
    rules = True

    while rules:
        for event in pg.event.get():
           if event.type == pg.QUIT:
               pg.quit()
               quit()

        moving_background()

        button("Terug", (screen_size[0] / 10), (screen_size[1] / 1.1), 200, 75, white, brown, game_intro)


        pg.display.update()
        clock.tick(60)


def hiscore_screen():
    hiscore = True

    while hiscore:
        for event in pg.event.get():
           if event.type == pg.QUIT:
               pg.quit()
               quit()
        moving_background()

        button("Terug", (screen_size[0] / 10), (screen_size[1] / 1.1), 200, 75, white, brown, game_intro)


        pg.display.update()
        clock.tick(60)


def moving_background():
    # moving background
    global screen_x
    rel_x = screen_x % introbkgd.get_rect().width
    main.SCREEN.blit(introbkgd, (rel_x - introbkgd.get_rect().width, 0))
    if rel_x < screen_size[0]:
        main.SCREEN.blit(introbkgd, (rel_x, 0))
    screen_x -= 1