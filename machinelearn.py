import time,sys

response = input()


def delay_print(d):
    for s in d:
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(.5)

if response == " ":
    delay_response == .05

delay_print('This is the start of machine learning')
