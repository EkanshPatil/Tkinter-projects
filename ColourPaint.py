import tkinter
thickness = 5
color = "black"
old_x = None
old_y = None
screen = tkinter.Tk()

def draw(event):
    if old_x and old_y:
        canvas.create_line(old_x,old_y,event.x,event.y,fill=color,thickness=thickness)

pen_button = tkinter.Button(screen,text="Pen")
pen_button.grid(row=1,column=1)
brush_button = tkinter.Button(screen,text="Brush")
brush_button.grid(row=1,column=2)
color_button = tkinter.Button(screen,text="Color")
color_button.grid(row=1,column=3)
eraser_button = tkinter.Button(screen,text="Eraser")
eraser_button.grid(row=1,column=4)
scale1 =tkinter.Scale(screen,from_=1,to=20)
scale1.grid(row=1,column=5)
canvas = tkinter.Canvas(screen,width=300,height=300)
canvas.bind("<<B1-Motion>>")
canvas.grid(row=2,column=1,columnspan=5)






screen.mainloop()