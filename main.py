import pygame as pg, sys 
from settings import * 

class Game:
    def __init__(self):

        #gen setup
        pg.init()
        self.screen = pg.display.set_mode((Hgt,Wdt))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.screen.fill('Blk')
            pg.display_update()
            self.clock.ticks(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()