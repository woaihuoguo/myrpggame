#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 21:56:28 2019
my game
@author: bill
"""
import random
from random import shuffle
import time
class player:
    def __init__ (self,name,oc):
        self.name=name
        self.oc=oc

class Magician:
    def __init__ (self):
        self.life=random.randint(80,90)
        self.skill=["FireBall"]*4+["IceArrow"]*4+["Meteorolite"]
        self.attack=[6]*3+[4]*3+[20]
        self.hit=100  
        self.trick=0
    def damaged(self,d):
        if self.trick==0:
            self.life -= d
        else:
            self.life -= 0
            self.trick=0
    def special(self,p1,p2):
        m="{} activated a shield to dispel the next attack"
        print(m.format(p1.name))
        self.trick=1
            
            

class Warrior:
    def __init__ (self):
        self.life=random.randint(105,120)
        self.skill=["Pierce"]*2+["Wave"]*2+["Tranple"]
        self.attack=[4]*2+[4]*2+[7]
        self.hit=70  
        self.trick=0
    def damaged(self,d):
        self.life -= d

    def special(self,p1,p2):
        m="{} has recovered 7 HP from the attack"
        print(m.format(p1.name))
        self.life+=7

class Bowman:
    def __init__ (self):
        self.life=random.randint(85,95)
        self.skill=["Shoot"]+["Discharge"]+["Snipe"]
        self.attack=[4]+[4]+[6]
        self.hit=85  
        self.trick=0
    def damaged(self,d):
        self.life -= d

    def special(self,p1,p2):
        m="{} has triggered multi_attack"
        print(m.format(p1.name))   
        battle(p1,p2)
        
class battle:
    def __init__ (self,p1,p2):
        skilln=random.randint(0,len(p1.oc.skill)-1)
        spn=random.randint(0,100)
        sk=p1.oc.skill[skilln]
        atta=p1.oc.attack[skilln]
        m="{} used {} ,and cause {}HP damage to {}"
        print(m.format(p1.name,sk,atta,p2.name))
        if random.randint(0,100) > p1.oc.hit:
            atta=0
            m="but missed"
            print(m)
        p2.oc.damaged(atta)
        if spn <=20 :
            p1.oc.special(p1,p2)
        

class Game:
    def __init__ (self):
        
        name1=input("player1 name:")
        oc1=input("player1 occupation(Magician/Warrior/Bowman):")
        name2=input("player2 name:")
        oc2=input("player2 occupation(Magician/Warrior/Bowman):")
        o1=self.chooseoc(oc1)
        o2=self.chooseoc(oc2)
        self.p1=player(name1,o1)
        self.p2=player(name2,o2)
        
    def wins(self,winner):
        m="{} has won!"
        print(m.format(winner))
        return
        
    def chooseoc(self,oc):
        if oc is "M":
            return Magician()
        if oc is "W":
            return Warrior()
        if oc is "B":
            return Bowman()
       
    def begin(self):    
        while (self.p1.oc.life)*(self.p2.oc.life) > 0:
            battle(self.p1,self.p2)
            m="{} life:{}       {} life:{}\n"
            print(m.format(self.p1.name,self.p1.oc.life,self.p2.name,self.p2.oc.life))
            time.sleep(2)
            if self.p2.oc.life <=0 :
                self.wins(self.p1.name)
                return
            battle(self.p2,self.p1)
            m="{} life:{}       {} life:{}\n"
            print(m.format(self.p1.name,self.p1.oc.life,self.p2.name,self.p2.oc.life))
            time.sleep(2)            
            if self.p1.oc.life <=0 :
                self.wins(self.p2.name)
                return
