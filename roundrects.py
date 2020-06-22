
import pygame as pg

def AAfilledRoundedRect(surface,rect,color,radius=0.4):

    """
    AAfilledRoundedRect(surface,rect,color,radius=0.4)

    surface : destination
    rect    : rectangle
    color   : rgb or rgba
    radius  : 0 <= radius <= 1
    """

    rect         = pg.Rect(rect)
    color        = pg.Color(*color)
    alpha        = color.a
    color.a      = 0
    pos          = rect.topleft
    rect.topleft = 0,0
    rectangle    = pg.Surface(rect.size,pg.SRCALPHA)

    circle       = pg.Surface([min(rect.size)*3]*2,pg.SRCALPHA)
    pg.draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
    circle       = pg.transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

    radius              = rectangle.blit(circle,(0,0))
    radius.bottomright  = rect.bottomright
    rectangle.blit(circle,radius)
    radius.topright     = rect.topright
    rectangle.blit(circle,radius)
    radius.bottomleft   = rect.bottomleft
    rectangle.blit(circle,radius)

    rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
    rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

    rectangle.fill(color,special_flags= pg.BLEND_RGBA_MAX)
    rectangle.fill((255,255,255,alpha),special_flags= pg.BLEND_RGBA_MIN)

    return surface.blit(rectangle,pos)