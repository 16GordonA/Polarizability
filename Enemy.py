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
        self.alive = True
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
            
class Shifter(Enemy):
    def __init__(self, images, startX, startY, damage, speed):
        pygame.sprite.Sprite.__init__(self, all_enemies)
        self.images = [i.convert_alpha() for i in images] #transparent images in RYB order
        self.image = images[0].convert_alpha()
        self.rect = self.image.get_rect().move(startX, startY)  # rect is for blitting
        self.startX = startX
        self.startY = startY
        self.dmg = damage
        self.HP = 30
        self.color = 'red'
        self.age = 0
        if(speed > 0):
            self.dir = 'R'  # direction (U, D), more added later?
        else:
            self.dir = 'L'
        self.speed = abs(speed)
        
    def updateLocation(self):
        Enemy.updateLocation(self)
        
        self.age += 1
        
        if self.age % 40 == 0:
            if self.color == 'red':
                self.image = self.images[1]
                self.color = 'yellow'
            elif self.color == 'yellow':
                self.image = self.images[2]
                self.color = 'blue'
            elif self.color == 'blue':
                self.image = self.images[0]
                self.color = 'red'
        