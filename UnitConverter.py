import tkinter
screen = tkinter.Tk()
screen.geometry("500x300")
def convert():
    input = int(entry1.get())
    grams = input*1000
    pounds = input*2.20462
    ounces = input*35.274
    grams_text.config(text=grams)
    pounds_text.config(text=pounds)
    ounces_text.config(text=ounces)
label1 = tkinter.Label(screen,text="Enter the weight in Kilograms")
label1.grid(row=1,column=1)
entry1 = tkinter.Entry(screen)
entry1.grid(row=1,column=2)
button1 = tkinter.Button(screen,text="Convert",bg="green",command=convert)
button1.grid(row=1,column=3)
grams_label = tkinter.Label(screen,text="Grams:")
grams_label.grid(row=2,column=1)
grams_text = tkinter.Label(screen)
grams_text.grid(row=3,column=1)

pounds_label = tkinter.Label(screen,text="Pounds:")
pounds_label.grid(row=2,column=2)
pounds_text = tkinter.Label(screen)
pounds_text.grid(row=3,column=2)

ounces_label = tkinter.Label(screen,text="ounces:")
ounces_label.grid(row=2,column=3)
ounces_text = tkinter.Label(screen)
ounces_text.grid(row=3,column=3)

screen.mainloop()