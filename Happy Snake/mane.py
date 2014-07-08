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

#####################################################
class Mane(object):
    def __init__(self,surface):
        self.surface=surface
        
    def draw(self,a):
        pygame.draw.rect(self.surface, (60,40,0,110), (self.x, self.y, 25, 25), 0)
        pygame.draw.rect(self.surface, (60,40,0,110), (self.x+26, self.y, 25, 25), 0)
        pygame.draw.rect(self.surface, (60,40,0,110), (self.x+52, self.y, 25, 25), 0)
        pygame.draw.rect(self.surface, (60,40,0,110), (self.x+78, self.y, 25, 25), 0)
        pygame.draw.rect(self.surface, (60,40,0,110), (self.x+104, self.y, 25, 25), 0)
        pygame.draw.rect(self.surface, (60,40,0,110), (self.x+a, self.y+26, 25, 25), 0)
        
#####################################################

class Mane1(Mane):
    def __init__(self,surface):
        Mane.__init__(self,surface)
        self.x=90
        self.y=100

    def check(self,x,y):
        if self.x <=x <=self.x+129 and self.y<=y<=self.y+26:
             return True
        if self.x+52 <=x <=self.x+77 and self.y+26 <=y<=self.y+52:
            return True
        else:
            return False

########################################

class Mane2(Mane):
    def __init__(self,surface):
        Mane.__init__(self,surface)
        self.x=365
        self.y=230

    def check(self,x,y):
        
        if (self.x <= x <=self.x+129  and  self.y <=y<=self.y+26):
            return True
        if  (self.x+104<= x<=self.x+129 and self.y+26<= y<=self.y+52):
            return True
        else:
            return False

###############################

class Mane3(Mane):
    def __init__(self,surface):
        Mane.__init__(self,surface)
        self.x=90
        self.y=280
        
    def check(self,x,y):
        if self.x <=x <=self.x+129 and self.y<=y<=self.y+26:
             return True
        if self.x <=x <=self.x+26 and self.y+26 <=y<=self.y+52:
            return True
        else:
            return False

###############################

class Mane4(Mane):
    def __init__(self,surface):
        self.surface=surface
        self.x=365
        self.y=470
    
        
    def check(self,x,y):
        if self.x <=x <=self.x+129 and self.y<=y<=self.y+26:
             return True
        if self.x+52 <=x <=self.x+77 and self.y+26 <=y<=self.y+52:
            return True
        else:
            return False
##################################
class Sange(object):
    def __init__(self,surface,x,y):
        self.surface=surface
        self.x=x
        self.y=y
        self.color=60,40,0,110

    def draw(self):
        pygame.draw.rect(self.surface, (60,40,0,110), (self.x, self.y, 25, 25), 0)
        pygame.draw.rect(self.surface, (60,40,0,110), (self.x-26, self.y+25, 25, 25), 0)
        pygame.draw.rect(self.surface, (60,40,0,110), (self.x-51, self.y+51, 25, 25), 0)

    def check(self,x,y):
        if self.x<=x<=self.x+25 and self.y<=y<=self.y+25:
            return True
        if self.x-25<=x<=self.x and self.y+25<=y<self.y+50:
            return True
        if self.x-51<=x<=self.x-25 and self.y+50<=y<self.y+75:
            return True
        else:
            return False
