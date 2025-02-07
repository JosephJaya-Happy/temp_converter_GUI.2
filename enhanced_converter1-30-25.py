import tkinter as ttk

Hoi = ttk.Tk()
Hoi.title('anhanced converter')
Hoi.geometry('300x300')

fa = ttk.Label(Hoi, text='celsius')
fa.place(x=200, y=50)
fb = ttk.Label(Hoi, text='farenheit')
fb.place(x=200, y=200)

a = ttk.StringVar()
e1 = ttk.Entry(Hoi, textvar = a)
e1.place(x=50, y=50)


b = ttk.StringVar()
e2 = ttk.Entry(Hoi, textvar = b)
e2.place(x=50, y=200)

c = ttk.StringVar(value='C -> F')
options = ['C -> F','F -> C']

def lablechange(*arg):
    if c.get() == 'C -> F':
        fa.config(text='celsius')
        fb.config(text='farenheit')
    elif c.get() == 'F -> C':
        fa.config(text='farenheit')
        fb.config(text='celsius')

op1 = ttk.OptionMenu(Hoi,c, *options, command= lablechange)
op1.place(x=50, y=140)

def convertvalue():
    try:
        value = float(a.get())
        if c.get() == 'C -> F':
            ans = value*1.8+32
            b.set(f'{ans:.2F}')

        elif c.get() == 'F -> C':
            ans = (value-32)/1.8
            b.set(f'{ans:.2F}')

    except:
        b.set("noooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")

b1 = ttk.Button(Hoi, text= "convet", command=convertvalue)
b1.place(x=50, y=100)

Hoi.mainloop()