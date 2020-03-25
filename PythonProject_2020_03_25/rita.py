from tkinter import *
from tkinter import ttk, colorchooser, filedialog
import PIL, json, requests
from PIL import ImageGrab
import ord


class main:
    def __init__(self,master):
        self.master = master
        self.pen_color = 'black'
        self.c_color = 'white'
        self.old_x = None
        self.old_y = None
        self.pen = 5
        self.drawWidgets()
        self.c.bind('<B1-Motion>',self.paint)
        self.c.bind('<ButtonRelease-1>',self.reset)


    def paint(self,pos):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x,self.old_y,pos.x,pos.y,width=self.pen,fill=self.pen_color,capstyle=ROUND,smooth=True)

        self.old_x = pos.x
        self.old_y = pos.y

    def reset(self, pos):
        self.old_x = None
        self.old_y = None      

    def changeW(self,pos):
        self.pen = pos

    def save(self):
        width = 600
        height = 500
        x = self.master.winfo_rootx() + self.c.winfo_x()
        y = self.master.winfo_rooty() + self.c.winfo_y()
        x1 = x + width
        y1 = y + height

        PIL.ImageGrab.grab().crop((x,y,x1,y1)).save('static/bild.png')
            
    def clear(self):
        self.c.delete(ALL)

    def open(self):
        self.clear()
        ord.SkapaOrd()
        with open('Ritat_ord.json', 'r', encoding='utf8') as ord_file:
            j_ord = json.load(ord_file)
        self.word = str(j_ord)
        self.new_word.config(text=f'{self.word.upper()}')

    def color_pen_change(self):
        self.pen_color=colorchooser.askcolor(color=self.pen_color)[1]

    def change_c_color(self):
        self.c_color=colorchooser.askcolor(color=self.c_color)[1]
        self.c['bg'] = self.c_color

    def drawWidgets(self):
        self.controls = Frame(self.master,padx = 3,pady = 3)
        Label(self.controls, text='Storlek: ',font=(10)).grid(row=0,column=0)
        self.slider = ttk.Scale(self.controls,from_= 5, to = 100, command=self.changeW,orient=HORIZONTAL)
        self.slider.set(self.pen)
        self.slider.grid(row=0,column=1, ipadx=100)
        self.controls.pack()
        
        self.c = Canvas(self.master,width=600,height=500,bg=self.c_color)
        self.c.pack()

        self.done = Button(text='KLAR', bg='#007ad9', fg='white', command = self.save)
        self.done.pack(side=LEFT)

        self.color_button = Button(text='FÄRG', bg='#007ad9', fg='white', command = self.color_pen_change)
        self.color_button.pack(side=LEFT)

        self.c_color_button = Button(text='BACKGRUNDSFÄRG', bg='#007ad9', fg='white', command = self.change_c_color)
        self.c_color_button.pack(side=LEFT)

        self.clear_button = Button(text='RENSA', bg='#007ad9', fg='white', command = self.clear)
        self.clear_button.pack(side=LEFT)

        self.new_word = Button(text='KLICKA FÖR ATT FÅ ETT ORD', bg='#007ad9', fg='white', command=self.open)
        self.new_word.pack(side=BOTTOM, fill=X)
    

if __name__ == '__main__':
    root = Tk()
    main(root)
    root.title('Skribble')
    root.mainloop()
    


