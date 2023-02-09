import pyautogui as pag
import time, sys

def delay_print(c):
    for s in c:
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(.005)

delay_print("Little automation trick. it keeps the mouse active")

while True:
    pag.moveRel(0,10)
    time.sleep(1)
    pag.moveRel(10,0)
    time.sleep(1)
    
