import tkinter
import tkinter.messagebox
screen = tkinter.Tk()

def name():
    player_name = name_entry.get()
    if len(player_name) == 0:
        tkinter.messagebox.showerror(title="Error",message="You have not entered your name!")
    else:
        tkinter.messagebox.showinfo(title="Name",message=f"Hello {player_name},nice to meet you! I have picked a number between 1 and 20 and you have to guess it! ")
label1 = tkinter.Label(screen,text="The Number Game!",fg="red",font=(50))
label1.grid(row=1, column=2)
label2 = tkinter.Label(screen,text="Welcome to our game!",fg="gray")
label2.grid(row=2,column=2)

label3 = tkinter.Label(screen,text="What is your name?")
label3.grid(row=5,column=1)
name_entry = tkinter.Entry(screen)
name_entry.grid(row=5,column=2)
name_button = tkinter.Button(screen,text="OK",command=name)
name_button.grid(row=5,column=3)

label4 = tkinter.Label(screen,text="Take a guess:")
label4.grid(row=7,column=1)
guess_entry = tkinter.Entry(screen)
guess_entry.grid(row=7,column=2)
guess_button = tkinter.Button(screen,text="Guess")
guess_button.grid(row=7,column=3)

screen.mainloop()