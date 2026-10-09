import tkinter
import random
import tkinter.messagebox
screen = tkinter.Tk()

def press(user_choice):
    if user_choice in button_list:
        user_choice.config(text="X",bg="lightblue")
        button_list.remove(user_choice)
        computer_choice = random.choice(button_list)
        computer_choice.config(text="O",bg="tomato")
        button_list.remove(computer_choice)
        check_winner()

def check_winner():
    for i in winning_combinations:
        if i[0]["text"] == "X" and i[1]["text"] == "X" and i[2]["text"] == "X":
            tkinter.messagebox.showinfo(title="YOU WIN!",message="Congratulations! you win!!!")

button1 = tkinter.Button(screen,font=50,command= lambda:press(button1),width=5,height=3)
button1.grid(row=1,column=1)
button2 = tkinter.Button(screen,font=50,command= lambda:press(button2),width=5,height=3)
button2.grid(row=1,column=2)
button3 = tkinter.Button(screen,font=50,command= lambda:press(button3),width=5,height=3)
button3.grid(row=1,column=3)
button4 = tkinter.Button(screen,font=50,command= lambda:press(button4),width=5,height=3)
button4.grid(row=2,column=1)
button5 = tkinter.Button(screen,font=50,command= lambda:press(button5),width=5,height=3)
button5.grid(row=2,column=2)
button6 = tkinter.Button(screen,font=50,command= lambda:press(button6),width=5,height=3)
button6.grid(row=2,column=3)
button7 = tkinter.Button(screen,font=50,command= lambda:press(button7),width=5,height=3)
button7.grid(row=3,column=1)
button8 = tkinter.Button(screen,font=50,command= lambda:press(button8),width=5,height=3)
button8.grid(row=3,column=2)
button9 = tkinter.Button(screen,font=50,command= lambda:press(button9),width=5,height=3)
button9.grid(row=3,column=3)

button_list = [button1,button2,button3,button4,button5,button6,button7,button8,button9]
winning_combinations = [(button1,button2,button3),(button4,button5,button6),(button7,button8,button9),(button1,button4,button7),(button2,button5,button8),(button3,button6,button9),(button1,button5,button9),(button3,button5,button7)]

screen.mainloop()