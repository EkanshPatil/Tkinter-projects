import tkinter
screen = tkinter.Tk()
def add_numbers():
    number1 = int(entry1.get())
    number2 = int(entry2.get())
    result = f"result= {number1 + number2}"
    result_text = tkinter.Text(screen,font=("comic sans",25,"bold"),width=10,height=10)
    result_text.pack()
    result_text.insert(tkinter.END,result)
    screen.mainloop()
label1 = tkinter.Label(screen,text="Enter two numbers")
label1.pack()
entry1 = tkinter.Entry(screen)
entry1.pack()
entry2 = tkinter.Entry(screen)
entry2.pack()
button1 = tkinter.Button(screen,text="Add",bg="green",command=add_numbers)
button1.pack()

screen.mainloop()