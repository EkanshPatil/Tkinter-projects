import tkinter

screen = tkinter.Tk()
address_book = {}

def open():
    pass

def edit():
    pass

def delete():
    pass           

def update():
    name = name_entry.get()
    address = address_entry.get()
    mobile = mobile_entry.get()
    email = email_entry.get()
    birthday = birthday_entry.get()
    address_book[name] = [address,mobile,email,birthday]
def save():
    pass

label1 = tkinter.Label(screen,text="My Address Book:")
label1.grid(row=1,column=1)
open_button = tkinter.Button(screen,text="Open")
open_button.grid(row=1,column=2)
list1 = tkinter.Listbox(screen)
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
edit_button = tkinter.Button(screen,text="Edit")
edit_button.grid(row=8,column=1)
delete_button = tkinter.Button(screen,text="Delete")
delete_button.grid(row=8,column=2)
update_button = tkinter.Button(screen,text="Update/Add")
update_button.grid(row=8,column=5)
save_button = tkinter.Button(screen,text="Save")
save_button.grid(row=9,column=2,columnspan=3)
screen.mainloop()