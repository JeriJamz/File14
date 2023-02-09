import pygame as pg
from settings import * 
pg.init()
font = pg.font.Font(None, 30)

def debug(info, y = 10, x = 10):
    display_surface = pg.display.get_surface()
    debug_surf = font.render(str(info), True, Wht)
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    pg.draw.rect(display_surface, Blk, debug_rect)
    display_surface.blit(debug_surf, debug_rect)
    
