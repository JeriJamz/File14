import pygame as pg
from setting import *
from debug import debug

run = True
pg.init()
screen = pg.display.set_mode(size)
pg.display.set_caption('RPG')
img = pg.image.load('...\fighter\boneman').convert_alpha()
img.convert()


while run:
    screen.fill(wht)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    pg.display.update()

pg.quit()
