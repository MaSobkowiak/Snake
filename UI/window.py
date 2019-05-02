import pygame as pg
import numpy as np
import random
import time
from UI.grid import Grid, Node
from pygame.locals import *
from time import sleep, time

class Apple:

    position = (0,0)
    apple_node = None

    def __init__(self,grid: Grid):
        self.grid = grid
        

    def newApple(self):
        while(1):
            self.position = (random.randint(0,len(self.grid.table)-1),random.randint(0,(len(self.grid.table[len(self.grid.table)-1]) -1)))
            node = self.grid.return_node(self.position[0],self.position[1])
            if(node.field_type == 0):
                self.grid.change_field(self.position[0],self.position[1],1)
                self.apple_node = self.grid.return_node(self.position[0],self.position[1])
                break

    def drawApple(self,screen):
        self.apple_node.draw(screen)

        





class Snake:
    body_list = []
    head = None
    length = 0 
    direction = 1
    
    def __init__(self,start: (int,int),grid : Grid):
        self.grid =grid
        grid.change_field(start[0],start[1],2)
        self.length =1
        self.head = grid.return_node(start[0],start[1])
        self.body_list.append(self.head)

    def update(self):

        def changeHead(self, move: (int,int)):
            position = (0,0)
            self.grid.change_field(self.head.row,self.head.col, 0)
            position = ( self.head.position[0]+move[0],self.head.position[1] + move[1])
            print(position)
            self.head = self.grid.return_node(position[0],position[1])
            self.grid.change_field(position[0],position[1],2)
            self.body_list.pop
            self.body_list.append(self.head)

        if(self.direction ==0):
            changeHead(self, (0, -1))
        if(self.direction ==1):
            changeHead(self, (-1, 0))
        if(self.direction ==2):
            changeHead(self, (0, 1))
        if(self.direction ==3):
            changeHead(self, (1, 0))

   


    def moveLeft(self):
        self.direction = 0
    def moveRight(self):
        self.direction =2
    def moveUp(self):
        self.direction =1
    def moveDown(self):
        self.direction =3

    def drawSnake(self,screen):
        for x in self.body_list:
            x.draw(screen)
            #pg.time.delay(500)
    
     


class Window():

    
    def __init__(self, grid: Grid, start: (int,int)):
        pg.init()   # pylint: disable=no-member
        # setup window
        pg.display.set_caption('Snake')
        
        self.grid = grid

        # assign to variables for brevity
        cols = self.grid.cols
        rows = self.grid.rows
        width = Node.r_width
        height = Node.r_height
        margin = Node.r_margin
        

        screen_width = cols * (width + margin) + 2 * margin
        screen_height = rows * (height + margin) + 2 * margin

        self.screen = pg.display.set_mode((screen_width, screen_height),pg.HWSURFACE)
        self.clock = pg.time.Clock()
        self.grid.draw_map(self.screen)

        self.snake = Snake((0,0),grid)
        self.apple = Apple(grid)


    def UpdateOnLoop(self):
        self.snake.update()
        self.snake.drawSnake(self.screen)
        self.apple.newApple()
        self.apple.drawApple(self.screen)

    def Start(self):
        last_time = time()
        while(1):
            pg.event.pump()
            keys = pg.key.get_pressed() 
            
            if (keys[K_RIGHT]):
                self.snake.moveRight()                
            if (keys[K_LEFT]):
                self.snake.moveLeft() 
            if (keys[K_UP]):
                self.snake.moveUp()
            if (keys[K_DOWN]):
                self.snake.moveDown()
            if (keys[K_ESCAPE]):
                pg.quit() # pylint: disable=no-member



            #no delay on keys           
            if(time()-last_time >0.5):
                last_time = time()
                self.UpdateOnLoop()
            else:
                sleep(0.1)         

 
               # pylint: disable=no-member
