import tkinter
screen = tkinter.Tk()
label1 = tkinter.Label(screen,text="Hello i am a label!",bg="red",fg="blue")
label1.pack()
button1 = tkinter.Button(screen,text="Hello i am a button!",font=("comic sans",30,"bold"))
button1.pack(pady=60,ipadx=50)
entry1 = tkinter.Entry(screen)
entry1.pack(padx=25)
screen.mainloop()