import pygame as pg
import numpy as np
import random
import time
from UI.grid import Grid, Node
from time import sleep, time

class Apple:

    position = (0,0)
    apple_node = None

    def __init__(self,grid: Grid):
        self.grid = grid
        self.newApple()
        

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
    tail = None
    length = 0 
    direction = 1
    
    def __init__(self,grid : Grid):
        self.grid =grid
        grid.change_field(int(self.grid.rows/2),int(self.grid.cols/2),2)
        self.length =1
        self.head = grid.return_node(int(self.grid.rows/2),int(self.grid.cols/2))
        self.body_list.append(self.head)

    def update(self,apple: Apple):

        def changeHead(self, move: (int,int)):
            position = (0,0)
            remove_node = None
            position = ( self.head.position[0]+move[0],self.head.position[1] + move[1])

            if(hitMap(self, (position[0], position[1])) == True):
                self.grid._isRunning =False
                print("Game Over  Score:", len(self.body_list))

            elif(eatApple(self, (position[0],position[1])) == True):
                self.head = self.grid.return_node(position[0],position[1])
                self.grid.change_field(position[0],position[1],2)
                for n in self.body_list:
                    n.change_field_type(3)
                self.body_list.append(self.head)
                apple.newApple()
                print("Score: ", len(self.body_list))

            elif(hitBody(self, (position[0],position[1])) == True):
                self.grid._isRunning = False
                print("Game Over  Score:", len(self.body_list))

            else:
                self.head = self.grid.return_node(position[0],position[1])
                self.grid.change_field(position[0],position[1],2)
                remove_node = self.body_list.pop(0)
                self.tail = remove_node
                self.grid.change_field(remove_node.row,remove_node.col, 0)
                for n in self.body_list:
                    n.change_field_type(3)
                self.body_list.append(self.head)
               
        def hitBody(self,position: (int,int)):

            next_node = self.grid.return_node(position[0],position[1])

            if(next_node.field_type == 3):
                return True
            else:
                return False
            
        def eatApple(self,position: (int,int)):

            next_node = self.grid.return_node(position[0],position[1])

            if(next_node.field_type == 1):
                return True
            else:
                return False
        def hitMap(self,position: (int,int)):

            if(position[0] > (self.grid.rows-1) or position[1] > (self.grid.cols-1) or position[0] < 0 or position[1] < 0):
                return True
            else:
                return False

        if(self.direction ==0):
            changeHead(self, (0, -1))
        if(self.direction ==1):
            changeHead(self, (-1, 0))
        if(self.direction ==2):
            changeHead(self, (0, 1))
        if(self.direction ==3):
            changeHead(self, (1, 0))

    

   



    def moveLeft(self):
        if(self.direction != 2):
            self.direction = 0
    def moveRight(self):
        if(self.direction !=0):
            self.direction =2
    def moveUp(self):
        if(self.direction != 3):
            self.direction =1
    def moveDown(self):
        if(self.direction != 1):
            self.direction =3

    def drawSnake(self,screen):
        for x in self.body_list:
            x.draw(screen)
        self.tail.draw(screen)
    
     


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

        self.screen = pg.display.set_mode((screen_width, screen_height),pg.HWSURFACE) # pylint: disable=no-member
        self.clock = pg.time.Clock()
        self.grid.draw_map(self.screen)

        self.snake = Snake(grid)
        self.apple = Apple(grid)


    def updateOnLoop(self):
        self.snake.update(self.apple)
        self.quit()

    def updateMapOnLoop(self):
        self.snake.drawSnake(self.screen)
        self.apple.drawApple(self.screen)

    def quit(self):
        if(self.grid._isRunning == False):
            pg.quit() # pylint: disable=no-member


    def start(self):
        last_time = time()
        while(self.grid._isRunning == True):
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
                self.grid._isRunning = False
               



            #no delay on keys           
            if(time()-last_time >0.2):
                last_time = time()
                self.updateOnLoop()
                self.updateMapOnLoop()
            else:
                sleep(0.001)         

 
               # pylint: disable=no-member
