import pygame,time,random
import mane
from mane import *

joon=3
dir=1
width=600
height=600
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock() 
bgcolor =0,80,20
screen.fill(bgcolor)
#score = 0
qx=[]
qy=[]
wx=[]
wy=[]
rx=[]
ry=[]
cx=[]
cy=[]
ax=[]
ay=[]
bx=[]
by=[]
for i in range(75,235):
    qx.append(i)
for i in range(80,160):
    qy.append(i)

for i in range(350,510):
    wx.append(i)
for i in range(210,290):
    wy.append(i)

for i in range(75,235):
    rx.append(i)
for i in range(200,380):
    ry.append(i)

for i in range(110,210):
    bx.append(i)
for i in range(400,550):
    by.append(i)

for i in range(345,505):
    cx.append(i)
for i in range(450,520):
    cy.append(i)
    
for i in range(400,520):
    ax.append(i)
for i in range(40,220):
    ay.append(i)

#**************************************************************************
class Ghaza1:
    def __init__(self,x,y,color,surface,r):
        self.surface = surface
        self.x = random.randint(50, width-50)
        self.y = random.randint(50, height-50)
        self.color =color
        self.r=r
        
    def draw(self):
        while (self.x in qx and self.y in qy) or  (self.x in wx and self.y in wy) or (self.x in rx and self.y in ry) or (self.x in cx and self.y in cy) or (self.x in ax and self.y in ay) or (self.x in bx and self.y in by):
            self.x = random.randint(50, width-50)
            self.y = random.randint(150, height-50)
        pygame.draw.circle(self.surface, self.color, (self.x,self.y),self.r, 0)
               
    def erase(self):
        pygame.draw.circle(self.surface, bgcolor, (self.x, self.y),self.r, 0)
        
    def check(self,x,y):
        if (self.x-self.r<=x<=self.x+self.r) and (self.y-self.r<=y<=self.y+self.r):
            return True
        else :
            return False        
#**************************************************************************
        
class Ghaza2:
    def __init__(self,x,y,color,surface,a):
        self.surface = surface
        self.x = random.randint(50, width-50)
        self.y = random.randint(50, height-50)
        self.color =color
        self.a=a
        
    
    def draw(self):
        while (self.x in qx and self.y in qy) or  (self.x in wx and self.y in wy) or (self.x in rx and self.y in ry) or (self.x in cx and self.y in cy) or (self.x in ax and self.y in ay) or (self.x in bx and self.y in by) :
            self.x = random.randint(50, width-50)
            self.y = random.randint(150, height-50)
        pygame.draw.rect(self.surface, self.color, (self.x, self.y,self.a, self.a), 0)
        
    def erase(self):
        pygame.draw.rect(self.surface, bgcolor, (self.x, self.y,self.a, self.a), 0)
        
    
    def check(self,x,y):
        if x < self.x or x > self.x+self.a:
            return False
        elif y < self.y or y > self.y+self.a:
            return False
        else:
            return True

#**************************************************************************

class Food(Ghaza2):
    def __init__(self,x,y,color,surface,a):
        Ghaza2.__init__(self,x,y,color,surface,a)

class Ascore(Ghaza2):
    def __init__(self,x,y,color,surface,a):
        Ghaza2.__init__(self,x,y,color,surface,a)

class Energy(Ghaza1):
    def __init__(self,x,y,color,surface,r):
        Ghaza1.__init__(self,x,y,color,surface,r)

class Bomb(Ghaza1):
    def __init__(self,x,y,color,surface,r):
        Ghaza1.__init__(self,x,y,color,surface,r)

