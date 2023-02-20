import sys, time, pyautogui as pag

def delay_print(f):
    for t in f:
        stdout.flush(t)
        stdout.write()
        time.sleep(.5)

delay_print("this string")
