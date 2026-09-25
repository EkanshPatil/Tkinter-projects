import tkinter
import tkinter.ttk
screen = tkinter.Tk()
range_variable = tkinter.IntVar()

def muiltiply():
    output = ""
    number = int(number_box.get())
    range_var = int(range_variable.get())
    for i in range(range_var):
        output = output + f"{number} X {i + 1} = {number*(i+1)}\n"
    number_label.config(text=output)
label1 = tkinter.Label(screen,text="Mathematical table")
label1.grid(row = 1,column=2)
label2 = tkinter.Label(screen,text="Number and Range:")
label2.grid(row=2,column=1)
number_box = tkinter.ttk.Combobox(screen)
number_box.grid(row=2,column=2)
number_box["values"] = list(range(1,101,1))
rb1 = tkinter.ttk.Radiobutton(screen,text="10",variable=range_variable,value=10)
rb1.grid(row=2,column=3)
rb2 = tkinter.ttk.Radiobutton(screen,text="20",variable=range_variable,value=20)
rb2.grid(row=3,column=3)
rb3 = tkinter.ttk.Radiobutton(screen,text="30",variable=range_variable,value=30)
rb3.grid(row=4,column=3)
number_button = tkinter.Button(screen,text="Generate",command=muiltiply)
number_button.grid(row=5,column=2)
number_label = tkinter.Label(screen)
number_label.grid(row=6,column=2)




screen.mainloop()