
import pygame as pg
import random as rnd

pg.init()
## sets the default screen size
s_size = (500,500) 
screen = pg.display.set_mode(s_size)

pg.display.set_caption('game :)')




class Player():
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.w = 40
        self.h = 60
        self.vel = 5

    def move(self): ## movement code stops at edge of screen
        keys = pg.key.get_pressed()
        
        if keys[pg.K_DOWN] and self.posy <= 440: 
            self.posy += self.vel
        elif keys[pg.K_UP] and self.posy >= 0:
            self.posy -= self.vel
        elif keys[pg.K_LEFT] and self.posx >= 0:
            self.posx -= self.vel
        elif keys[pg.K_RIGHT] and self.posx <= 460:
            self.posx += self.vel

    def drawRect(self):
        obj = pg.rect.Rect(self.posx,self.posy,self.w,self.h)
        pg.draw.rect(screen,'blue',obj)

class Apple():
    def __init__(self):
        self.posx = rnd.randint(0,500)
        self.posy = rnd.randint(0,500)

        self.w = 20
        self.h = 20
        self.score = 1

    def newPos(self):
        self.posx = rnd.randint(0,500)
        self.posy = rnd.randint(0,500)
        self.drawRect()
        

    def drawRect(self):
        obj = pg.rect.Rect(self.posx,self.posy,self.w,self.h)
        pg.draw.rect(screen,'green',obj)

        
#player behaviour
p1 = Player()
apple = Apple()



#main game loop
running = True
while running:
    pg.clock.tick(60)
    
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    p1.move()
    screen.fill((0,0,0))
    p1.drawRect()
    apple.newPos()
    pg.display.update()
    
    
 

 