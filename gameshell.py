import pygame as pg#this import the pystuff
from setting import *#this import game settings i dont want on the main 

pg.init()#starts pg

screen = pg.display.set_mode((size))#set screen size
screen.fill(blk)#fills blk
pg.display.set_caption('Rpg frame')#Title

img = pg.image.load('...\Faceset.png')

run = True#run

while run:#start the main game program
    for event in pg.event.get():#if you quit
        if event.type == pg.QUIT:
            run = False
    pg.display.update()#if you need any screen update
        


pg.quit()
