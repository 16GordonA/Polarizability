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

size = SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode(size)

print "Loading Images..."
background = pygame.image.load('Images/Background.png')

bshot = pygame.image.load('Images/blue_shot.png')
rshot = pygame.image.load('Images/red_shot.png')
yshot = pygame.image.load('Images/yellow_shot.png')

bplayer = pygame.image.load('Images/blue_player.png')
rplayer = pygame.image.load('Images/red_player.png')
yplayer = pygame.image.load('Images/yellow_player.png')

player = Player([rplayer, yplayer, bplayer], 180, 450 + buffer_height, 1)

counter = 0

while 1 == 1:
    counter = counter + 1
    
    screen.blit(background, (0, 0+buffer_height))
    screen.blit(bshot, (10,10 + buffer_height))
    screen.blit(rshot, (20,10 + buffer_height))
    screen.blit(yshot, (30,10 + buffer_height))
    
    for p in all_projs:
        p.updateLocation()
    
    all_players.draw(screen)
    all_projs.draw(screen)
    
    key = pygame.key.get_pressed()
    player.update(key)
    
    if(counter % 10 == 0):
        if player.color == 'red':
            p = Projectile(rshot, player.rect.centerx - 2, player.rect.top - 20, 5, 'red', 7)
        if player.color == 'yellow':
            p = Projectile(yshot, player.rect.centerx - 2, player.rect.top - 20, 5, 'yellow', 7)
        if player.color == 'blue':
            p = Projectile(bshot, player.rect.centerx - 2, player.rect.top - 20, 5, 'blue', 7)
    
    pygame.display.update()
    pygame.event.pump()

