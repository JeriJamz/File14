import pygame as pg

class Level:
    def _init__(self):

        #get the display surface?
        self.display_surface = pg.display.get_surface()
        #sprite group
        self.visible_sprites = pg.sprite.Group()
        self.obstacles_sprites = pg.sprite.Group()

    def run(self):
        #update
        pass