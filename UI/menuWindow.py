from tkinter import *
from pathlib import Path
from grid import Grid
from window import Window
from PIL import ImageTk, Image



def MenuWindow():
    master = Tk()



    bg_image = PhotoImage(file ='..//Image//background.gif')
    bg_label = Label (image = bg_image)
    bg_label.place(x = 0, y = 0, relwidth=1, relheight=1)
   
    master.minsize(450,320)
    master.geometry("320x100")

    def mode1():
        print ("click!")


    def mode2():
        print("mode22")
    buttonMode1_image = PhotoImage(file = '..//Image//mode1.gif')
    buttonMode1 = Button(master, image = buttonMode1_image, text="        AI Mode   ", height = 50, width = 150, bg='white', compound=LEFT, command=mode1)
    buttonMode1.place(x=300, y =10)

    buttonMode2_image = PhotoImage(file = '..//Image//mode2.gif')
    buttonMode2 = Button(master, image = buttonMode2_image, text="  Human Mode", height = 50, width = 150, bg='white', compound=LEFT, command=mode2)
    buttonMode2.place(x=300, y =80)

    mainloop()

MenuWindow()




