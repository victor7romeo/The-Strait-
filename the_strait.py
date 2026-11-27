import sys
import pygame as pg
from pygame import sprite
from time import sleep
from settings import Settings
from destroyer import Destroyer
from land import make_land
from bullet import Bullet
from shaheb import Shaheb
from pt_boat import Pt_Boat
from missile import Missile
from health_Bar import HealthBar
#import some functionality stuff
#this class will make the settings that we need in order to make the game actually start running
class TheStrait:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.font.init()
        pg.mixer.music.load('Bg_music.mp3')
        self.cram = pg.mixer.Sound('U.S. Naval Academy.mp3')
        self.main_font = pg.font.Font(r'Courier_Prime/CourierPrime-Regular.ttf',size=50)
        self.sub_font = pg.font.Font(r'Courier_Prime/CourierPrime-Regular.ttf' , size = 20)
        self.clock = pg.time.Clock()
        self.settings = Settings()
        #making a surface , with dimensions
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption('The Strait')
        #adding my destroyer
        self.destroyer = Destroyer(self, 550, 500, 0)
        self.health_bar = HealthBar()
        #adding my bullets as a sprite group
        self.bullets = pg.sprite.Group()
        self.shaheb = pg.sprite.Group()
        self.pt_boat = pg.sprite.Group()
        self.missiles = pg.sprite.Group()
        
        self.bg_color = (self.settings.bg_color)
        self.font_color = (self.settings.font_color)
        self.start_bg = pg.image.load(r'background.jpg')
        self.lose_bg = pg.image.load(r'lose_bg.jpg')
        
        
        
        
    def start_screen(self):
        running = 1
        pg.mixer.music.play()
        main_surf = pg.font.Font.render(self.main_font,'The \n Strait',True, self.font_color)
        while running:
            for e in pg.event.get():
                if e.type == pg.KEYDOWN:
                    running = 0          
            self.screen.blit(self.start_bg,(-50,-200))
            self.screen.blit(main_surf, (100,200))
            
            pg.display.flip()
    def brief_screen(self):
        running = 1
        sub_surf = pg.font.Font.render(self.sub_font,'Mission Brief...\n you and your carrier strike group were on patrol\n in the Strait of Hormuz until you were ambushed\n by OPFOR all other ships were disabled or destroyed... \n except for yours.\n You are the last ship.\n \nPress space to engage...', True, self.font_color)
        while running:
            for e in pg.event.get():
                if e.type == pg.KEYDOWN:
                    if e.key == pg.K_SPACE:
                        running = 0
                        
            self.screen.blit(self.start_bg,(-50,-200))
            self.screen.blit(sub_surf, (100, 425))

            pg.display.flip()
    def run_game(self):
        #making the land
        running = 1
        strait = make_land()
        #ship speed
        fwd_spd = 4   
        bg_y = self.settings.screen_height - 29000
        #will go up after every frame and manages when my shahebs spawn
        spawn_timer = 0
        boat_spawn_timer = 0
        
        #starts the main loop of the game
        while running:
            ##look for new events##
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    sys.exit()
                elif e.type == pg.KEYDOWN:
                    if e.key == pg.K_d:
                        self.destroyer.go_right = 1
                    if e.key == pg.K_a:
                        self.destroyer.go_left = 1
                    if e.key == pg.K_q:
                        sys.exit()
                    if e.key == pg.K_p:
                        running = 0
            # using the space bar i can use the sprite group .add attribute and add the bullet to the destroyers position and its theta
                    if e.key == pg.K_SPACE:
                        self.bullets.add(Bullet(self.destroyer, self.destroyer.theta))
                        pg.mixer.Sound.play(self.cram)
                         
                        
                        
                elif e.type == pg.KEYUP:
                    if e.key == pg.K_d:
                        self.destroyer.go_right = 0
                    if e.key == pg.K_a:
                        self.destroyer.go_left = 0
                    if e.key == pg.K_SPACE:
                        self.bullets.add(Bullet(self.destroyer, self.destroyer.theta))
                    if e.key == pg.K_e:
                        self.missiles.add(Missile(self.destroyer, self.destroyer.theta))
                        
                        
            if bg_y < 0:
                bg_y += fwd_spd
                    
            else:
                bg_y = 300
                sleep(5)
                running =0
                    
            #my spawn timer
            spawn_timer += 1
            if spawn_timer >=200:
                #im just going to pass in self to the shaheb class call so it automatically grabs all the values that it needs
                self.shaheb.add(Shaheb(self))
                spawn_timer = 0
                
            boat_spawn_timer += 1
            if boat_spawn_timer >=300:
                self.pt_boat.add(Pt_Boat(self))
                boat_spawn_timer = 0
                      
            ##_________________##
            
            
                ### Updating Section # drawing things and flipping the screen ###
            self.destroyer.update()
            self.bullets.update()
            self.missiles.update()
            self.shaheb.update()
            self.pt_boat.update()
            # my bullets collsions, call the groupcollide then the bullets + shaheb and then true, true so they both disappear
            pg.sprite.groupcollide(self.bullets, self.shaheb, True, True)
            pg.sprite.groupcollide(self.missiles, self.pt_boat, True, True)
            # my dron/boat collsions on the boat, use sprite collide bc the destroyer is not a group
            if pg.sprite.spritecollide(self.destroyer, self.shaheb, True):
                self.health_bar.decrement(15)
            if pg.sprite.spritecollide(self.destroyer, self.pt_boat, True):
                self.health_bar.decrement(30)
            
            if self.health_bar.health <= 0:
                sleep(1)
                running = 0 
            self.screen.fill(self.bg_color)
            self.screen.blit(strait,(0,bg_y))
            # draw the bullets
            self.bullets.draw(self.screen)
            self.missiles.draw(self.screen)
            #draw the drones
            self.shaheb.draw(self.screen)
            #draw the boats
            self.pt_boat.draw(self.screen)
                # draw the ship
            self.destroyer.draw_ship()
            #draw the health bar
            self.health_bar.draw(self.screen)
            pg.display.flip()
                #frames
            self.clock.tick(60)
    def losing_screen(self):
        main_surf = pg.font.Font.render(self.main_font,'YOU LOST\n MISSION FAILED',True, self.font_color)
        while 1:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    sys.exit()
            self.screen.blit(self.lose_bg,(-50, -300))
            self.screen.blit(main_surf, (200,300))
            pg.display.flip()
            
if __name__ == '__main__':
    # this makes the game instance and runs it
    ts = TheStrait()
    ts.start_screen()
    ts.brief_screen()
    ts.run_game()
    ts.losing_screen()