from tkinter import *

var = ''

# functions

def press(num):
    global var
    var = var + str(num)
    entry_var.set(var)


def equal():
    global var
    eql = eval(var)
    entry_var.set(str(eql))


def clear():
    global var
    var = ''
    entry_var.set('')

# Tkinter

root = Tk()
root.config(bg="#0e0d0a")
root.title("                                                           CALCULATOR    ")
root.iconbitmap("calcc.ico")

entry_var = StringVar()



# Entry

myEntry = Entry(
    root,
    textvariable=entry_var,
    fg='black',
    bg='#7232a1',
    font=('ariel', 50),
    width=10,
    )
myEntry.grid(
    row=0,
    column=0,
    columnspan=5,
    padx=15,
    pady=15,
    ipady=20,
    ipadx=50,
    )

# Button

button_1 = Button(
    root,
    text='1',
    font=('ariel', 50),
    bg='black',
    fg='white',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press(1),
    )
button_1.grid(row=1, column=0, padx=5, pady=5)

button_2 = Button(
    root,
    text='2',
    font=('ariel', 50),
    bg='black',
    fg='white',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press(2),
    )
button_2.grid(row=1, column=1, padx=5, pady=5)

button_3 = Button(
    root,
    text='3',
    font=('ariel', 50),
    bg='black',
    fg='white',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press(3),
    )
button_3.grid(row=1, column=2, padx=5, pady=5)

button_4 = Button(
    root,
    text='4',
    font=('ariel', 50),
    bg='black',
    fg='white',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press(4),
    )
button_4.grid(row=2, column=0, padx=5, pady=5)

button_5 = Button(
    root,
    text='5',
    font=('ariel', 50),
    bg='black',
    fg='white',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press(5),
    )
button_5.grid(row=2, column=1, padx=5, pady=5)

button_6 = Button(
    root,
    text='6',
    font=('ariel', 50),
    bg='black',
    fg='white',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press(6),
    )
button_6.grid(row=2, column=2, padx=5, pady=5)

button_7 = Button(
    root,
    text='7',
    font=('ariel', 50),
    bg='black',
    fg='white',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press(7),
    )
button_7.grid(row=3, column=0, padx=5, pady=5)

button_8 = Button(
    root,
    text='8',
    font=('ariel', 50),
    bg='black',
    fg='white',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press(8),
    )
button_8.grid(row=3, column=1, padx=5, pady=5)

button_9 = Button(
    root,
    text='9',
    font=('ariel', 50),
    bg='black',
    fg='white',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press(9),
    )
button_9.grid(row=3, column=2, padx=5, pady=5)

button_0 = Button(
    root,
    text='0',
    font=('ariel', 50),
    bg='black',
    fg='white',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press(0),
    )
button_0.grid(row=4, column=1, padx=5, pady=5)

button_clear = Button(
    root,
    text='C',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=clear,
    )
button_clear.grid(row=4, column=0)

button_Multiply = Button(
    root,
    text='x',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press('*'),
    )
button_Multiply.grid(row=1, column=3, padx=5, pady=5)

button_Divide = Button(
    root,
    text='/',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press('/'),
    )
button_Divide.grid(row=2, column=3, padx=5, pady=5)

button_Add = Button(
    root,
    text='+',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press('+'),
    )
button_Add.grid(row=3, column=3, padx=5, pady=5)

button_point = Button(
    root,
    text='.',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press('.'),
    )
button_point.grid(row=4, column=2, padx=5, pady=5, ipadx='9')

button_Sub = Button(
    root,
    text='-',
    font=('Digital-7', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press('-'),
    )
button_Sub.grid(row=4, column=3, padx=5, pady=5)

button_Equal = Button(
    root,
    text='=',
    font=('Digital-7', 50),
    bg='black',
    bd=0,
    activebackground='black',
    fg='#fdc703',
    activeforeground='green',
    command=equal,
    )
button_Equal.grid(row=5, column=0, columns=2, ipadx=95, ipady=10)

root.mainloop()
