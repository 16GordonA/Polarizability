import pygame, sys, random, math
from pygame.locals import *

all_enemies = pygame.sprite.Group()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, startX, startY, damage, color, speed):
        pygame.sprite.Sprite.__init__(self, all_enemies)
        self.image = image.convert_alpha()  # transparent image
        self.rect = self.image.get_rect().move(startX, startY)  # rect is for blitting
        self.startX = startX
        self.startY = startY
        self.dmg = damage
        self.HP = 5
        self.color = color
        if(speed > 0):
            self.dir = 'R'  # direction (U, D), more added later?
        else:
            self.dir = 'L'
        self.speed = abs(speed)
    
    def updateLocation(self):
        if self.dir == 'R':
            self.rect = self.rect.move(self.speed, 0)
        elif self.dir == 'L':
            self.rect = self.rect.move(-self.speed, 0)
        
        if self.rect.right >= 400:
            self.dir = 'L'
        elif self.rect.left <= 0:
            self.dir = 'R'
        if self.rect.bottom < -100 or self.rect.top > 800:
            all_enemies.remove(self)
    
    def setHP(self, newHP):
        self.HP = newHP
        if newHP <= 0:
            all_enemies.remove(self)