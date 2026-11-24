import pygame as pg

class HealthBar():
    def __init__(self):
        self.width = 50
        self.height = 10
        self.image = pg.Surface((self.width,self.height))
        #make red
        self.red = (255,50,50)
        self.green = (50,255,50)
        self.image.fill(self.red)
        self.rect = self.image.get_rect()
        self.health = 100
        self.update()
    def decrement(self,amount):
        #decrease health
        if health - amount <= 0:
            self.health = 0
        else:
            self.health += -amount
        
    def set_health(self,health):
        self.health = health
        #set the green amount on my health bar
        green_w = self.health/100 * self.width
        green_h = self.height
        green_image = pg.Surface((green_w,green_h))
        green_image.fill(self.green)
        #blit
        self.image.blit(self.green_image,(0,0))
   
        