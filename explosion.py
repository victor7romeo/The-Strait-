import pygame as pg
from pygame.time import get_ticks
class Explosion(pg.sprite.Sprite):
    def __init__(self,ts_game,x,y):
        super().__init__()
        self.screen = ts_game.screen
        self.image = pg.image.load(r'Ckenney_pirate-pack/PNG/Default size/Effects/explosion2.png')
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(self.x,self.y))
        