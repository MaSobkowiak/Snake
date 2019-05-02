import pygame as pg
import numpy as np
import random
from UI.grid import Grid, Node


class Window():
    def __init__(self, grid: Grid):
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

        self.screen = pg.display.set_mode([screen_width, screen_height])


        self.clock = pg.time.Clock()
        self.grid.draw_map(self.screen)
        

 
        pg.time.delay(5000)
        pg.quit()   # pylint: disable=no-member
