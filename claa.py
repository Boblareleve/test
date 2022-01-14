import pygame
import random


if False :
        for i in range(len(ennemies)-1):
            for k in range(0,int((601-ennemies[i].w)/(ennemies[i].w+10))):
                if k*(ennemies[i].w+10)<i.posx<k*(ennemies[i].w+10)+(ennemies[i].w+10) and 0<=i.posy<=ennemies[i].h+10:
                    pass
                else : 
                    ennemies[len(ennemies)-1].posx = k*(ennemies[len(ennemies)-1].w+10)
                    ennemies[len(ennemies)-1].posy = 0
                    break

class player :
    def __init__(self) -> None:
        self.image = pygame.image.load("logo.png")
        self.h = self.image.get_height()
        self.w = self.image.get_width()
        self.posx = 300-(self.w/2)
        self.posy = 540-(self.h/2)
        self.HP = 20
        
    def dépdroite(self,chan):
        if 600-self.w>=self.posx:
            self.posx+=chan
    def dépgauche(self,chan):
        if 0<=self.posx:
            self.posx-=chan
    def déphaut(self,chan):
        if 400<=self.posy:
            self.posy-=chan
    def dépbas(self,chan):
        if 630-self.h>=self.posy:
            self.posy+=chan

class ennemie_type :
    def __init__(self,HP,image) -> None:
        self.HP = HP
        self.image = pygame.image.load(image)
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        

class ennemie :
    def __init__(self,type,x,y) -> None:
        self.HP = type.HP
        self.image = type.image
        self.w = type.w
        self.h = type.h
        self.posx = x
        self.posy = y

    
        
    
    def setPosx(self, x):
        self.posx = x
    def setPosy(self,y):
        self.posy = y
    def getPosx(self):
        return self.posx
    def getPosy(self):
        return self.posy
    def getImage(self):
        return self.image
    
    def IA_tick(self):
        
        self.posx
        self.posy