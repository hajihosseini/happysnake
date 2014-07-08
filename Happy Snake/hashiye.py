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

class Hashiye(object):
    def __init__(self,surface):
        self.surface=surface
        self.color=0,60,0

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (0, 0, 20, 275), 0)
        pygame.draw.rect(self.surface, bgcolor, (0, 275, 20, 50), 0)
        pygame.draw.rect(self.surface, self.color, (0, 325, 20, 275), 0)
        
        pygame.draw.rect(self.surface, self.color, (0,580,275,20), 0)
        pygame.draw.rect(self.surface,bgcolor, (275,580,50,20), 0)
        pygame.draw.rect(self.surface, self.color, (325,580,275,20), 0)
        
        pygame.draw.rect(self.surface, self.color, (580,0,20,275), 0)
        pygame.draw.rect(self.surface,bgcolor, (580,275,20,50), 0)
        pygame.draw.rect(self.surface, self.color, (580,325,20,275), 0)
        
        pygame.draw.rect(self.surface, self.color, (0,0,275,20), 0)
        pygame.draw.rect(self.surface,bgcolor, (275,0,50,20), 0)
        pygame.draw.rect(self.surface, self.color, (325,0,275,20), 0)
        
        
