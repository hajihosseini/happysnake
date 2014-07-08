import mar
from mar import*
running1 = True
running2 = True
###############################################
pygame.init()
pygame.font.init()
font1 = pygame.font.Font('Font/arial.ttf',15)
font2= pygame.font.Font('Font/arialbd.ttf',30)
font3= pygame.font.Font('Font/ariblk.ttf',20)
text_Win=font2.render('Win!',1,(255,0,40))
text_sWin=font2.render('snake is winner!',1,(255,0,40))
text_wWin=font2.render('worm is winner!',1,(255,0,40))
text_Score= font1.render(" score:" ,0,(255,255,255))
text_Life=font1.render('life :',0,(255,255,255))
text_Pause = font2.render("Pause",1, (0,255,0))
###############################################
class Worm(Mar):

    def __init__(self,surface,x,y,length,color):

        Mar.__init__(self,surface,x,y,length,color)

    def event(self,event):
        if event.key == pygame.K_UP:
            if self.dir_y == 1: return
            self.dir_x = 0
            self.dir_y = -1
        elif event.key == pygame.K_DOWN:
            if self.dir_y == -1:return
            self.dir_x = 0
            self.dir_y = 1
        elif event.key == pygame.K_LEFT:
            if self.dir_x==1: return 
            self.dir_x = -1
            self.dir_y = 0
        elif event.key == pygame.K_RIGHT:
            if self.dir_x==-1: return 
            self.dir_x = 1
            self.dir_y = 0
        
    
#####################################################

class Snake(Mar):

    def __init__(self,surface,x,y,length,color):

        Mar.__init__(self,surface,x,y,length,color)

    def event(self,event):
        if event.key == pygame.K_w:
            if self.dir_y == 1: return
            self.dir_x = 0
            self.dir_y = -1
        elif event.key == pygame.K_s:
            if self.dir_y == -1:return
            self.dir_x = 0
            self.dir_y = 1
        elif event.key == pygame.K_a:
            if self.dir_x==1: return 
            self.dir_x = -1
            self.dir_y = 0
        elif event.key == pygame.K_d:
            if self.dir_x==-1: return 
            self.dir_x = 1
            self.dir_y = 0
        
###############################################################

