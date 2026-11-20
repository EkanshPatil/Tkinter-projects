import tkinter
from time import strftime
screen = tkinter.Tk()

def time():
    current = strftime("%I,%M,%S,%p")
    clock_label.config(text=current)
    clock_label.after(1000,time)

clock_label = tkinter.Label(screen,text="hello",fg="white",bg="orange",font=("Redaction 10",50))
clock_label.grid(row=1,column=2,rowspan=5,columnspan=5)
time()

tkinter.mainloop()