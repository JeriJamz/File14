import pygame as pg

BLK = (0,0,0)
WHT = (255,255,255)
B = (0,0,255)


size = 640,240
FPS = 120
width,height = size
screen = pg.display.set_mode(size)
screen.fill(BLK)
pg.display.update()

class MySprite(pg,sprite.Sprite):
    def __init__(self,action):
        super(Mysprite,self).__init__()
        im = glob.glob(f"png\\{action})

run = True
pg.init()
screen = pg.display.set_mode(size)
Chou = pg.image.load("fighter/Mr_Chou.png").convert_alpha()
pg.display.set_caption('Big Brawler')

def get_img(sheet,frame,width,height, scale,color):
    img = pg.Surface((width,height)).convert_alpha()
    img.blit(sheet, (0,0),((frame*width),0, width, height))
    img = pg.transform.scale(img,(width * scale, height * scale))
    img.set_colorkey(color)

    return img

frame_0 = get_img(Chou,0,77,68,1,B)
frame_1 = get_img(Chou,1,77,68,1,B)
frame_2 = get_img(Chou,2,77,68,1,B)
frame_3 = get_img(Chou,3,77,68,1,B)
frame_4 = get_img(Chou,4,77,68,1,B)

while run:
    screen.fill(WHT)

    screen.blit(frame_0,(0,0))
    screen.blit(frame_1,(0,0))
    screen.blit(frame_2,(0,0))
    screen.blit(frame_3,(0,0))
    screen.blit(frame_4,(0,0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update()
    
pg.quit()
