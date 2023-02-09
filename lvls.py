import pygame as pg

class Level:
    def __init__(self):

        #get display
        self.display_surface = pg.display.get_surface()
        
        #sprite group
        self.visible_sprites = pg.sprite.Group()
        self.obstacles_sprites = pg.sprite.Group()

    def run(self):
        #update and draw game
        pass
