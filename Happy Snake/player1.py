import pygame,time,random,sys
import snake,mane,hashiye,mar,emtiaz,food
from mar import*
from snake import *
from mane import*
from hashiye import *
from emtiaz import *
from food import *


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

s=Mane1(screen)
t=Mane2(screen)
p=Mane3(screen)

#******************************************************************#
sang=Sange(screen,470,80)
sang1=Sange(screen,180,450)
worm=Worm(screen,width/2 ,height/2 ,100,(230,200,0))
food1=Food(random.randint(50, width-50), random.randint(50, height-50),(158,0,0),screen,7)
food2=Food(random.randint(50, width-50), random.randint(50, height-50),(255,0,255),screen,8)
bomb=Bomb(random.randint(50, width-50),random.randint(50, height-50),(0,0,0),screen,5)
hashiye=Hashiye(screen)
mane1=Mane1(screen)
mane2=Mane2(screen)
mane3=Mane3(screen)
mane4=Mane4(screen)
energy=Energy(random.randint(50, width-50),random.randint(50, height-50),(0,255,0),screen,5)
ascore=Ascore(random.randint(50, width-50),random.randint(50, height-50),(0,0,255),screen,10)
emtiaz=Emtiaz(screen,75,30,(255,255,255),60)
joon1=Emtiaz(screen,75,55,(255,255,255),60)

#******************************************************************#
#sound :
#******************************************************************#

pygame.mixer.init()
pygame.mixer.music.load('sound/music.ogg')# --> seda to paszamine
pygame.mixer.music.play(-1, 0.0)

#******************************************************************#
#Font :                                                                     
#******************************************************************#


pygame.init()
pygame.font.init()
font1 = pygame.font.Font('Font/arial.ttf',15)
font2 = pygame.font.Font('Font/arialbd.ttf',40)
text_Score= font1.render("score:" ,0,(255,255,255))
text_Life=font1.render('life :',0,(255,255,255))
text_win=font2.render('Win!',0,(255,255,255))
text_los=font2.render('Game Over!',0,(255,255,255))

#******************************************************************#
#Ejraye bazi :                                                          
#******************************************************************#

while running1:
    worm.move()
    worm.draw()
    emtiaz.erase(75,30)
    emtiaz.draw(75,30,(255,255,255),score)
    joon1.erase(75,55)
    joon1.draw(75,55,(0,128,0),5*joon)
    food1.draw()
    food2.draw()
    bomb.draw()
    ascore.draw()
    mane1.draw(52)
    mane2.draw(104)
    mane3.draw(0)
    mane4.draw(52)
    sang.draw()
    sang1.draw()
    hashiye.draw()
    screen.blit(text_Score, (22, 30))    
    screen.blit(text_Life, (22,50))
    if joon <6:
        energy.draw()
    if worm.crashed:
       pygame.mixer.music.stop() 
       running1 = False
       print "game over"
       screen.blit(text_los,(200,280))
#******************************************************************#
#Worm :
#******************************************************************#

#dar in ghesmat barkhord be hashiyeha check mishavad .
#4 mored aval ghesmathayist ke dar hashiye tonel gozashte shode ast. 

    elif worm.x <=20 and 274<worm.y<326:
        worm.x = width-20
            
    elif  worm.x >= width-20 and  274<worm.y<326 :
        worm.x=20
    
    elif worm.y <=20 and 274<worm.x<326:
        worm.y=height-20

    elif worm.y >=height -20 and 274<worm.x<326:
        worm.y = 20

#dar in ghesmat aghar be hashiye barkhord konad yek vahed az joon kam mishavad .
        
    elif (worm.x <=20 and (274>worm.y or worm.y>326)) or (worm.x >= width-20 and  (274>worm.y or worm.y>326)) or (worm.y <=20 and (274>worm.x or worm.x>326)) or (worm.y >=height -20 and (274>worm.x or worm.y>326)):
        screen.fill(bgcolor)
        worm=Worm(screen,width/2 ,height/2 ,100,(230,200,0))
        joon-=1
        if joon==0:
            pygame.mixer.music.stop()
            running1 = False
            print "game over"
            screen.blit(text_los,(200,280))
        
#*****************************************************************#
#Food :                                                            
#*****************************************************************#
#dar in ghesmat barkhord be foodha chek mishavad dar sorat barkhord be food1 score 1 vahed va food2 score 3 vahed ziyad mishavad  .

    elif food1.check(worm.x,worm.y):
        score += 1
        if score >=30:
            pygame.mixer.music.stop()
            running1 = False
            print 'win'
            screen.blit(text_win,(294,300))

        worm.eat()
        print "Score: %d" % score
        food1.erase()
        food1=Food(random.randint(50, width-50), random.randint(50, height-50),(158,0,0),screen,7)

    elif food2.check(worm.x,worm.y):
        score += 3
        if score >=30:
            pygame.mixer.music.stop()
            running1 = False
            print 'win'
            screen.blit(text_win,(294,300))

        worm.eat()
        print "Score: %d" % score
        food2.erase()
        food2=Food(random.randint(50, width-50), random.randint(50, height-50),(255,0,255),screen,8)
        
#******************************************************************#
#Bomb :                                                              
#******************************************************************#
#dar in ghesmat barkhord be bomb baresi mishe ke dar sorat barkhord score 5 vahed va joon 1 vahed kam mishavad .

    elif bomb.check(worm.x,worm.y):
        if score > 5:
            score -=5
        else:
            score =0
        joon -=1
        if joon == 0:
            pygame.mixer.music.stop()
            running1 = False
            print "game over"
            screen.blit(text_los,(200,280))
        print "Score: %d" % score
        bomb.erase()
        screen.fill(bgcolor)
        worm =Worm(screen,width/2 ,height/2 ,100,(230,200,0))
        bomb=Bomb(random.randint(50, width-50),random.randint(50, height-50),(0,0,0),screen,5)

#******************************************************************#
#Mane ha :                                                             
#******************************************************************#
#dar in ja barkhord be mane ha check mishavad
#dar sorat barkhord be har yek az mane ha score 0 shode az joon yek vahed kam mishavad .

    elif mane1.check(worm.x,worm.y)==True:
        score=0
        screen.fill(bgcolor)
        worm = Worm(screen,width/2 ,height/2 ,100,(230,200,0))
        joon -=1
        if joon == 0:
            running1 = False
            pygame.mixer.music.stop()
            print "game over"
            screen.blit(text_los,(200,280))

    elif mane2.check(worm.x,worm.y)==True:
        score=0
        screen.fill(bgcolor)
        worm=Worm(screen,width/2 ,height/2 ,100,(230,200,0))
        joon -=1
        if joon == 0:
            pygame.mixer.music.stop()
            running1 = False
            print "game over"
            screen.blit(text_los,(200,280))

    elif mane3.check(worm.x,worm.y)==True:
        score=0
        screen.fill(bgcolor)
        worm=Worm(screen,width/2 ,height/2 ,100,(230,200,0))
        joon -=1
        if joon == 0:
            pygame.mixer.music.stop()
            running1 = False
            print "game over"
            screen.blit(text_los,(200,280))

    elif mane4.check(worm.x,worm.y)==True:
        score=0
        screen.fill(bgcolor)
        worm=Worm(screen,width/2 ,height/2 ,100,(230,200,0))
        joon -=1
        if joon == 0:
            pygame.mixer.music.stop()
            running1 = False
            print "game over"
            screen.blit(text_los,(200,280))
            
    elif sang.check(worm.x,worm.y)==True:
        score=0
        screen.fill(bgcolor)
        worm=Worm(screen,width/2 ,height/2 ,100,(230,200,0))
        joon -=1
        if joon == 0:
            pygame.mixer.music.stop()
            running1 = False
            print "game over"
            screen.blit(text_los,(200,280))

    elif sang1.check(worm.x,worm.y)==True:
        score=0
        screen.fill(bgcolor)
        worm=Worm(screen,width/2 ,height/2 ,100,(230,200,0))
        joon -=1
        if joon == 0:
            pygame.mixer.music.stop()
            running1 = False
            print "game over"
            screen.blit(text_los,(200,280))
#******************************************************************#
#Energy :                                                               
#******************************************************************#
#yeki az anvae ghaza ha energyist ke be joon yek vahed ezafe mikonad va dar in ja barkhord be an check mishavad .

    elif energy.check(worm.x,worm.y)==True:
        if joon<6:
            joon+=1
            energy.erase()
            energy=Energy(random.randint(50, width-50),random.randint(50, height-50),(0,255,0),screen,5)

#******************************************************************#
#Ascore :                                                              
#******************************************************************#
#akharin noe ghaza ascore ast ke score ra 2 vahed ziyad mikonad .

    elif ascore.check(worm.x,worm.y):
        score += 2
        worm.eat()
        print "Score: %d" % score
        ascore.erase()
        ascore=Ascore(random.randint(50, width-50),random.randint(50, height-50),(0,0,255),screen,10)
        if score >=30:
            pygame.mixer.music.stop()
            running1 = False
            print 'win'
            screen.blit(text_win,(294,300))

#*************************************************

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            running1 = False
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            worm.event(event)

    pygame.display.flip()
    clock.tick(100)



