import pygame as pg
from random import randint
from math import sin, cos, atan2, pi
class Shaheb(pg.sprite.Sprite):
    #represents the drone
    def __init__(self, ts_game):
        super().__init__()
        #asign the main game screen to a variable
        self.screen = ts_game.screen
        #assign the destroyer to a variable in this class
        self.destroyer = ts_game.destroyer
        #my image
        self.og_image = pg.image.load(r'shahed_PNG4.png')
        self.image = self.og_image
        #get my rect for the background and the image
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.offset_x = randint(-50,50)
        self.offset_y = randint(-50,50)
        #spawning code
        self.x = float(randint(0,900))
        self.y = -50
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.speed = 10
        #calc direction to the destroyer only once so it keeps flying by 
        self.d_x = self.destroyer.rect.centerx - self.x + self.offset_x
        self.d_y = self.destroyer.rect.centery - self.y +self.offset_y
        self.theta = atan2(self.d_y,self.d_x)
        
        #the updating attribute
    def update(self):
    
        #change the direction of the drone towards the destroyer
        #x vector
        self.x += cos(self.theta)*self.speed
        #y vector
        self.y += sin(self.theta)*self.speed
        #get the center of the rect
        self.rect.center = (int(self.x),int(self.y))
        #calc the theta for the image
        self.img_theta = atan2(-self.d_y, self.d_x) * (180/pi) 
        #use the theta in rotozoom
        self.image = pg.transform.rotozoom(self.og_image,self.img_theta,.04)
        #change the rectangle w the theta
        self.rect = self.image.get_rect(center= self.rect.center)
        
        if self.rect.top > self.screen_rect.bottom:
            self.kill()
        