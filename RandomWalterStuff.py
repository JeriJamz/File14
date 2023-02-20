#this is some random py program again
import sys, time


def dq(q):
    for z in q:
        sys.stdout.write(z)
        sys.stdout.flush()
        time.sleep(.05)

#dq("\n") ref
dq("Welcome my name is Walter.\n"
   "What is your name?")
name = input()

dq(f"{name} is it? \n")
response = input()
while response.lower() != 'yes':
    dq('Sorry about that, please tell me your name again.')
    name = input()
    dq(f"I hope I got it right this time, {name}, correct?")
    response = input()
    
