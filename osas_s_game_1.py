import pygame as pg
from pygame.math import Vector2
import random as rnd

from pygame.sprite import collide_rect

pg.init()
pg.font.init()
## sets the default screen size
s_size = (500,500) 
screen = pg.display.set_mode(s_size)

pg.display.set_caption('game :)')


class Player():
    def __init__(self):
        self.pos = Vector2(100,210)
        self.w = 40
        self.h = 60
        self.vel = 5
        self.rect = pg.rect.Rect(self.pos.x,self.pos.y,self.w,self.h)


    def move(self): ## movement code stops at edge of screen
        keys = pg.key.get_pressed()
        
        if keys[pg.K_DOWN] and self.pos.y <= 440: 
            self.pos.y += self.vel
        elif keys[pg.K_UP] and self.pos.y >= 0:
            self.pos.y -= self.vel
        elif keys[pg.K_LEFT] and self.pos.x >= 0:
            self.pos.x -= self.vel
        elif keys[pg.K_RIGHT] and self.pos.x <= 460:
            self.pos.x += self.vel



    def drawRect(self):## draw the rectangle with new position
        self.rect = pg.rect.Rect(self.pos.x,self.pos.y,self.w,self.h)
        pg.draw.rect(screen,'blue',self.rect)

class Apple():
    def __init__(self):
        self.pos = Vector2(350,210) 
        self.w = 20
        self.h = 20
        self.score = 10
        self.rect = pg.rect.Rect(self.pos.x,self.pos.y,self.w,self.h)

    def newPos(self):#randomly generate a new position in the screen
        self.pos = Vector2(rnd.randint(0,500),rnd.randint(0,500))
        
    def drawRect(self):
        self.rect   = pg.rect.Rect(self.pos.x,self.pos.y,self.w,self.h)
        pg.draw.rect(screen,'green',self.rect)

score = 0 
font = pg.font.Font(None, 36)



#player behaviour
p1 = Player()
apple = Apple()



#main game loop
running = True
while running:
    pg.time.delay(15)    
    
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    p1.move()
    
    screen.fill((0,0,0))
    p1.drawRect()
    apple.drawRect()
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    if p1.rect.colliderect(apple.rect) == True:
        apple.newPos()
        score += apple.score
       
    pg.display.update()



