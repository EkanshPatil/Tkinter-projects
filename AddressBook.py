import tkinter
import tkinter.messagebox
import tkinter.filedialog
screen = tkinter.Tk()
address_book = {}

def display():
    list1.delete(0,tkinter.END)
    for key in address_book.keys():
        list1.insert(tkinter.END,key)
    name_entry.delete(0,tkinter.END)
    address_entry.delete(0,tkinter.END)
    mobile_entry.delete(0,tkinter.END)
    email_entry.delete(0,tkinter.END)
    birthday_entry.delete(0,tkinter.END)

def show(event):
    index = list1.curselection()
    selected = list1.get(index)
    values = address_book[selected]
    tkinter.messagebox.showinfo(title=selected,message=f"Name: {selected}\nAddress: {values[0]}\nMobile: {values[1]}\nEmail: {values[2]}\nBirthday: {values[3]}")

def open():
    global address_book
    open_file = tkinter.filedialog.askopenfile()
    if open_file != None:
        address_book = eval(open_file.read())
        display()
        
def edit():
    index = list1.curselection()
    selected = list1.get(index)
    values = address_book[selected]
    name_entry.insert(tkinter.END,selected)
    address_entry.insert(tkinter.END,values[0])
    mobile_entry.insert(tkinter.END,values[1])
    email_entry.insert(tkinter.END,values[2])
    birthday_entry.insert(tkinter.END,values[3])

def delete():
    index = list1.curselection()
    selected = list1.get(index)
    del address_book[selected]
    display()          

def update():
    global address_book
    name = name_entry.get()
    address = address_entry.get()
    mobile = mobile_entry.get()
    email = email_entry.get()
    birthday = birthday_entry.get()
    address_book[name] = [address,mobile,email,birthday]
    print(address_book)
    display()

def save():
    selected_file = tkinter.filedialog.asksaveasfile()
    if selected_file != None:
        print(address_book,file=selected_file)


label1 = tkinter.Label(screen,text="My Address Book:")
label1.grid(row=1,column=1)
open_button = tkinter.Button(screen,text="Open",command=open)
open_button.grid(row=1,column=2)
list1 = tkinter.Listbox(screen)
list1.bind("<<ListboxSelect>>",show)
list1.grid(row=2,column=1,columnspan=3,rowspan=6)
label2 = tkinter.Label(screen,text="Name:")
label2.grid(row=2,column=4)
name_entry = tkinter.Entry(screen)
name_entry.grid(row=2,column=5,columnspan=2)
label3 = tkinter.Label(screen,text="Address:")
label3.grid(row=4,column=4)
address_entry = tkinter.Entry(screen)
address_entry.grid(row=4,column=5,columnspan=2)
label4 = tkinter.Label(screen,text="Mobile:")
label4.grid(row=5,column=4)
mobile_entry = tkinter.Entry(screen)
mobile_entry.grid(row=5,column=5,columnspan=2)
label5 = tkinter.Label(screen,text="Email:")
label5.grid(row=6,column=4)
email_entry = tkinter.Entry(screen)
email_entry.grid(row=6,column=5,columnspan=2)
label6 = tkinter.Label(screen,text="Birthday:")
label6.grid(row=7,column=4)
birthday_entry = tkinter.Entry(screen)
birthday_entry.grid(row=7,column=5,columnspan=2)
edit_button = tkinter.Button(screen,text="Edit",command=edit)
edit_button.grid(row=8,column=1)
delete_button = tkinter.Button(screen,text="Delete",command=delete)
delete_button.grid(row=8,column=2)
update_button = tkinter.Button(screen,text="Update/Add",command=update)
update_button.grid(row=8,column=5)
save_button = tkinter.Button(screen,text="Save",command=save)
save_button.grid(row=9,column=2,columnspan=3)



screen.mainloop()
