import pygame as pg
import numpy as np






class Grid:
    _isRunning = True

    def __init__(self, cols: int, rows: int):
        self.table = [[Node(row, col)
                       for col in range(cols)]
                      for row in range(rows)]
        self.cols = cols
        self.rows = rows
        self._isRunning = True

    def draw_map(self, screen: "PyGame screen"):
        """Draws whole map"""
        screen.fill(Node.BLACK)
        for row in self.table:
            for node in row:
                node.draw(screen)

    def change_field(self, row: int, col: int, f_type: int):
        self.table[row][col].change_field_type(f_type)

    def draw_node(self, screen, row: int, col: int):
        self.table[row][col].draw(screen)

    def return_node(self, row: int, col: int):
        return self.table[row][col]



class Node:
    # define rectangles dimensions
    r_width = 20
    r_height = 20
    r_margin = 5

    # define some basic colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    ORANGE = (255, 165, 0)
    PINK = (199,21,133)

    def __init__(self, row: int, col: int,
                 field_type: int = 0):
        self.row = row
        self.col = col
        self.field_type = field_type
        self.position = (row,col) 



    def draw(self, screen):
        color = self.get_field_color()
        col = self.col
        row = self.row
        width = self.r_width
        height = self.r_height
        margin = self.r_margin
        # rect -> (left, top, width, height)
        # draw.rect(surface, color, rect, margin)
        pg.draw.rect(screen, color,
                     ((col * (width + margin)) + margin,
                      (row * (height + margin)) + margin,
                      width, height))
        pg.display.flip()  # refresh screen

    def change_field_type(self, field_type: int):
        self.field_type = field_type

    def get_field_color(self) -> tuple:
        """Gets the color tuple of field"""
        if self.field_type == 0:    #field
            return self.GREEN
        elif self.field_type == 1:  #apple
            return self.RED
        elif self.field_type == 2:  #head
            return self.BLUE
        elif self.field_type ==3:   #body
            return self.PINK

