import pygame as pg

class HealthBar():
    def __init__(self):
        self.width = 200
        self.height = 20
        self.image = pg.Surface((self.width,self.height))
        #make red
        self.red = (255,50,50)
        self.green = (50,255,50)
        self.image.fill(self.red)
        self.rect = self.image.get_rect()
        self.health = 100
        #basically just called the function we did below to set the health
        self.set_health(self.health)
        #this draws the bar to the side of the screen
        self.rect.bottomright = (1050, 650)
        
    def decrement(self,amount):
        #decrease health
        if self.health - amount <= 0:
            self.health = 0
        else:
            self.health -= amount
        self.set_health(self.health) # redraws the remaining health after
        
    def set_health(self,health):
        self.health = health
        #draw the red below the green so it appears
        self.image.fill(self.red)
        #set the green amount on my health bar
        green_w = int((self.health/100) * self.width)
        green_h = self.height
        green_image = pg.Surface((green_w,green_h))
        green_image.fill(self.green)
        self.image.blit(green_image,(0,0))
    
        
    def draw(self, screen):
        #blit
        screen.blit(self.image, self.rect)
   
        