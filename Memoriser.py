import tkinter
import tkinter.filedialog
screen = tkinter.Tk()
def save():
    selected_file = tkinter.filedialog.asksaveasfile()
    if selected_file != None:
        for i in list1.get(0,tkinter.END):
            print(i,file=selected_file)

def delete():
    selected = list1.curselection()
    for i in reversed(selected):
        list1.delete(i)

def add():
    input = add_entry.get()
    list1.insert(tkinter.END,input)

def open():
    open_file = tkinter.filedialog.askopenfile()
    if open_file != None:
        items = open_file.readlines()
        for i in items:
            list1.insert(tkinter.END,i)


open_button = tkinter.Button(screen,text="OPEN",bg="green",command=open)
open_button.grid(row=1,column=1)
delete_button = tkinter.Button(screen,text="DELETE",bg="gold",command=delete)
delete_button.grid(row=1,column=2)
save_button = tkinter.Button(screen,text="SAVE",bg="red",command=save)
save_button.grid(row=1,column=3)
add_entry = tkinter.Entry(screen)
add_entry.grid(row=2,column=1,columnspan=2)
add_button = tkinter.Button(screen,text="ADD",bg="lightblue",command=add)
add_button.grid(row=2,column=3)
list1 = tkinter.Listbox(screen,selectmode=tkinter.MULTIPLE)
list1.grid(row=3,column=1,columnspan=3)

screen.mainloop()
