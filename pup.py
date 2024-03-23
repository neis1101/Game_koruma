import pygame as pg 


class Pup: 
    def __init__(self, screen ):
        self.screen = screen 
        self.x = 250
        self.y = 350
        self.x2 = 250
        self.y2 = 0
        self.x3 = 240
        self.y3 = 120
        self.x4 = 240
        self.y4 = 350

    def draw(self): 
        pg.draw.rect(self.screen, 'green', (self.x, self.y, 60, 150))
        pg.draw.rect(self.screen, 'green', (self.x2, self.y2, 60, 150))
        pg.draw.rect(self.screen, 'green', (self.x3, self.y3, 80, 30))
        pg.draw.rect(self.screen, 'green', (self.x4, self.y4, 80, 30))
        

    def move(self): 
        self.x -= 10
        if self.x < 0:
            self.x = 500
        
        self.x2 -= 10
        if self.x2 < 0:
            self.x2 = 500

        self.x3 -= 10
        if self.x3 < 0:
            self.x3 = 500

        self.x4 -= 10
        if self.x4 < 0:
            self.x4 = 500
            

    def update(self): 
      pass
        
