from PIL import ImageTk, Image, ImageDraw
import PIL
from tkinter import *
import json
from tkinter.colorchooser import askcolor


width = 800
height = 400
center = height//2
white = (255, 255, 255)
green = (0,128,0)
standard_pen_storlek = 5.0
standard_färg = 'black'

color = standard_färg

def save():
    filename = "static/bild.png"
    image1.save(filename)

def choose_color():
    color = standard_färg
    color = askcolor(color=color)

def paint(event):
    python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_oval(x1, y1, x2, y2, fill="black",width=5)
    draw.line([x1, y1, x2, y2],fill="black",width=5)
    if x1 and y1: 
        cv.create_line(fill=choose_color, capsyle=ROUND, smooth=TRUE, splinesteps=36)
    old_x = None
    old_y = None
    cv.bind("<B1-Motion>")
    paint_color = 'black'
    if old_x and old_y:
        cv.create_line(old_x, old_y, event.x, event.y,
                            width=50, fill=paint_color,
                            capstyle=ROUND, smooth=TRUE, splinesteps=36)
    old_x = event.x
    old_y = event.y
def reset(event):
    old_x, old_y = None, None

root = Tk()



# Tkinter create a canvas to draw on
cv = Canvas(root, width=width, height=height, bg='white')
cv.pack()

# PIL create an empty image and draw object to draw on
# memory only, not visible
image1 = PIL.Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)

# do the Tkinter canvas drawings (visible)
# cv.create_line([0, center, width, center], fill='green')

cv.pack(expand=YES, fill=BOTH)
cv.bind("<B1-Motion>", paint)


with open('Ritat_ord.json', 'r', encoding='utf8') as ord_file:
    jord = json.load(ord_file)

test = str(jord)

message = Label(root, text=f'rita följande ord: {test}')
message.pack(side=BOTTOM)

# do the PIL image/draw (in memory) drawings
# draw.line([0, center, width, center], green)

# PIL image can be saved as .png .jpg .gif or .bmp file (among others)
# filename = "my_drawing.png"
# image1.save(filename)
button=Button(text="save",command=save)
färg_knapp = Button(text = 'färg', command=choose_color)
färg_knapp.pack(side=LEFT)
button.pack()
root.mainloop()

