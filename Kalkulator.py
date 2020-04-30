from tkinter import *
from tkinter import messagebox

vnos=""
window = Tk()
window.title("Kalkulator")
def setTextInput(text):
    racun.insert(0, text)

def setTextInput2(text):
    racun2.insert(0, text)

def vrstica2():
    Btn1.config(text="1", width=5, height=2, command=lambda: setTextInput2(1))
    Btn2.config(text="2", width=5, height=2, command=lambda: setTextInput2(2))
    Btn3.config(text="3", width=5, height=2, command=lambda: setTextInput2(3))

    Btn4.config(text="4", width=5, height=2, command=lambda: setTextInput2(4))
    Btn5.config(text="5", width=5, height=2, command=lambda: setTextInput2(5))
    Btn6.config(text="6", width=5, height=2, command=lambda: setTextInput2(6))

    Btn7.config(text="7", width=5, height=2, command=lambda: setTextInput2(7))
    Btn8.config(text="8", width=5, height=2, command=lambda: setTextInput2(8))
    Btn9.config(text="9", width=5, height=2, command=lambda: setTextInput2(9))

    BtnC.config(text="Clear", width=5, height=2, command=lambda: setTextInput2(""))
    Btn0.config(text="0", width=5, height=2, command=lambda: setTextInput2(0))
    BtnL.config(text="St 1", width=5, height=2, command=lambda: vrstica1())

def vrstica1():
    Btn1.config(text="1", width=5, height=2, command=lambda: setTextInput(1))
    Btn2.config(text="2", width=5, height=2, command=lambda: setTextInput(2))
    Btn3.config(text="3", width=5, height=2, command=lambda: setTextInput(3))

    Btn4.config(text="4", width=5, height=2, command=lambda: setTextInput(4))
    Btn5.config(text="5", width=5, height=2, command=lambda: setTextInput(5))
    Btn6.config(text="6", width=5, height=2, command=lambda: setTextInput(6))

    Btn7.config(text="7", width=5, height=2, command=lambda: setTextInput(7))
    Btn8.config(text="8", width=5, height=2, command=lambda: setTextInput(8))
    Btn9.config(text="9", width=5, height=2, command=lambda: setTextInput(9))

    BtnC.config(text="Clear", width=5, height=2, command=lambda: setTextInput(""))
    Btn0.config(text="0", width=5, height=2, command=lambda: setTextInput(0))
    BtnL.config(text="St 2", width=5, height=2, command=lambda: vrstica2())



racun = Entry(window, width=30, bd=3)
racun.grid(row=0, column=0, columnspan=4)
racun2 = Entry(window, width=30, bd=3)
racun2.grid(row=1, column=0, columnspan=4)


Btn1 = Button(window, text="1", width=5, height=2, command=lambda: setTextInput(1), bd=5)
Btn1.grid(row=2, column=0)
Btn2 = Button(window, text="2", width=5, height=2, command=lambda: setTextInput(2), bd=5)
Btn2.grid(row=2, column=1)
Btn3 = Button(window, text="3", width=5, height=2, command=lambda: setTextInput(3), bd=5)
Btn3.grid(row=2, column=2)

Btn4 = Button(window, text="4", width=5, height=2, command=lambda: setTextInput(4), bd=5)
Btn4.grid(row=3, column=0)
Btn5 = Button(window, text="5", width=5, height=2, command=lambda: setTextInput(5), bd=5)
Btn5.grid(row=3, column=1)
Btn6 = Button(window, text="6", width=5, height=2, command=lambda: setTextInput(6), bd=5)
Btn6.grid(row=3, column=2)

Btn7 = Button(window, text="7", width=5, height=2, command=lambda: setTextInput(7), bd=5)
Btn7.grid(row=4, column=0)
Btn8 = Button(window, text="8", width=5, height=2, command=lambda: setTextInput(8), bd=5)
Btn8.grid(row=4, column=1)
Btn9 = Button(window, text="9", width=5, height=2, command=lambda: setTextInput(9), bd=5)
Btn9.grid(row=4, column=2)

BtnC = Button(window, text="Clear", width=5, height=2, command=lambda: setTextInput(""), bd=5)
BtnC.grid(row=5, column=0)
Btn0 = Button(window, text="0", width=5, height=2, command=lambda: setTextInput(0), bd=5)
Btn0.grid(row=5, column=1)
BtnL = Button(window, text="St 2", width=5, height=2, command=lambda: vrstica2(), bd=5)
BtnL.grid(row=5, column=2)

def sestej():
    x = racun.get()
    y = racun2.get()
    if not x or not y:
        messagebox.showerror("Napaka!", "Napaka")
        return
    if(x.isdigit() and y.isdigit()):
        messagebox.showinfo("Izračun", int(x)+int(y))
    return

def odstej():
    x = racun.get()
    y = racun2.get()
    if not x or not y:
        messagebox.showerror("Napaka!", "Napaka")
        return
    if(x.isdigit() and y.isdigit()):
        messagebox.showinfo("Izračun", int(x)-int(y))
    return

def krat():
    x = racun.get()
    y = racun2.get()
    if not x or not y:
        messagebox.showerror("Napaka!", "Napaka")
        return
    if(x.isdigit() and y.isdigit()):
        messagebox.showinfo("Izračun", int(x)*int(y))
    return

def deli():
    x = racun.get()
    y = racun2.get()
    if not x or not y:
        messagebox.showerror("Napaka!", "Napaka")
        return
    if(x.isdigit() and y.isdigit()):
        messagebox.showinfo("Izračun", int(x)/int(y))
    return

plusBtn = Button(window, text="+",  width=5, height=2, command=lambda: sestej(), bd=3, bg="red")
plusBtn.grid(row=2, column=3)
minusBtn = Button(window, text="-",  width=5, height=2, command=lambda: odstej(), bd=3, bg="red")
minusBtn.grid(row=3, column=3)
kratBtn = Button(window, text="*", width=5, height=2, command=lambda: krat(), bd=3, bg="red")
kratBtn.grid(row=4, column= 3)
deliBtn = Button(window, text="/", width=5, height=2, command=lambda: deli(), bd=3, bg="red")
deliBtn.grid(row=5, column=3)

window.mainloop()