import tkinter
from tkinter.colorchooser import askcolor
thick = 5
color = "black"
old_x = None
old_y = None
eraser_on = False
screen = tkinter.Tk()

def draw(event):
    global old_x
    global old_y
    global thick
    thick = scale1.get()
    if eraser_on == True:
        drawing_colour = "white"
    else:
        drawing_colour = color
    if old_x and old_y:
        canvas.create_line(old_x,old_y,event.x,event.y,fill=drawing_colour,width=thick)
    old_x = event.x
    old_y = event.y

def colour():
    global color
    color = askcolor()[1]

def eraser():
    global eraser_on
    eraser_on = True


def pen():
    global eraser_on
    eraser_on = False

pen_button = tkinter.Button(screen,text="Pen",command=pen)
pen_button.grid(row=1,column=1)
color_button = tkinter.Button(screen,text="Color",command=colour)
color_button.grid(row=1,column=2)
eraser_button = tkinter.Button(screen,text="Eraser",command=eraser)
eraser_button.grid(row=1,column=3)
scale1 =tkinter.Scale(screen,from_=1,to=20)
scale1.grid(row=1,column=4)
canvas = tkinter.Canvas(screen,width=1000,height=500)
canvas.bind("<B1-Motion>",draw)
canvas.grid(row=2,column=1,columnspan=5)






screen.mainloop()
