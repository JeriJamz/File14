import time, sys
#just a bunch of class work
'''class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("Jeri James","36")
print(p1.name)
print(p1.age)'''
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.05)
class Human:
    def __init__(huma,name,typ,hea,atk,defe,man,lvl):
        huma.name = name
        huma.typ = typ
        huma.hea = hea
        huma.atk = atk
        huma.defe = defe
        huma.man = man
        huma.lvl = lvl
        print(name)

    def npch(huma):
        return huma.name

    def npch_atk(huma):
        return huma.name + ' Attack is : ' + huma.atk
    def fstats_npch(huma):
        return 'These are ' + huma.name + ' stats: ' + Human

p1 = Human('Zulu','Paladin-Gen','25','22','26','17','5')

print(p1.npch())
delay_print(p1.npch_atk())
delay_print(fstats_npch())




