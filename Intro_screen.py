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
    smalltext = pg.font.Font('fonts/freesansbold.ttf', 50)


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
        start_rect = pg.Rect((screen_size[0] / 2), (screen_size[1] / 2), 200, 75)
        start_rect.center = (screen_size[0] / 2), (screen_size[1] / 2.5)
        pg.draw.rect(main.SCREEN, white, start_rect)

        rules_rect = pg.Rect((screen_size[0] / 2), (screen_size[1] / 2), 200, 75)
        rules_rect.center = (screen_size[0] / 2), (screen_size[1] / 2)
        pg.draw.rect(main.SCREEN, white, rules_rect)

        hiscores_rect = pg.Rect((screen_size[0] / 2), (screen_size[1] / 2), 200, 75)
        hiscores_rect.center = (screen_size[0] / 2), (screen_size[1] / 1.65)
        pg.draw.rect(main.SCREEN, white, hiscores_rect)

        #mouse collision with buttons
        mouse = pg.mouse.get_pos()

        if (screen_size[0] / 2) + 100 > mouse[0] > (screen_size[0] / 2) - 100 and (screen_size[1] / 2.5) + 32.75 > mouse[1] > (screen_size[1] / 2.5) - 32.75:
            pg.draw.rect(main.SCREEN, brown, start_rect)

        if (screen_size[0] / 2) + 100 > mouse[0] > (screen_size[0] / 2) - 100 and (screen_size[1] / 2) + 32.75 > mouse[1] > (screen_size[1] / 2) - 32.75:
            pg.draw.rect(main.SCREEN, brown, rules_rect)

        if (screen_size[0] / 2) + 100 > mouse[0] > (screen_size[0] / 2) - 100 and (screen_size[1] / 1.65) + 32.75 > mouse[1] > (screen_size[1] / 1.65) - 32.75:
            pg.draw.rect(main.SCREEN, brown, hiscores_rect)

        #Buttontext
        text_objects("Start", smalltext, (screen_size[0] / 2), (screen_size[1] / 2.5))
        text_objects("Regels", smalltext, (screen_size[0] / 2), (screen_size[1] / 2))
        text_objects("Hiscore", smalltext, (screen_size[0] / 2), (screen_size[1] / 1.65))

        pg.display.update()
        clock.tick(120)
    


def text_objects(text, font, center_x, center_y):
    textsurface = font.render(text, True, black)
    textrect = textsurface.get_rect()
    textrect.center = (center_x, center_y)
    main.SCREEN.blit(textsurface, textrect)
    #return textsurface, textsurface.get_rect()