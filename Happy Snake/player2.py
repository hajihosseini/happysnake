import pygame,time,random,sys
import mane,hashiye,mar,snake,emtiaz,food
from mar import *
from mane import *
from hashiye import *
from snake import *
from emtiaz import *
from food import *

running1 = True
running2 = True
joon1=3
joon2=3
dir=1
width=600
height=600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Happy Snake')
clock = pygame.time.Clock() 
bgcolor =0,80,20
screen.fill(bgcolor)
score1 = 0
score2=0

#******************************************************************#
#sound :                                
#******************************************************************#

pygame.mixer.init()
pygame.mixer.music.load('sound/music.ogg')# --> seda to paszamine
pygame.mixer.music.play(-1, 0.0)

#******************************************************************#
#object :
#******************************************************************#
sang=Sange(screen,470,80)
sang1=Sange(screen,180,450)
snake = Snake(screen,(width/3)+50 ,height/2 ,100,(255,255,255))
worm=Worm(screen,((2*width)/3)-100 ,height/2 ,100,(230,200,0))
ghaza=Food(random.randint(50, width-50), random.randint(50, height-50),(255,0,255),screen,8)
food=Food(random.randint(50, width-50), random.randint(50, height-50),(158,0,0),screen,7)
bomb=Bomb(random.randint(50, width-50),random.randint(50, height-50),(0,0,0),screen,6)
hashiye=Hashiye(screen)
mane1=Mane1(screen)
mane2=Mane2(screen)
mane3=Mane3(screen)
mane4=Mane4(screen)
energy=Energy(random.randint(50, width-50),random.randint(50, height-50),(0,255,0),screen,6)
ascore=Ascore(random.randint(50, width-50),random.randint(50, height-50),(0,0,255),screen,10)
emtiaz3=Emtiaz(screen,75,30,(255,255,255),60)
joon3=Emtiaz(screen,75,55,(255,255,255),60)
emtiaz4=Emtiaz(screen,75,30,(255,255,255),60)
joon4=Emtiaz(screen,75,55,(255,255,255),60)

#******************************************************************#
#Font :                                
#******************************************************************#

pygame.init()
pygame.font.init()
font1 = pygame.font.Font('Font/arial.ttf',15)
font2= pygame.font.Font('Font/arialbd.ttf',30)
text_Score1= font1.render("score:" ,0,(255,255,255))
text_Life1=font1.render('life :',0,(255,255,255))
text_Score2= font1.render("score:" ,0,(255,255,0))
text_Life2=font1.render('life :',0,(255,255,0))
text_worm=font1.render('worm',0,(255,255,0))
text_snake=font1.render('snake',0,(255,255,255))
text_sWin=font2.render('snake is winner!',1,(255,0,40))
text_wWin=font2.render('worm is winner!',1,(255,0,40))

#******************************************************************#
#Ejraye bazi :                             
#******************************************************************#

while running1 and running2 :
    screen.blit(text_Score1, (22, 35))    
    screen.blit(text_Life1, (22,60))
    screen.blit(text_snake, (22, 20))    
    screen.blit(text_worm, (300,20))
    screen.blit(text_Score2, (300,35))    
    screen.blit(text_Life2, (300,60))
    worm.move()
    worm.draw()
    snake.move()
    snake.draw()
    emtiaz3.erase(75,40)
    emtiaz3.draw(75,40,(255,255,255),score1)
    joon3.erase(75,65)
    joon3.draw(75,65,(0,128,0),5*joon1)
    emtiaz4.erase(350,40)
    emtiaz4.draw(350,40,(255,255,255),score2)
    joon4.erase(350,65)
    joon4.draw(350,65,(0,128,0),5*joon2)
    food.draw()
    bomb.draw()
    ghaza.draw()
    mane1.draw(52)
    mane2.draw(104)
    mane3.draw(0)
    mane4.draw(52)
    sang.draw()
    sang1.draw()
    ascore.draw()
    hashiye.draw()

    if joon1 <6 or joon2 <6:
        energy.draw()
        
#******************************************************************#
#Worm and Snake :                         
#******************************************************************#
#dar in 2 ghesmat barkhord mar ha ba khodeshan baresi mishavad .

    if worm.crashed:
       pygame.mixer.music.stop()
       running2 = False
       running1 = False
       print "snake is winner"
       screen.blit(text_sWin,(200,285))
       
    if snake.crashed:
       pygame.mixer.music.stop()
       running2 = False
       running1 = False
       print "worm is winner"
       screen.blit(text_wWin,(200,285))

#dar in 2 ghesmat barkhord mar ha ba yekdighar baresi mishavad .

    if snake.barkhord(worm.x,worm.y):
        screen.fill(bgcolor)
        worm=Worm(screen,((2*width)/3)-100 ,height/2 ,100,(230,200,0))
        joon2 -=1
        if joon2 == 0:
            pygame.mixer.music.stop()
            running2 = False
            running1 = False
            print "snake is winner"
            screen.blit(text_sWin,(200,285))

    if worm.barkhord(snake.x,snake.y):
        screen.fill(bgcolor)
        snake = Snake(screen,(width/3)+50 ,height/2 ,100,(255,255,255))
        joon1 -=1
        if joon1 == 0:
            pygame.mixer.music.stop()
            running2 = False
            running1 = False
            print "worm is winner"
            screen.blit(text_wWin,(200,285))

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
        worm=Worm(screen,((2*width)/3)-100 ,height/2 ,100,(230,200,0))
        joon2-=1
        if joon2==0:
            pygame.mixer.music.stop()
            running2 = False
            print "snake is winner"
            screen.blit(text_sWin,(200,285))

#dar in ghesmat barkhord be hashiyeha check mishavad .
#4 mored aval ghesmathayist ke dar hashiye tonel gozashte shode ast.

    elif snake.x <=20 and 274<snake.y<326:
        snake.x = width-20
            
    elif  snake.x >= width-20 and  274<snake.y<326 :
        snake.x=20
    
    elif snake.y <=20 and 274<snake.x<326:
        snake.y=height-20

    elif snake.y >=height -20 and 274<snake.x<326:
        snake.y = 20

#dar in ghesmat aghar be hashiye barkhord konad yek vahed az joon kam mishavad .

    elif (snake.x <=20 and (274>snake.y or snake.y>326)) or (snake.x >= width-20 and  (274>snake.y or snake.y>326)) or (snake.y <=20 and (274>snake.x or snake.x>326)) or (snake.y >=height -20 and (274>snake.x or snake.y>326)):
        screen.fill(bgcolor)
        snake = Snake(screen,(width/3)+50 ,height/2 ,100,(255,255,255))
        joon1-=1
        if joon1==0:
            pygame.mixer.music.stop()
            running1 = False
            print "worm is winner"
            screen.blit(text_wWin,(200,285))

#*****************************************************************#
#Food :                                 
#*****************************************************************#  
#dar in ghesmat barkhord be foodha chek mishavad dar sorat barkhord be food1 score 1 vahed va food2 score 3 vahed ziyad mishavad  .        
 
        
    elif food.check(worm.x,worm.y):
        score2 += 1
        if score2 >=30:
            pygame.mixer.music.stop()
            running2 = False
            running1 = False
            print 'worm is winner'
            screen.blit(text_wWin,(200,285))
        worm.eat()
        print "Score2: %d" % score2
        food.erase()
        food=Food(random.randint(50, width-50), random.randint(50, height-50),(158,0,0),screen,7)

    elif food.check(snake.x,snake.y):
        score1 += 1
        if score1 >=30:
            pygame.mixer.music.stop()
            running1 = False
            running2 = False
            print 'snake is winner'
            screen.blit(text_sWin,(200,285))
        snake.eat()
        print "Score1: %d" % score1
        food.erase()
        food=Food(random.randint(50, width-50), random.randint(50, height-50),(158,0,0),screen,7)

#*****************************************************************#
#Food :                                
#*****************************************************************#
#in ja barkhord ba ghaza check mishavad dar sorat barkhord score 3 vahed ziad mishavad .

    elif ghaza.check(worm.x,worm.y):
        score2 += 3
        if score2 >=30:
            pygame.mixer.music.stop()
            running2 = False
            running1 = False
            print 'worm is winner'
            screen.blit(text_wWin,(200,285))
        worm.eat()
        print "Score1: %d" % score1
        ghaza.erase()
        ghaza=Food(random.randint(50, width-50), random.randint(50, height-50),(255,0,255),screen,8)

    elif ghaza.check(snake.x,snake.y):
        score1 += 3
        if score1 >=30:
            pygame.mixer.music.stop()
            running1 = False
            running2 = False
            print 'snake is winner'
            screen.blit(text_sWin,(200,285))
        snake.eat()
        print "Score2: %d" % score2
        ghaza.erase()
        ghaza=Food(random.randint(50, width-50), random.randint(50, height-50),(255,0,255),screen,8)
        

#******************************************************************#
#Bomb :                                 
#******************************************************************#
#dar in ghesmat barkhord be bomb baresi mishe ke dar sorat barkhord score 5 vahed va joon 1 vahed kam mishavad .

    elif bomb.check(worm.x,worm.y):
        if score2 > 5:
            score2 -=5
        else:
            score2 =0
        joon2 -=1
        if joon2 == 0:
            pygame.mixer.music.stop()
            running2 = False
            running1 = False
            print "snake is winner"
            screen.blit(text_sWin,(200,285))
        print "Score2: %d" % score2
        bomb.erase()
        screen.fill(bgcolor)
        worm=Worm(screen,((2*width)/3)-100 ,height/2 ,100,(230,200,0))
        bomb=Bomb(random.randint(50, width-50),random.randint(50, height-50),(0,0,0),screen,6)
    
    elif bomb.check(snake.x,snake.y):
        if score1 > 5:
            score1 -=5
        else:
            score1 =0
        joon1 -=1
        if joon1 == 0:
            pygame.mixer.music.stop()
            running1 = False
            running2 = False
            print "worm is winner"
            screen.blit(text_wWin,(200,285))
        print "Score1: %d" % score1
        bomb.erase()
        screen.fill(bgcolor)
        snake = Snake(screen,(width/3)+50 ,height/2 ,100,(255,255,255))
        bomb=Bomb(random.randint(50, width-50),random.randint(50, height-50),(0,0,0),screen,6)

#******************************************************************#
# Mane ha :
#******************************************************************#

    elif mane1.check(worm.x,worm.y)==True:
        score2=0
        screen.fill(bgcolor)
        worm=Worm(screen,(2*width)/3 ,height/2 ,100,(230,200,0))
        joon2 -=1
        if joon2 == 0:
            pygame.mixer.music.stop()
            running2 = False
            running1 = False
            print "snake is winner"
            screen.blit(text_sWin,(200,285))

    elif mane1.check(snake.x,snake.y)==True:
        score1=0
        screen.fill(bgcolor)
        snake = Snake(screen,(width/3)+50 ,height/2 ,100,(255,255,255))
        joon1 -=1
        if joon1 == 0:
            pygame.mixer.music.stop()
            running2 = False
            running1 = False
            print "worm is winner"
            screen.blit(text_wWin,(200,285))


    elif mane2.check(worm.x,worm.y)==True:
        score2=0
        screen.fill(bgcolor)
        worm=Worm(screen,((2*width)/3)-100 ,height/2 ,100,(230,200,0))
        joon2 -=1
        if joon2 == 0:
            pygame.mixer.music.stop()
            running2 = False
            running1 = False
            print "snake is winner"
            screen.blit(text_sWin,(200,285))

    elif mane2.check(snake.x,snake.y)==True:
        score1=0
        screen.fill(bgcolor)
        snake = Snake(screen,(width/3)+50 ,height/2 ,100,(255,255,255))
        joon1 -=1
        if joon1 == 0:
            pygame.mixer.music.stop()
            running2 = False
            running1 = False
            print "worm is winner"
            screen.blit(text_wWin,(200,285))

    elif mane3.check(worm.x,worm.y)==True:
        score2=0
        screen.fill(bgcolor)
        worm=Worm(screen,((2*width)/3)-100 ,height/2 ,100,(230,200,0))
        joon2 -=1
        if joon2 == 0:
            pygame.mixer.music.stop()
            running2 = False
            running1 = False
            print "snake is winner"
            screen.blit(text_sWin,(200,285))

    elif mane3.check(snake.x,snake.y)==True:
        score1=0
        screen.fill(bgcolor)
        snake = Snake(screen,(width/3)+50 ,height/2 ,100,(255,255,255))
        joon1 -=1
        if joon1 == 0:
            pygame.mixer.music.stop()
            running2 = False
            running1 = False
            print "worm is winner"
            screen.blit(text_wWin,(200,285))

    elif mane4.check(worm.x,worm.y)==True:
        score2=0
        screen.fill(bgcolor)
        worm=Worm(screen,((2*width)/3)-100 ,height/2 ,100,(230,200,0))
        joon2 -=1
        if joon2 == 0:
            pygame.mixer.music.stop()
            running2 = False
            running1 = False
            print "snake is winner"
            screen.blit(text_sWin,(200,285))

    elif mane4.check(snake.x,snake.y)==True:
        score1=0
        screen.fill(bgcolor)
        snake = Snake(screen,(width/3)+50 ,height/2 ,100,(255,255,255))
        joon1 -=1
        if joon1 == 0:
            pygame.mixer.music.stop()
            running2 = False
            running1 = False
            print "worm is winner"
            screen.blit(text_wWin,(200,285))
            
    elif sang.check(snake.x,snake.y)==True:
        score=0
        screen.fill(bgcolor)
        snake = Snake(screen,(width/3)+50 ,height/2 ,100,(255,255,255))
        joon -=1
        if joon == 0:
            pygame.mixer.music.stop()
            running1 = False
            print "game over"
            screen.blit(text_los,(200,280))

    elif sang1.check(snake.x,snake.y)==True:
        score=0
        screen.fill(bgcolor)
        snake = Snake(screen,(width/3)+50 ,height/2 ,100,(255,255,255))
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
        if joon2<6:
            joon2 +=1
            energy.erase()
            energy=Energy(random.randint(50, width-50),random.randint(50, height-50),(0,255,0),screen,6)

    elif energy.check(snake.x,snake.y)==True:
        if joon1<6:
            joon1 +=1
            energy.erase()
            energy=Energy(random.randint(50, width-50),random.randint(50, height-50),(0,255,0),screen,6)

#******************************************************************#
#Ascore :                              
#******************************************************************#
#akharin noe ghaza ascore ast ke score ra 2 vahed ziyad mikonad . 

    elif ascore.check(worm.x,worm.y):
        score2 += 2
        worm.eat()
        print "Score2: %d" % score2
        ascore.erase()
        ascore=Ascore(random.randint(50, width-50),random.randint(50, height-50),(0,0,255),screen,10)
        if score2 >=30:
            pygame.mixer.music.stop()
            running2 = False
            running1 = False
            print 'worm is win'
            screen.blit(text_wWin,(200,285))

    elif ascore.check(snake.x,snake.y):
        score1 += 2
        snake.eat()
        print "Score1: %d" % score1
        ascore.erase()
        ascore=Ascore(random.randint(50, width-50),random.randint(50, height-50),(0,0,255),screen,10)
        if score1 >=30:
            pygame.mixer.music.stop()
            running1 = False
            running2 = False
            print 'snake is win'
            screen.blit(text_sWin,(200,285))

#******************************************************************#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            running1 = False
            running2 = False
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            worm.event(event)
            snake.event(event)

    pygame.display.flip()
    clock.tick(100)        
