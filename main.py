from tkinter import *
import random

def act():
    choice_entry.delete(0,END)
    coin = (1, 3, 4, 5, 6)
    toss = random.choice(coin)
    choice_entry.insert(0, toss)


root = Tk()
root.title('coin toss by Oditha')
root.geometry("300x250")

l = Label(root, text= "Tossing program by Oditha")
l.pack(pady=20)

choice_entry = Entry(root, text='',font=("Helvetica",24),bd=0,bg="systembuttonface")
choice_entry.pack(pady=1,padx=135)

frame = Frame(root)
frame.pack(pady=20)

button_1 = Button(frame, text="toss", command = act)
button_1.grid(row=0, column=0, pady=20)

root.mainloop()