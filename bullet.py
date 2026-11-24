import pygame as pg
from pygame.sprite import Sprite
from math import sin, cos, pi

class Bullet(Sprite):
    #loading the image
    og_image = pg.image.load(r'kenney_space-shooter-extension/PNG/Sprites/Missiles/spaceMissiles_040.png')
    b_image = pg.transform.rotozoom(og_image,0,.5)
    #manages the bullets
    # load in the bullets x, y, theta of the ship, hard code speed
    def __init__(self, destroyer, theta, speed=10):
        #super init the sprite inheritence
        super().__init__()
        
        self.x = destroyer.rect.x +10
        self.y = destroyer.rect.y +8
        self.theta = theta
        #this rotates the image with respect to the ship and established self.image from my loaded stuff
        self.image = pg.transform.rotozoom(self.b_image, self.theta, 1)
        #get my rectangle
        self.rect = self.image.get_rect(center=(self.x,self.y))
        #now i need to calculate the vectors (this was a pain)
        rad = self.theta * (pi/180)
        self.dx = speed * sin(rad)
        self.dy = speed * cos(rad)
        
        
    def update(self):
        
        self.x -= self.dx
        self.y -= self.dy
        #finding the center
        self.rect.center = (self.x,self.y)
        #using the cetner in order to be able to kill the bullets 
        if self.x < 0 or self.x > 1200 or self.y < 0 or self.y > 700:
            self.kill()
            
    
        