import time, sys
class Human:
    def __init__(self,name,hp,atk,defe,nat):
        Human.self = self
        Human.name = name
        Human.hp = hp
        Human.atk = atk
        Human.defe = defe
        Human.self.stat = name,hp,atk,defe,nat
        Human.nat = nat

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()

p1 = Human('Zulu','21','25','26','Choatic Evil')
p2 = Human('Shoa','17','27','28','LawFul Good')

print(p1.name)
print(p1.stat)
print(p1.nat)

print(p2.name)
print(p2.stat)
print(p2.nat)

delay_print('Hello\nWelcome to SweatVentures\nPlease pick between our two characters\n')
print(p1.name + '' + p1.name)
delay_print('to check stats. Enter stats')

response = input()
if response == 'Stats'.lower():
   delay_print('this is Zulu stats: ' + p1.stats + '\nThis is Shoa Stata:\n' + p2.stats)
