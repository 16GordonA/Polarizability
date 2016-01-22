import pygame, sys
from pygame.locals import *

all_players = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    
    buffer_height = 50
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 600 + buffer_height
    score = 0
    
    def __init__(self, images, startX, startY, lives):
        pygame.sprite.Sprite.__init__(self, all_players)
        self.images = [i.convert_alpha() for i in images] #transparent images in RYB order
        self.image = images[0].convert_alpha()
        self.rect = self.image.get_rect().move(startX, startY)  # rect is for blitting
        self.color= "red"
        self.speedX = 0
        self.speedY = 0
        self.direction = 'U'
        self.alive = True
        self.lives = lives
        self.alive = True
        self.armor = 0
        self.maxHP = 15
        self.HP = self.maxHP
    
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
        
        if Player.score >= (self.maxHP - 10)/5 * 100:
            self.maxHP += 5
            self.HP = self.maxHP
            self.armor += 1
    
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
                
        if self.speedX > 0 and self.rect.right >= Player.SCREEN_WIDTH:
            self.speedX = -2
        elif self.speedX < 0 and self.rect.left <= 0:
            self.speedX = 2
        
        if self.speedY < 0 and self.rect.top <= Player.buffer_height:
            self.speedY = 2
        elif self.speedY > 0 and self.rect.bottom >= Player.SCREEN_HEIGHT:
            self.speedY = - 2
    
    def setHP(self, newHP):
        self.HP = newHP
        if newHP <= 0:
            self.alive = False
            all_players.remove(self)