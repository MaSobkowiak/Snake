from tkinter import *
from pathlib import Path
from UI.grid import Grid
from UI.window import Window
from PIL import ImageTk, Image
import threading

class MenuWindow():
    score = 0

    def __init__(self):
        self.master = Tk()
        bg_image = PhotoImage(file ='Image//background.gif')
        bg_label = Label (image = bg_image)
        bg_label.place(x = 0, y = 0, relwidth=1, relheight=1)

        self.master.minsize(450,320)
        self.master.geometry("320x100")

        buttonMode1_image = PhotoImage(file = 'Image//mode1.gif')
        buttonMode1 = Button(self.master, image = buttonMode1_image, text="        AI Mode   ", height = 50, width = 150, bg = 'white', compound=LEFT, command=self.mode1)
        buttonMode1.place(x=300, y =10)

        buttonMode2_image = PhotoImage(file = 'Image//mode2.gif')
        buttonMode2 = Button(self.master, image = buttonMode2_image, text="  Human Mode", height = 50, width = 150, bg = 'white', compound=LEFT, command=self.mode2)
        buttonMode2.place(x=300, y =80)


        self.v = StringVar()
        scoreLabel = Label(self.master, textvariable = self.v, font=("Helvetica", 20), bg = 'white')
        scoreLabel.place(x=10,y=20)

        self.master.mainloop()





    def mode1(self):
        grid = None
        app = None
        grid = Grid(20, 10)
        app = Window(grid)
        self.score = app.start(2)
        self.v.set('Score: ' + str(self.score))
        


        
    def mode2(self):
        grid = None
        app = None
        grid = Grid(20, 10)
        app = Window(grid)
        self.score = app.start(1)
        self.v.set('Score: ' + str(self.score))

        



