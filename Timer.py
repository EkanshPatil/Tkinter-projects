import tkinter
import time
import tkinter.messagebox
screen = tkinter.Tk()
hours = tkinter.StringVar()
minutes = tkinter.StringVar()
seconds = tkinter.StringVar()
hours.set("00")
minutes.set("00")
seconds.set("00")
def countdown():
    user_hours = int(hours_entry.get())
    user_minutes = int(minutes_entry.get())
    user_seconds = int(seconds_entry.get())

    while True:
        time.sleep(1)
        if user_seconds > 0:
            user_seconds -=1
        elif user_minutes > 0:
            user_minutes -= 1
            user_seconds += 59    
        elif user_hours > 0:
            user_hours -= 1
            user_minutes +=59
            user_seconds +=59
        else:
            tkinter.messagebox.showwarning(title="TIMER DONE!",message="The timer is done!")
            break
        hours.set(user_hours)
        minutes.set(user_minutes)
        seconds.set(user_seconds)
        screen.update()

            
hours_entry = tkinter.Entry(screen,width=2,textvariable=hours)
hours_entry.grid(row=1,column=1,padx=20)
minutes_entry = tkinter.Entry(screen,width=2,textvariable=minutes)
minutes_entry.grid(row=1,column=2,padx=20)
seconds_entry = tkinter.Entry(screen,width=2,textvariable=seconds)
seconds_entry.grid(row=1,column=3,padx=20)
time_button = tkinter.Button(screen,text="Set Timer",command=countdown)
time_button.grid(row=3,column=2)

tkinter.mainloop()