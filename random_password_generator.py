import random
from tkinter import *
import tkinter

# CREATING THE WINDOW
window = Tk()

# GIVING THE WINDOW A TITLE
window.title('password generator')

# SETTING THE WINDOW DIMENSIONS
window.geometry("600x600")

# ADDING A LABEL
Label(window, text='password genenrator', font=("arial italic", 18)).pack()

# CONVERTING THE LENGTH OBTAINED FROM THE CHECKBOX INTO AN INTEGER VALUE
length1 = tkinter.IntVar()
length2 = tkinter.IntVar()
length3 = tkinter.IntVar()
length4 = tkinter.IntVar()
length5 = tkinter.IntVar()

# CREATING THE PASSWORD GENERATOR FUNCTION
def generate_password(n):
    rand_pass = ''
    alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*12345'
    for items in range(n):
        rand_pass += random.choice(alphabets)
        label = Label(window, text=rand_pass, font=("arial italic", 20))
        label.place(height=50, x=250, y=40)
    return rand_pass

# FUNCTION THAT CALLS THE MAIN GENERATE PASSWORD FUNCTION TO GENEREATE A PASSWORD OF A SPECIFIC LENGTH
def getLength():
    if length1.get() == 4:
        generate_password(4)
    elif length2.get() == 6:
        generate_password(6)
    elif length3.get() == 8:
        generate_password(8)
    elif length4.get() == 10:
        generate_password(10)
    else:
        generate_password(12)

# CREATING THE GENERATE PASSWORD BUTTON
button = Button(window, text='generate password', font=(
    "arial italic", 10), bg='blue', command=getLength)
button.place(x=200, y=100)

# CREATING THE CHECKBOX BUTTON
Checkbutton(text='4 characters', onvalue=4, offvalue=0,
            variable=length1).place(x=250, y=150)
Checkbutton(text='6 characters', onvalue=6, offvalue=0,
            variable=length2).place(x=250, y=170)
Checkbutton(text='8 characters', onvalue=8, offvalue=0,
            variable=length3).place(x=250, y=190)
Checkbutton(text='10 characters', onvalue=10, offvalue=0,
            variable=length4).place(x=250, y=210)
Checkbutton(text='12 characters', onvalue=12, offvalue=0,
            variable=length5).place(x=250, y=230)

if __name__ == '__main__':
    window.mainloop()
