from tkinter import *
from tkinter import ttk, colorchooser, filedialog
import PIL, json, requests
from PIL import ImageGrab
import ord


class main:
    def __init__(self,master):
        self.master = master
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.drawWidgets()
        self.c.bind('<B1-Motion>',self.paint)
        self.c.bind('<ButtonRelease-1>',self.reset)


    def paint(self,e):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x,self.old_y,e.x,e.y,width=self.penwidth,fill=self.color_fg,capstyle=ROUND,smooth=True)

        self.old_x = e.x
        self.old_y = e.y

    def reset(self,e):
        self.old_x = None
        self.old_y = None      

    def changeW(self,e):
        self.penwidth = e

    def save(self):
        x = self.master.winfo_rootx() + self.c.winfo_x()
        y = self.master.winfo_rooty() + self.c.winfo_y()
        x1 = x + self.c.winfo_width()
        y1 = y + self.c.winfo_height()

        PIL.ImageGrab.grab().crop((x,y,x1,y1)).save('static/bild.png')
            
    def clear(self):
        self.c.delete(ALL)

    def open(self):
        self.clear()
        ord.SkapaOrd()
        with open('Ritat_ord.json', 'r', encoding='utf8') as ord_file:
            jord = json.load(ord_file)
        self.word = str(jord)
        self.ny.config(text=f'{self.word}')

    def change_fg(self):
        self.color_fg=colorchooser.askcolor(color=self.color_fg)[1]

    def change_bg(self):
        self.color_bg=colorchooser.askcolor(color=self.color_bg)[1]
        self.c['bg'] = self.color_bg

    def drawWidgets(self):
        self.controls = Frame(self.master,padx = 3,pady = 3)
        Label(self.controls, text='Pen Width: ',font=('',15)).grid(row=0,column=0)
        self.slider = ttk.Scale(self.controls,from_= 5, to = 100, command=self.changeW,orient=HORIZONTAL)
        self.slider.set(self.penwidth)
        self.slider.grid(row=0,column=1,ipadx=30)
        self.controls.pack()
        
        self.c = Canvas(self.master,width=500,height=400,bg=self.color_bg,)
        self.c.pack(fill=BOTH,expand=True)

        self.klar = Button(text='KLAR', bg='#007ad9', fg='white', command = self.save)
        self.klar.pack(side=LEFT)

        self.color = Button(text='FÄRG', bg='#007ad9', fg='white', command = self.change_fg)
        self.color.pack(side=LEFT)

        self.colorbg = Button(text='BACKGRUNDSFÄRG', bg='#007ad9', fg='white', command = self.change_bg)
        self.colorbg.pack(side=LEFT)

        self.clearbg = Button(text='CLEAR', bg='#007ad9', fg='white', command = self.clear)
        self.clearbg.pack(side=LEFT)


        self.ny = Button(text='Klicka för att få ettord', bg='#007ad9', fg='white', command=self.open)
        self.ny.pack(side=BOTTOM, fill=X)
    


        
        

if __name__ == '__main__':
    root = Tk()
    main(root)
    root.title('DrawingApp')
    root.mainloop()
    


