import pygame
running1 = True
running2 = True
joon=3
dir=1
width=600
height=600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Happy Snake')
clock = pygame.time.Clock() 
bgcolor =0,80,20
screen.fill(bgcolor)
score = 0
class Emtiaz:
    def __init__(self,surface,x,y,color,i):
        self.surface=surface
        self.x=x
        self.y=y
        self.color=color
        self.i=i
        
    def draw(self,x,y,color,i):
        pygame.draw.rect(self.surface,color, (x,y,2*i,15), 0)

    def erase(self,x,y):
        pygame.draw.rect(self.surface,(80,0,20), (x,y,60,15), 0)
