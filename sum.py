import sys, time, pygame, random

#idk what this is gonna be about

def delay_print(c):
    for s in c:
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(0.05)

print('my name is Walter. I hope I can be of assistance to you')
print('What my I refer to you as?')
name = input()
print('Your name is ' + name + ' correct?')
response = input()
if response == 'Yes'.lower():
    print('Great! let us continue')
else:
    print('Well, let us fix that')
    while True:
        if response ==  'No'.lower():
            print('Please reenter you name.')
            name = input()
            print('Is this correct')
            response = input()

        if response == 'Yes'.lower():
            break
        
print('Ill be introducing you to a couple of things')
print('Im gonna introduce you to a game without a name')
delay_print('Are you ready\n')
response1 = input()

if response == 'Yes'.lower():
    print('Great let us contiue')
else:
    sys.exit()

print('This is the start of the number game')

secrectNumber =  random.randint(1,25)

delay_print('You will have 6 guesses to guess my secrect number\n')

for guessTaken in range(1,7):
    print('Guess what number i am thinking of')
    guess =  int(input())
    if guess > secrectNumber:
        print('Your guess is just too high')
    elif guess < secrectNumber:
        print('Your guess is too low')
    else:
        break
if guess == secrectNumber:
    print('Congrats you guessed my secrect number')
else:
    print('You did not guess my secrect number. I must inform you that I am terminating this program')
    sys.exit()
    
print('I am glad you made it past my first trial.')
