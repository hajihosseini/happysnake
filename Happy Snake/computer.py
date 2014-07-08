import pygame,random,math
import snake
from snake import *
from math import *


bgcolor=0,80,20
class Computer:
    def __init__(self,surface,x,y,length):
        self.surface = surface
        self.x = x
        self.y = y
        self.length = length
        self.dir_x = 0
        self.dir_y = -1
        self.body = []
        self.grow_to=50
        self.crashed = False
        self.start = True
        self.color=255,255,255

    def eat(self):
        self.grow_to +=25

    def control(self,dx,dy):
        
        
        if dx==0:
            if dy<0:
                self.dir_x=0
                self.dir_y=1
                return   
            if dy>0:
                self.dir_x=0
                self.dir_y=-1
                return   
                            
        if dy==0:
            if dx<0:
                self.dir_x=1
                self.dir_y=0
                return
            
            if dx>0:
                self.dir_x=-1
                self.dir_y=0
                return
                
        if dx>0:
            if self.dir_x!=1:
                self.dir_x=-1
                self.dir_y=0
                return
            
        if dx<0:
            if self.dir_x!=-1:
                self.dir_x=1
                self.dir_y=0
                return
            
        if dy>0:
            if self.dir_y!=1:
                self.dir_x=0
                self.dir_y=-1
                return
            
        if dy<0:
            if self.dir_y!=-1:
                self.dir_x=0
                self.dir_y=1
                return
         
    def move(self):
        self.x += self.dir_x
        self.y += self.dir_y

        if (self.x , self.y) in self.body:
            self.crashed = True
            
        self.body.insert(0, (self.x ,self.y))

        if (self.grow_to >self.length):
            self.length +=1

        if len(self.body) > self.length:
            self.body.pop()

    def draw(self):
        x , y = self.body[0]
        self.surface.set_at((x, y), self.color)
        x, y =self.body[-1]
        self.surface.set_at((x, y), bgcolor)

    def barkhord(self,a,b):
        if (a,b) in self.body:
            return True
        return False


                
                
        
