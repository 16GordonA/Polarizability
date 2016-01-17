import pygame, sys, random, math
from pygame.locals import *

all_projs = pygame.sprite.Group()

class Projectile(pygame.sprite.Sprite):
    def __init__(self, image, startX, startY, damage, color, speed):
        pygame.sprite.Sprite.__init__(self, all_projs)
        self.image = image.convert_alpha()  # transparent image
        self.rect = self.image.get_rect().move(startX, startY)  # rect is for blitting
        self.startX = startX
        self.startY = startY
        self.dmg = damage
        self.color = color
        if(speed > 0):
            self.dir = 'U'  # direction (U, D), more added later?
        else:
            self.dir = 'D'
        self.speed = abs(speed)
    
    def updateLocation(self):  # Only used when on screen
        if self.dir == 'U':
            self.rect = self.rect.move(0, -self.speed)
        elif self.dir == 'D':
            self.rect = self.rect.move(0, self.speed)
        
        if self.rect.left > 500 or self.rect.right < -100 or self.rect.bottom < -100 or self.rect.top > 800:
            all_projs.remove(self)
            
    def contactPlayer(self, target):
        if self.rect.bottom > target.rect.top and self.rect.top < target.rect.bottom and self.rect.right > target.rect.left and self.rect.left < target.rect.right:
            target.setHP(target.HP - self.dmg)
            self.rect = self.rect.move(999, 999)
            all_projs.remove(self)