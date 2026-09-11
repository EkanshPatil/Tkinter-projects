import tkinter
import random
screen = tkinter.Tk()
options = ["rock","paper","scissors"]
computer_score = 0
player_score = 0
def game(player_choice):
    global computer_score
    global player_score
    computer_choice = random.choice(options)
    computer_label1.config(text=f"Computer selected: {computer_choice}")
    player_label1.config(text=f"You selected: {player_choice}")
    if player_choice == "rock" and computer_choice == "scissors" or player_choice == "paper" and computer_choice == "rock" or player_choice == "scissors" and computer_choice == "paper":
        player_score += 1
        winner_label.config(text="You won!!!!",fg="green",font=("bold"))
    elif player_choice == "rock" and computer_choice == "paper" or player_choice == "paper" and computer_choice == "scissors" or player_choice == "scissors" and computer_choice == "rock":
        computer_score += 1
        winner_label.config(text="You lost!!",fg="red",font=("bold"))
    elif player_choice == computer_choice:
        winner_label.config(text="Tie!",fg="gold",font=("bold"))
    computer_label2.config(text=f"Computer score: {computer_score}")
    player_label2.config(text=f"Your score: {player_score}")

screen.geometry("1000x1000")
label1 = tkinter.Label(screen,text="Rock Paper Scissors!",font=("New Times Roman",50,"bold"),fg="gray")
label1.grid(row=1,column=2,columnspan=7)
winner_label = tkinter.Label(screen)
winner_label.grid(row=2,column=3)
label2 = tkinter.Label(screen,fg="gray",text="Your Options:",font=(20))
label2.grid(row=2,column=1)

rock_button = tkinter.Button(screen,bg="red",text="Rock",fg="white",font=("bold"),command=lambda:game("rock"))
rock_button.grid(row=3,column=2)
paper_button = tkinter.Button(screen,bg="gray",text="Paper",fg="white",font=("bold"),command=lambda:game("paper"))
paper_button.grid(row=3,column=3)
scissors_button = tkinter.Button(screen,bg="blue",text="Scissors",fg="white",font=("bold"),command=lambda:game("scissors"))
scissors_button.grid(row=3,column=4)

label3 = tkinter.Label(screen,fg="gray",text="score:",font=(20))
label3.grid(row=4,column=1)

player_label1 = tkinter.Label(screen,text="You selected: ",font=(10))
player_label1.grid(row=5,column=2)
player_label2 = tkinter.Label(screen,text="Your score: ",font=(10))
player_label2.grid(row=5,column=3)

computer_label1 = tkinter.Label(screen,text="Computer selected: ",font=(10))
computer_label1.grid(row=6,column=2)
computer_label2 = tkinter.Label(screen,text="Computer score: ",font=(10))
computer_label2.grid(row=6,column=3)

screen.mainloop()
