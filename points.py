import pygame as pg

from pygame.locals import *

fps = 120
BLK = (0,0,0) 
WHT = (255,255,255)
R = (255,0,0)
B = (0,0,255)

size = (1000,600)
width, height = size
screen = pg.display.set_mode(size)
screen.fill(BLK)
pg.display.set_caption('Big Brawler')
pg.display.update()

#bg img
bg_img = pg.image.load('sum.jpeg').convert_alpha()

#fun for bg

screen.fill(WHT)
#gonna try and draw shapes
#rect(Surface, color. (dim in pix))
#polygon(Surface, color,(dim in oix))
#circle(Surface,color, center, rdius, width)
pg.display.update()

def get_bg():
    screen.blit(bg_img(0,0))

    
run = True
pg.init()

while run:

    get_bg()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = false 

    pg.display.update()

pg.quit()
