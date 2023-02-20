import sys
password = 'Swordfish'

trys = 0

print(f"What the password")
response = input()
while response.lower() != password:
    #trys = int(input())
    print("I dont have all day")
    trys += 1
    print(trys)
    #    sys.exit()

print('0')
