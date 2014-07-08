import pygame,time,random,sys,snake
from pygame.locals import *

pygame.init()
running = True
joon=3
dir=1
width=600
height=600
screen = pygame.display.set_mode((width,height))
screen1= pygame.display.set_mode((width,height))
clock = pygame.time.Clock() 
bgcolor =0,0,0
screen.fill(bgcolor)
pygame.font.init()
#-------------------------------------------
background_main = pygame.image.load('image/8.jpg').convert()
screen.blit(background_main,(0,0))
#-------------------------------------------
font1 = pygame.font.Font('Font/arial.ttf',15)
font2= pygame.font.Font('Font/arialbd.ttf',20)
font3= pygame.font.Font('Font/ariblk.ttf',25)
font4= pygame.font.Font('Font/arialbd.ttf',15)
#-------------------------------------------
text_happy= font3.render("Happy",0,(200,200,0))
text_snake= font3.render("Snake",0,(100,200,50))
text_play= font2.render("Play",0,(0,0,0))
text_help= font2.render("Help",0,(0,0,0))
text_about= font2.render("About",0,(0,0,0))
text_exit= font2.render("Exit",0,(0,0,0))
text_mail= font1.render("happysnake.2014@gmail.com",1,(255,50,100))
screen.blit(text_play,(280,240))
screen.blit(text_help,(280,300))
screen.blit(text_about,(270,360))
screen.blit(text_exit,(280,420))
screen.blit(text_happy,(220,75))
screen.blit(text_snake,(320,75))
screen.blit(text_mail,(210,460))
#-------------------------------------------
text_1player= font2.render("1player",0,(0,0,0))
text_2player= font2.render("2player",0,(0,0,0))
text_2player_co = font2.render("2player-co",0,(0,0,0))
#text_2player_net = font2.render("2player-net",0,(0,0,0))
text_back= font2.render("Back",0,(0,0,0))
#-------------------------------------------
text_a= font4.render("Red square :This is food. The score is increased by one.",1,(0,0,0))
text_b= font4.render("Blue square :This is food. The score is increased by two.",1,(0,0,0))
text_c= font4.render("Pink square :This is food. The score is increased by three.",1,(0,0,0))
text_d= font4.render("Green circle:Life is increased by one if it is less than 6.",1,(0,0,0))
text_e= font4.render("Black circle:This is a bomb! The score is decreased by",1,(0,0,0))
text_f= font4.render("five and the life is reduced by one.",1,(0,0,0))
text_g= font4.render("Brown block:The score is changed to zero and the life",1,(0,0,0))
text_p= font4.render("is reduced by one.",1,(0,0,0))
#--------------------------------------------
text_h= font4.render("Application:Happy Snake",1,(0,0,0))
text_i= font4.render("Version:14.1",1,(0,0,0))
text_j= font4.render("Options:Single player/two players/one player against computer",1,(0,0,0))
text_k= font4.render("Last modification: 2014.01.21",1,(0,0,0))
text_l= font4.render("Developer team:",1,(0,0,0))
text_m= font4.render("Malihe HajiHosseini",1,(0,0,0))
text_n= font4.render("Zahra Hamze",1,(0,0,0))
text_o= font4.render("Zahra Momeni",1,(0,0,0))
#-------------------------------------------
scrn1=True
scrn0=True
scrn2=False
scrn3=False
scrn4=False

while scrn0:
    while scrn1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
                pygame.quit()
                sys.exit()

                
            elif event.type == pygame.KEYDOWN:
                worm.event(event)
        pygame.display.flip()
        clock.tick(100)
#----------------------------------------   
        p=pygame.mouse.get_pos()
        ev =pygame.event.wait()
        if ev.type == 5 and 250<=p[0]<=310 and 210<=p[1]<=265:
            print 'play'
            screen.blit(background_main,(0,0))
            screen.blit(text_1player,(260,180))
            screen.blit(text_2player,(260,240))
            screen.blit(text_2player_co,(250,300))
            #screen.blit(text_2player_net,(250,360))
            screen.blit(text_back,(270,420))
            pygame.display.flip()
            scrn1=False
            scrn2=True
            
        elif ev.type == 5 and 250<=p[0]<=320 and 270<=p[1]<=325:
            print "help"
            screen.blit(background_main,(0,0))
            screen.blit(text_h,(130,210))
            screen.blit(text_i,(130,240))
            screen.blit(text_j,(110,270))
            screen.blit(text_k,(130,300))
            screen.blit(text_l,(130,330))
            screen.blit(text_m,(160,360))
            screen.blit(text_n,(160,390))
            screen.blit(text_o,(160,420))
            screen.blit(text_back,(280,520))
            pygame.display.flip()
            scrn1=False
            scrn2=True
            scrn3=True
        elif ev.type == 5 and 250<=p[0]<=310 and 345<=p[1]<=375:
            print "about"
            screen.blit(background_main,(0,0))
            screen.blit(text_a,(130,180))
            screen.blit(text_b,(130,210))
            screen.blit(text_c,(130,240))
            screen.blit(text_d,(130,270))
            screen.blit(text_e,(130,300))
            screen.blit(text_f,(150,320))
            screen.blit(text_g,(130,350))
            screen.blit(text_p,(150,370))
            screen.blit(text_back,(280,490))
            pygame.display.flip()
            scrn1=False
            scrn2=True
            scrn4=True    
        elif ev.type == 5 and 250<=p[0]<=310 and 390<=p[1]<=450:
            print "exit"
            scrn1=False
            scrn0=False
            pygame.quit()

    while scrn2:    
        q=pygame.mouse.get_pos()
        ko=pygame.event.wait()
        if ko.type == 5 and 220<=q[0]<=320 and 150<=q[1]<=210:
            print '1player'
            execfile('player1.py')
            pygame.display.flip()
        elif ko.type == 5 and 220<=q[0]<=320 and 215<=q[1]<=270:
            print "2player"
            execfile('player2.py')
            pygame.display.flip()
        elif ko.type == 5 and 220<=q[0]<=320 and 275<=q[1]<=330:
            print "2player_co"
            execfile('player2.AI.py')
            pygame.display.flip()

       # elif ko.type == 5 and 220<=q[0]<=320 and 335<=q[1]<=390:
            print "2player_net"
            screen1.fill(bgcolor)
            pygame.display.flip()

        elif ko.type == 5 and 220<=q[0]<=330 and 395<=q[1]<=450:
            print 'back'
            screen.blit(background_main,(0,0))
            screen.blit(text_play,(280,240))
            screen.blit(text_help,(280,300))
            screen.blit(text_about,(270,360))
            screen.blit(text_exit,(280,420))
            screen.blit(text_happy,(220,75))
            screen.blit(text_snake,(320,75))
            screen.blit(text_mail,(210,460))
            pygame.display.flip()
            scrn1=True
            scrn2=False
        while scrn3:
             h=pygame.mouse.get_pos()
             jo=pygame.event.wait()
             if jo.type == 5 and 230<=h[0]<=340 and 480<=h[1]<=550:
                print 'back'
                screen.blit(background_main,(0,0))
                screen.blit(text_play,(280,240))
                screen.blit(text_help,(280,300))
                screen.blit(text_about,(270,360))
                screen.blit(text_exit,(280,420))
                screen.blit(text_happy,(220,75))
                screen.blit(text_snake,(320,75))
                screen.blit(text_mail,(210,460))
                pygame.display.flip()
                scrn1=True
                scrn2=False
                scrn3=False
        while scrn4:
             l=pygame.mouse.get_pos()
             lo=pygame.event.wait()
             if lo.type == 5 and 230<=l[0]<=340 and 470<=l[1]<=510:
                print'back'
                screen.blit(background_main,(0,0))
                screen.blit(text_play,(280,240))
                screen.blit(text_help,(280,300))
                screen.blit(text_about,(270,360))
                screen.blit(text_exit,(280,420))
                screen.blit(text_happy,(220,75))
                screen.blit(text_snake,(320,75))
                screen.blit(text_mail,(210,460))
                pygame.display.flip()
                scrn1=True
                scrn2=False
                scrn4=False
                    
