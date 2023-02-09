#Try this again
import sys, pygame, time

class Human:
    def __init__(self,stats,name,hea,atk,defe):
        Human.self = self
        Human.stats.name.hea.atk.defe = stats
        Human.name = name
        Human.hea = hea
        Human.atk = atk
        Human.defe = defe

    def paladin(huma,stat):
        return huma.stats

    def paladin_name(huma):
        return huma.name

p1 = Human('Zulu','Paladin Gen','25','21','24')

print(p1.paladin_name)
