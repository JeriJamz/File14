import pygame as pg
from rects import *

pts = ('topleft','top','topright','midleft','mid','midright',
       'bottemleft','bottem','bottemright')

BLK = (0,0,0)
R = (255,0,0)
G = (0,255,0)
WHT = (255,255,255)

size = (1000,600)
width,height = size
screen = pg.display.set_mode(size)
screen.fill(BLK)
pg.display.update()

run = True
pg.init()
pg.display.set_caption('Rec')

while run:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    screen.fill(WHT)
    pg.draw.rect(screen,G,rect,4)
    for pt in pts:
        pos = eval('rect.' +pt)
        draw_text(pt, pos)
        pg.draw.circle(screen,R,pos,3)

    pg.display.flip()

    pg.display.update()
    
pg.quit()
