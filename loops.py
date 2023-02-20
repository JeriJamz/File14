import time,sys

#loops
def dprint(c):
    for s in c:
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(.05)


i = 0
while i< len('Howdy'):
    letter = 'Howdy'[i]
    print('The letter is ' + letter)
    i = i + 1


print('Please enter the password')
password = input()
if password == 'Swordfish':
    print('Access Granted')
    pass
else:
    print('Access Denied')
    sys.exit()
print('Done')

x = 0 
while x < 3:
    password = input()
    if password == 'Swordfish':
        print('Access Granted')
        pass
    elif password != 'Swordfish':
        print('The hint is marlin')
        x + 1
    else:
        x == 3
        sys.exit()
