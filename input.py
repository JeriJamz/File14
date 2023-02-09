#ima workm on data validation
import pyinputplus as pyip


while True:
    print('Enter you age: ')
    age = input()#makes the data input only works for ints
    try:#run a try and except just incase its not int
        age = int(age)
    except:
        print('Please use numeric digits. ')
        continue#keeps the code running
    if age < 1:
        print('Please enter a postive number. ')
        continue
    break
print(f'Your age is {age}.')# ion know wat the f  but let the {} 

response = pyip.inputNum()
