import pygame as pg, sys
from pygame.locals import *
#this img 0,0-77,68
BLK = (0,0,0)
WHT = (255,255,255)

size = (1000,600)
width,height = size
screen = pg.display.set_mode(size)
screen.fill(BLK)
pg.display.update()

running = True
pg.init()
screen = pg.display.set_mode(size)
pg.display.set_caption('sprite')

#SSI means spirte sheet image
ssi = pg.image.load('fighter/Mr_Chou.png').convert_alpha()#member to have the pic in the file location and if its on a file fo "file_name"/"pic name"

def get_img(sheet,width,height):#this function makes it where u can get a single frame
    img = pg.Surface((width,height)).convert_alpha()#gets the wid anf hgt of the frame
    img.blit(sheet, (0,0), (0,0, width, height))#0,0 puts it in top left corner also gets rid of the black block
    
    return img#returns the function
    #like screen img is a surface and i can blit on it

frame_0 = get_img(ssi, 77,68)#this singles out a frame 

while running:

    #when u make a background make all new screen updates after it
    screen.fill(WHT)

    #display img
    screen.blit(frame_0,(0,0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pg.display.update()

pg.quit()
