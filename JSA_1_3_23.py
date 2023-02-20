import time, sys

def delay_print(s):
    for z in s:
        sys.stdout.write(z)
        sys.stdout.flush()
        time.sleep(.075)

delay_print('Really random announcments. Found some documentations on A.I w/python.\n')
delay_print('Be on the look out for the lingo parser and A.I.')
