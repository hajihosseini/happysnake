import pygame,time,random

#running = True
joon=3
dir=1
width=600
height=600
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock() 
bgcolor =0,80,20
screen.fill(bgcolor)
#score = 0

############################################

class Mar:
    def __init__(self,surface,x,y,length,color):
        self.surface = surface
        self.x = x
        self.y = y
        self.length = length
        self.dir_x = 0
        self.dir_y = -1
        self.body = []
        self.grow_to=50
        self.crashed = False
        self.color=color
        
    def eat(self):
        self.grow_to +=25


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
            

