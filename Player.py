import pygame, sys
from pygame.locals import *

all_players = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self, images, startX, startY, lives):
        pygame.sprite.Sprite.__init__(self, all_players)
        self.images = [i.convert_alpha() for i in images] #transparent images in RYB order
        self.image = images[0]
        self.rect = self.image.get_rect().move(startX, startY)  # rect is for blitting
        self.color= "red"
        self.speedX = 0
        self.speedY = 0
        self.direction = 'U'
        self.alive = True
        self.lives = lives
        self.HP = 100
    
    def update(self, keyPressed):
        if(self.speedX > 0):
            self.speedX = self.speedX - 1
        elif(self.speedX < 0):
            self.speedX = self.speedX + 1
        
        if(self.speedY > 0):
            self.speedY = self.speedY - 1
        elif(self.speedY < 0):
            self.speedY = self.speedY + 1
        
        if(keyPressed[K_w]):
            self.color = "red"
            self.image = self.images[0]
        elif(keyPressed[K_e]):
            self.color = "yellow"
            self.image = self.images[1]
        elif(keyPressed[K_r]):
            self.color = "blue"
            self.image = self.images[2]
        else:
            self.updateSpeed(keyPressed)
            
        self.rect = self.rect.move(self.speedX, self.speedY)
    
    def updateSpeed(self, keyPressed):
        speed = 3
        max = 8
        if keyPressed[K_RIGHT]:  # Movement Tests
            self.speedX += speed
            if self.speedX > max:
                self.speedX = max
        elif keyPressed[K_LEFT]:
            self.speedX -= speed
            if self.speedX < -max:
                self.speedX = -max
        if keyPressed[K_UP]:
            self.speedY -= speed
            if self.speedY < -max:
                self.speedY = -max
        if keyPressed[K_DOWN]:
            self.speedY += speed
            if self.speedY > max:
                self.speedY = max
        