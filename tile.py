import pygame as pg
from setting import *

class Tile(pg.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image
        self.rect = self.image.get_rect(topleft = pos)
