import pygame as pg
from math import atan2, pi
#from health_Bar import HealthBar
#from random import uniform
#this class will manage my ship
class Destroyer(pg.sprite.Sprite):
    def __init__(self, ts_game, x, y, theta):
        pg.sprite.Sprite.__init__(self)
        # so this class will take the current instance of the The Strait class, so it can have access to all the gmae resources i defined earlier
        self.screen = ts_game.screen
        #assign a value to the game screen
        self.screen_rect = ts_game.screen.get_rect()
        self.theta = theta
        # this lets me place my ship in the correct location by getting the rectangle
        self.x = x
        self.y = y
        #load the ship image, returns a surface representing the ship
        self.og_image = pg.image.load(r'Sea Warfare Set/Destroyer/ShipDestroyerHull.png')
        self.image = self.og_image
        # get the rectangle of the ship
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.go_right = 0
        self.go_left = 0
        #self.hb = HealthBar()
        #self.compass = pg.image.load('
    
    def update(self):
        if self.go_right and self.rect.right < 950:
            self.rect.x += 5
        if self.go_left and self.rect.left > 150:
            self.rect.x -= 5
        #have to find out my mouses position, it returns as a tuple, separate them as x and y
        mouse_x, mouse_y = pg.mouse.get_pos()
        #find the distance between the mouse and the ship postiion
        d_x = mouse_x - self.x
        d_y = mouse_y - self.y
        #finding the angle in radians + converting to degrees
        self.theta = (atan2(-d_y, d_x)) * (180/pi) - 90
        
        #health bar update
        #if uniform(0,1000)<3:
            
            #self.hb.set_health()
            
        
        
            
    def draw_ship(self):
        
        self.screen.blit(self.image, self.rect)
        
        #blit the health bar
        #self.hb.rect.midtop = self.rect.midbottom
        #self.screen.blit(self.hb.image, self.hb.rect)
    
        
        
    