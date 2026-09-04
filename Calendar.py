import tkinter
import calendar
screen = tkinter.Tk()
def create_calender():
    year = int(entry1.get())
    calendar_data = calendar.calendar(year)
    calendar_screen = tkinter.Tk()
    calendar_screen.geometry("700x700")
    text = tkinter.Text(calendar_screen)
    text.pack()
    text.insert(tkinter.END,calendar_data)
    calendar_screen.mainloop()
label1 = tkinter.Label(screen,text="CALENDAR",bg="gray",font=("Times New Roman",50,"bold"))
label1.pack()
label2 = tkinter.Label(screen,text="Enter Year",bg="light green")
label2.pack()
entry1 = tkinter.Entry(screen)
entry1.pack()
button1 = tkinter.Button(screen,text="Show Calender",bg="red",command=create_calender)
button1.pack()
button2 = tkinter.Button(screen,text="exit",bg="red")
button2.pack()


screen.mainloop()