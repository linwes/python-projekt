from tkinter import *
from tkinter.colorchooser import askcolor
import json
import requests
import ord
from PIL import ImageTk, Image, ImageDraw
import PIL

class Paint(object):

    storlek = 5.0
    color = 'black'

    
    def __init__(self):
        self.root = Tk()

        self.vall_color = Button(self.root, text='color', command=self.choose_color)
        self.vall_color.grid(row=0, column=1)

        self.val_sudd = Button(self.root, text='eraser', command=self.use_eraser)
        self.val_sudd.grid(row=0, column=2)

        self.val_storlek = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.val_storlek.grid(row=0, column=3)

        self.c = Canvas(self.root, bg='white', width=600, height=400)
        self.c.grid(row=1, columnspan=5)

        with open('Ritat_ord.json', 'r', encoding='utf8') as ord_file:
            jord = json.load(ord_file)
        self.test = str(jord)

        self.message = Button(self.root, text='klicka för ord:', command=self.open)
        self.message.grid(row=2, columnspan=1)
        
        self.save = Button(self.root, text='spara', command=self.save)
        self.save.grid(row=0, columnspan=4)         
        self.setup()
        self.root.mainloop()
    def open(self):
        ord.SkapaOrd()
       
        with open('Ritat_ord.json', 'r', encoding='utf8') as ord_file:
            jord = json.load(ord_file)
        self.test = str(jord)
        self.message = Label(self.root, text=f'rita följande ord: {self.test}')
        self.message.grid(row=2, columnspan=7)
        
    def save(self):
        self.filename = "static/bild.png"
        self.image1.save(filename)
        image1 = PIL.Image.new("RGB", self.white)
        draw = ImageDraw.Draw(image1)

    def setup(self):
        self.x_pos = None
        self.y_pos = None
        self.line_width = self.val_storlek.get()
        self.color = self.color
        self.eraser_on = False
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.val_sudd, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.val_storlek.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.x_pos and self.y_pos:
            self.c.create_line(self.x_pos, self.y_pos, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.x_pos = event.x
        self.y_pos = event.y

    def reset(self, event):
        self.x_pos, self.y_pos = None, None

if __name__ == '__main__':
    Paint()