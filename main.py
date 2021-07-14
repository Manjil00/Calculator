from tkinter import *

var = ''

# Functions

def press(num):                         #Press input function
    global var
    var = var + str(num)
    entry_var.set(var)


def equal():            # Totalling function
    global var
    eql = eval(var)
    entry_var.set(str(eql))
    var=str(eql)

def clear():           # Function to Clears/ Erases the data
    global var
    var = ''
    entry_var.set('')

# Tkinter
root = Tk()
root.config(bg="#0e0d0a")             # color is mid-black
root.title("                                                           CALCULATOR    ")   # Title equipped
root.iconbitmap("calcc.ico")          #calculator icon adding

entry_var = StringVar()



# Entry

myEntry = Entry(
    root,
    textvariable=entry_var,
    fg='black',
    bg='#7232a1',                              # Entry background color is LightPurple
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
    font=('Arial', 50),
    bg='black',
    fg='white',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press(1),
    )
button_1.grid(row=1, column=0, padx=5, pady=5)               # 1 button added and grid

button_2 = Button(
    root,
    text='2',
    font=('Arial', 50),
    bg='black',
    fg='white',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press(2),
    )
button_2.grid(row=1, column=1, padx=5, pady=5)            # 2 button added and grid

button_3 = Button(
    root,
    text='3',
    font=('Arial', 50),
    bg='black',
    fg='white',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press(3),
    )
button_3.grid(row=1, column=2, padx=5, pady=5)             # 3 button added and grid

button_4 = Button(
    root,
    text='4',
    font=('Arial', 50),
    bg='black',
    fg='white',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press(4),
    )
button_4.grid(row=2, column=0, padx=5, pady=5)                 # 4 button added and grid

button_5 = Button(
    root,
    text='5',
    font=('Arial', 50),
    bg='black',
    fg='white',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press(5),
    )
button_5.grid(row=2, column=1, padx=5, pady=5)                   # 5 button added and grid

button_6 = Button(
    root,
    text='6',
    font=('Arial', 50),
    bg='black',
    fg='white',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press(6),
    )
button_6.grid(row=2, column=2, padx=5, pady=5)              # 6 button added and grid

button_7 = Button(
    root,
    text='7',
    font=('Arial', 50),
    bg='black',
    fg='white',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press(7),
    )
button_7.grid(row=3, column=0, padx=5, pady=5)                 # 7 button added and grid

button_8 = Button(
    root,
    text='8',
    font=('Arial', 50),
    bg='black',
    fg='white',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press(8),
    )
button_8.grid(row=3, column=1, padx=5, pady=5)                     # 8 button added and grid

button_9 = Button(
    root,
    text='9',
    font=('Arial', 50),
    bg='black',
    fg='white',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press(9),
    )
button_9.grid(row=3, column=2, padx=5, pady=5)                   # 9 button added and grid

button_0 = Button(
    root,
    text='0',
    font=('Arial', 50),
    bg='black',
    fg='white',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press(0),
    )
button_0.grid(row=4, column=1, padx=5, pady=5)                         # 0 (Zero) button added and grid




button_clear = Button(
    root,
    text='C',
    font=('Arial', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=clear,
    )
button_clear.grid(row=4, column=0)                      # clear( C ) button added and grid


button_Multiply = Button(
    root,
    text='x',
    font=('Arial', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press('*'),
    )
button_Multiply.grid(row=1, column=3, padx=5, pady=5)             # Multiply button added and grid


button_Divide = Button(
    root,
    text='/',
    font=('Arial', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press('/'),
    )
button_Divide.grid(row=2, column=3, padx=5, pady=5)     # Divide button added and grid


button_Add = Button(
    root,
    text='+',
    font=('Arial', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press('+'),
    )
button_Add.grid(row=3, column=3, padx=5, pady=5)                      # Add button added and grid


button_point = Button(
    root,
    text='.',
    font=('Arial', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press('.'),
    )
button_point.grid(row=4, column=2, padx=5, pady=5, ipadx='9')                  # Decimal button added and grid

button_Sub = Button(
    root,
    text='-',
    font=('Arial', 50),
    bg='black',
    fg='#fdc703',
    bd=0,
    activeforeground='green',
    activebackground='black',
    command=lambda : press('-'),
    )
button_Sub.grid(row=4, column=3, padx=5, pady=5)                         # Substract button added and grid
# Substract button added and grid

button_Equal = Button(
    root,
    text='=',
    font=('Arial', 50),
    bg='black',
    bd=0,
    activebackground='black',
    fg='#fdc703',
    activeforeground='green',
    command=equal,
    )
button_Equal.grid(row=5, column=0, columns=2, ipadx=95, ipady=10)        # Equals button added and grid

root.mainloop()
