import tkinter 
import tkinter.messagebox
import random

words = ["computer","tkinter","keyboard","console","python","vscode","mouse","personalcomputer","pygame","turtle"]
screen = tkinter.Tk()
screen.config(bg="black")
score = 0

def scramble():
    global pick
    global choice
    pick = random.choice(words)
    choice = list(pick)
    random.shuffle(choice)
    jumbled = "".join(choice)
    jumbled_label.config(text=jumbled)
    words.remove(pick)

def guess():
    global pick
    global score
    user_guess = entry.get()
    if user_guess == pick:
        tkinter.messagebox.showinfo(title="CORRECT!",message="Congratulations, you have guessed correctly!")
        scramble()
        score +=2
        score_label.config(text=f"score:{score}")
    else:
        tkinter.messagebox.showerror(title="WRONG!",message=f"Oops! you got the word wrong! The word was {pick}! ")
        scramble()
        score -=2
        score_label.config(text=f"score:{score}")

def hint():
    global pick
    global score
    letter = pick[0]
    tkinter.messagebox.showinfo(title="HINT!",message=f"The first letter of the word is: {letter}")
    score -=1
    score_label.config(text=f"score:{score}")
    
label1 = tkinter.Label(screen,font=("Redaction 10",30),text="Jumbled Word Game!",fg="white",bg="black")
label1.grid(row=1,column=2)
jumbled_label = tkinter.Label(screen,font=("comic sans",20),text="nil",fg="white",bg="black")
jumbled_label.grid(row=2,column=2)
entry = tkinter.Entry(screen)
entry.grid(row=3,column=2,columnspan=3)
guess_button = tkinter.Button(screen,text="Confirm guess",fg="lime",bg="SlateGray",command=guess)
guess_button.grid(row=4,column=2,columnspan=2)
hint_button = tkinter.Button(screen,text="Hint",fg="red",bg="SlateGray",command=hint)
hint_button.grid(row=5,column=2,columnspan=2)
score_label = tkinter.Label(screen,text=f"score: ",fg="gold",font=("comic sans",15),bg="black")
score_label.grid(row=6,column=1)

scramble()
screen.mainloop()
