
from tkinter import *
import PIL
from PIL import Image, ImageDraw
import json
from tkinter.colorchooser import askcolor


class paint():
    standard_färg = 'black'
    root = Tk()
    cv = Canvas(root, width=640, height=480, bg='white')
    image = PIL.Image.new('RGB', (640, 480), 'white')
    draw = ImageDraw.Draw(image)
    
    # def save(self):
    #     filename = 'bild.png'
    #     image.save(filename)

    def choose_color(self):
        self.color = standard_färg
        self.color = askcolor(color=color)


        # färg = color

    def activate_paint(self,e):
        self.lastx, self.lasty
        self.cv.bind('<B1-Motion>', paint)
        self.lastx, lasty = self.e.x, self.e.y

    def paint(self,e):
        self.lastx, self.lasty
        self.x, y = e.x, e.y
        self.cv.create_line((lastx, lasty, x, y), width=1)
        self.draw.line((lastx, lasty, x, y), fill=colorchooser.color, width=1)
        self.lastx, lasty = x, y
        
    def __init__(self):

        with open('Ritat_ord.json', 'r', encoding='utf8') as ord_file:
            jord = json.load(ord_file)

        self.test = str(jord)

        self.message = Label(root, text=f'rita följande ord: {test}')
        self.message.pack(side=BOTTOM)

        self.lastx, lasty = None, None

        self.cv.bind('<1>', activate_paint)
        self.cv.pack(expand=YES, fill=BOTH)
        self.färg_knapp = Button(text = 'färg', command=choose_color)
        self.färg_knapp.pack(side=LEFT)

        self.btn_save = Button(text="save", command=save)
        self.btn_save.pack()
        self.färg_knapp.pack()

    root.mainloop()
paint()