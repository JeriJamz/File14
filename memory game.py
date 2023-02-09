#Memory Puzzle
import pygame,sys
from pygame.loacals import *

FPS = 30
WINWIDTH = 640
WINHEIGHT = 480
REVEALSPD = 8
BOXSIZE = 40
GAPSIZE = 10
BOARDWIDTH = 10
BOARDHEIGHT = 7
assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board nedds to have an even number boxes for pairs matches.'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) /2)
YMARGIN = int((WINDOWWIDTH - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) /2)

#rgb stuff
Gray = (100,100,100)
NavyBlue = (60,60,100)
White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)
Yellow = (255,255,0)
Orange = (255,128,0)
Purple = (255,0,255)
Cyan = (0,255,255)

BGCOLOR = NavyBlue
LIGHTBGCOLOR = Gray
BOXCOLOR = White
HIGHLIGHTCOLOR = Blue

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamonds'
LINES = 'lines'
OVAL = 'oval'

ALLColors = (Red,Green,Blue,Yellow,Orange,Purple,Cyan)
ALLShapes = (DONUT,SQUARE, DIAMONDS,LINES,OVAL)
assert len(ALLColors) * len(ALLShapes) * 2>=BOARDWIDTH * BOARDHEIGHT, 'Board is too big for the number of shapes/color defined'

def maain():
    global FPSCLOCK, WINDOW
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    WINDOW = pygame.display.set_mode((WINWIDTH, WINHEIGHT))

    mousex = 0
    mousey = 0
    pygame.display.set_mode((WINHEIGHT,WINLENGTH))

    mainBoard = getRandomizedBoard()
    revealdBoxes = generateRevealedBoxesData(False)

    firstSelection = None

    WINDOW.fill(BGColor)
    startGameAnimation(mainBoard)

    while True: #main game loop
        mouseClicked = False

        WINDOW.fill(BGColor)#draw windows
        drawBoard(mainBoard, revealdBoxes)

        for event in pygame.event.get():
            if event.tpye == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousc, mousey = eventpos
            elif event.type == MOUSEBUTTONUP:
                mousex,mousey = event.pos
                mouseClicked = True

        boxx, boxy, getBoxAtPixel(mousex,mousey)
        for boxx != None and boxy != None:
            #this mouse is vurrentlt over a box
            if not revealedBoxes[boxx][boxy]:
                drawHightlightBox(boxx,boxy)
            if not revealedBoxes[boxx][boxy] and mouseClicked:
                revealedBoxesAnimation(mainBoard, [(boxx,boxy)])
                revealedBoxes[boxx][boxy] = True

                if firstSelection == None:

                    firstselection = (boxx,boxy)
                else:
                    icon1shape, icon1color = getShapeAndColor(mainBoard,firstSelection[0], firstSelection[1])
                    icon2shape, icon2color = getshapeAndColor(mainBoard, boxx,boxy)

                    if icon1shape != icon2shape or icon1color != icon2color:
                        pygame.time.wait(1000)
                        coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]),(boxx,boxy)])
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxx][boxy]
                    elif hasWon(revealed)
