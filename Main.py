import pygame, sys, random, time, pygame.mixer, pygame.font
from pygame.locals import *
from pygame.font import *

from Projectile import *
from Player import *
from Enemy import *

'''
main.py
Creates the outermost frame for the world
'''



buffer_height = 50 #extra space for HP, currency, etc

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600 + buffer_height #this number refers to the dimensions of the game field

pygame.font.init()
myFont = pygame.font.SysFont("Comic Sans", 18)

scoreFont = pygame.font.SysFont("Helvetica", 40)

size = SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode(size)

print "Loading Images..."
background = pygame.image.load('Images/Background.png')
header = pygame.image.load('Images/Header.png')

bshot = pygame.image.load('Images/blue_shot.png')
rshot = pygame.image.load('Images/red_shot.png')
yshot = pygame.image.load('Images/yellow_shot.png')

bplayer = pygame.image.load('Images/blue_player.png')
rplayer = pygame.image.load('Images/red_player.png')
yplayer = pygame.image.load('Images/yellow_player.png')

bspid = pygame.image.load('Images/blue_spider.png')
rspid = pygame.image.load('Images/red_spider.png')
yspid = pygame.image.load('Images/yellow_spider.png')

bshift = pygame.image.load('Images/blue_shift.png')
rshift = pygame.image.load('Images/red_shift.png')
yshift = pygame.image.load('Images/yellow_shift.png')

def fallerWave(x_pos):
    if x_pos == 'R':
        x_pos = SCREEN_WIDTH - 72
    elif x_pos == 'L':
        x_pos = 30
    
    order = [0, 30, 60]
    
    types = [[rspid, 'red'],[yspid, 'yellow'],[bspid, 'blue']]
    
    random.shuffle(types)
    
    a = Faller(types[0][0], x_pos, 0 + buffer_height, 10, types[0][1])
    
    '''
    a = Faller(rspid, x_pos, order[0] + buffer_height, 10, 'red')
    b = Faller(yspid, x_pos, order[1] + buffer_height, 10, 'yellow')
    c = Faller(bspid, x_pos, order[2] + buffer_height, 10, 'blue')
    '''
player = Player([rplayer, yplayer, bplayer], 180, 450 + buffer_height, 1)
en1 = Enemy(bspid, 50, 200 + buffer_height, 10, 'blue', 5)
en2 = Enemy(rspid, 150, 250 + buffer_height, 10, 'red', 5)
en3 = Enemy(yspid, 250, 300 + buffer_height, 10, 'yellow', 5)

en4 = Shifter([rshift,yshift,bshift], 100, 100 + buffer_height, 10, 3)

counter = 0

enemies_alive = True

while player.alive and enemies_alive:
    counter = counter + 1
    
    
    screen.blit(background, (0, 0+buffer_height))

    if(counter % 10 == 0):
        if player.color == 'red':
            p = Projectile(rshot, player.rect.centerx - 2, player.rect.top - 20, 5, 'red', 9)
        if player.color == 'yellow':
            p = Projectile(yshot, player.rect.centerx - 2, player.rect.top - 20, 5, 'yellow', 9)
        if player.color == 'blue':
            p = Projectile(bshot, player.rect.centerx - 2, player.rect.top - 20, 5, 'blue', 9)
    
    if(counter % 50 == 0):
        fallerWave(random.randint(30,SCREEN_WIDTH - 72))
    
    key = pygame.key.get_pressed()
    
    if key[K_ESCAPE]:
        sys.exit()
    
    player.update(key)
    
    for p in all_projs:
        p.updateLocation()
        for e in all_enemies:
            p.contactEnemy(e)
        p.contactPlayer(player)
    
    enemies_alive = False
    for e in all_enemies:
        e.updateLocation()
        if e.alive:
            enemies_alive = True
        #pygame.sprite.spritecollide(e, all_projs, True)
    
    all_players.draw(screen)
    all_projs.draw(screen)
    all_enemies.draw(screen)
    
    screen.blit(header, (0,0))
    
    htext = myFont.render("Ship Damage: " + str((100*(player.maxHP - player.HP))/(player.maxHP)) + "%", 1, (0,0,0))
    screen.blit(htext, (250, 10))
    stext = scoreFont.render(str(Player.score),1, (0,0,0))
    screen.blit(stext, (130, 3))
    
    
    pygame.display.update()
    pygame.event.pump()
    
if enemies_alive:
    print("YOU STINK, LOSER")

elif player.alive:
    print("You play almost as well as my grandma")
    


