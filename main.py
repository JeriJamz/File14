import pygame as pg, sys 
from settings import * 
from debug import debug
from lvls import Level

class Game:
    def __init__(self):

        #gen setup
        pg.init()
        self.screen = pg.display.set_mode((Hgt,Wdt))
        pg.display.set_caption('RPG')
        self.clock = pg.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.screen.fill(Blk)
            debug('-_-')
            self.level.run()
            pg.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
