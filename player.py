import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)#can putgroups here
        self.img = pg.image.load('..graphis/test/player.png').convert_alpha
        self.rect = self.image.get_rect(topleft = pos)
