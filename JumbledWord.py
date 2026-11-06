import tkinter 
import tkinter.messagebox
import random

words = ["computer","tkinter","keyboard","console","python","vscode","mouse","personalcomputer","pygame","turtle"]
screen = tkinter.Tk()
screen.config(bg="black")

def scramble():
    pick = random.choice(words)
    choice = list(pick)
    random.shuffle(choice)
    jumbled = "".join(choice)
    jumbled_label.config(text=jumbled)

label1 = tkinter.Label(screen,font=("Redaction 10",30),text="Jumbled Word Game!",fg="white",bg="black")
label1.grid(row=1,column=2)
jumbled_label = tkinter.Label(screen,font=("comic sans",20),text="nil",fg="white",bg="black")
jumbled_label.grid(row=2,column=2)
entry = tkinter.Entry(screen)
entry.grid(row=3,column=2,columnspan=3)
guess_button = tkinter.Button(screen,text="Confirm guess",fg="lime",bg="SlateGray")
guess_button.grid(row=4,column=2,columnspan=2)
reset_button = tkinter.Button(screen,text="Reset",fg="red",bg="SlateGray")
reset_button.grid(row=5,column=2,columnspan=2)
score_label = tkinter.Label(screen,text="score: ",fg="gold",font=("comic sans",15),bg="black")
score_label.grid(row=6,column=1)

scramble()
screen.mainloop()