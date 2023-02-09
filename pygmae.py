import pygame,sys
from pygame.locals import *

pygame.init()

# this should set up window
WINDOW = pygame.display.set_mode((700,500), 0 ,32)
pygame.display.set_caption('Drawings')

#set up colors
Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)

#drawing onna surface object
WINDOW.fill(White)
pygame.draw.polygon(WINDOW, Green,((146,0), (291,106),(236,277), (56,277),(0,106)))#polygon,color, plot points
pygame.draw.line(WINDOW, Blue, (60,60),(120,60),4)
pygame.draw.line(WINDOW, Blue, (120,60), (60,120))
pygame.draw.line(WINDOW, Blue,(60,120),(120,120), 4)
pygame.draw.circle(WINDOW, Blue,(300,50), 20, 0)
pygame.draw.ellipse(WINDOW, Red,(300,250,40,80),1)
pygame.draw.rect(WINDOW, Red,(200,150,100,50))

pixObj = pygame.PixelArray(WINDOW)
pixObj[480][380] = Black
pixObj[482][382] = Black
pixObj[484][384] = Black
pixObj[486][386] = Black
pixObj[488][388] = Black
del pixObj#remeber to add the del statment to close PixelArray

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
