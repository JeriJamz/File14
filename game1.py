import pygame as pg, sys
from pygame.locals import *#call it pygame
#(cmb)from setting import *

R = (255,0,0)
G = (0,255,0)
B = (0,0,255)
BLK = (0,0,0)
WHT = (255,255,255)
YEL = (255,255,0)
Cyn = (0,255,255)
Mag = (255,0,255)

size = 640,240#this define the screen size
width,height = size#this actually defines the screen
screen = pg.display.set_mode(size)#this is where screen get defined. give it name and atr
screen.fill(BLK)#changes background
pg.display.update()#gotta update to display again



running = True# makes running = true
pg.init()#starts da game
screen = pg.display.set_mode(size)#this is where screen get defined. give it name and atr
#try and get a lil sprite up
ball = pg.image.load("ball.jpg")
rect = ball.get_rect()
speed = [2,2]
while running:#fancy way of while true
    for event in pg.event.get():#This is where u can user input
        if event.type == pg.QUIT:#gives opt for the player to quit
            running = False#code for quitting
rect = rect.move(speed)
if rect.left < 0 or rect.right > width:
    speed[0] =-speed[0]
if rect.top < 0 or rect.bottem > height:
    speed[1] =-[1]
pg.draw.rect(screen, R, rect, 1)
screen.blit(ball, rect)
pg.display.update()


pg.quit()
#MEMBA RGB R(255,0,0)G(0,255,0)B(0,0,255)BLK(0,0,0)Gry(127,127,127)Wht(0,0,0)
