import pygame as pg
from random import randint
TS = 64
MAP_HEIGHT= 29000
def make_land():
    bg = pg.Surface((1100, MAP_HEIGHT),pg.SRCALPHA)

    #load filep
    sand_fp = pg.image.load(r'kenney_pirate-pack/PNG/Default size/Tiles/tile_69.png')
    sand_shorel= pg.image.load(r'kenney_pirate-pack/PNG/Default size/Tiles/tile_19.png')
    sand_shorer= pg.image.load(r'kenney_pirate-pack/PNG/Default size/Tiles/tile_17.png')
    sand_shoreb= pg.image.load(r'kenney_pirate-pack/PNG/Default size/Tiles/tile_34.png')

    # put sand on our background
    for x in range(0,1000,TS):
        for y in range(0,50,TS):
            bg.blit(sand_shoreb,(x,y))
    for x in range(0,100,TS):
        for y in range(0,MAP_HEIGHT,TS):
            bg.blit(sand_fp,(x, y))
    for x in range(1000,1100, TS):
        for y in range(0,MAP_HEIGHT, TS):
            bg.blit(sand_fp,(x,y))
    for x in range(100,164,TS):
        for y in range(0,MAP_HEIGHT,TS):
            bg.blit(sand_shorel,(x,y))
    for x in range(936,1000,TS):
        for y in range(0,MAP_HEIGHT,TS):
            bg.blit(sand_shorer,(x,y))
    
    return bg
    
            

            
