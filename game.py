import pygame as pyg
from pygame.locals import *


BLK = (0,0,0)
GRY = (127,127,127)
WHT = (255,255,255)
RED = (255,0,0)
BLU = (0,0,255)
GRE = (0,255,0)
YLW = (255,255,0)
CYN = (0,255,255)
MAG = (255,0,255)


pyg.init()

screen =  pyg.display.set_mode((1248,840))
screen.fill(WHT)
pyg.display.set_caption('Sprite Sheets 1')
Rss = pyg.image.load('romona.png').convert_alpha()#put this under screen setup
screen.blit(Rss, (0,0))

def get_img(sheet,width,height):#scale):
    img = pyg.Surface((width,height)).convert_alpha()
    img.blit(sheet, (0,0),(0,0,width, height))
    #img = pyg.transform.scale(image, (width * scale, height * scale))

    return img
frame_00 = get_img(Rss, 68,35)

run = True


while run:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False
    pyg.display.update()
    
pyg.quit()
