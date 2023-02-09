#this is gonna cover fonts ig
#https://invypy.com/formats
import pygame,sys
from pygame.locals import *

pygame.init()
WINDOW =pygame.display.set_mode((700,500))
pygame.display.set_caption('Hello Wrld?')

White = (255,255,255)
Blue =(0,0,255)
Slime = (0,128,0)

fontObj = pygame.font.Font('AstronBoyWonder.ttf',32)
textSurfaceObj =fontObj.render('Hello World',True, Slime,Blue)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200,150)

run = True
while run:
    WINDOW.fill(White)
    WINDOW.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
