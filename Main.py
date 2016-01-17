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

while 1 == 1:
    screen.blit(background, (0, 0+buffer_height))
    screen.blit(bshot, (10,10 + buffer_height))
    screen.blit(rshot, (20,10 + buffer_height))
    screen.blit(yshot, (30,10 + buffer_height))
    
    all_players.draw(screen)
    
    key = pygame.key.get_pressed()
    player.update(key)
    
    
    
    
    pygame.display.update()
    pygame.event.pump()

