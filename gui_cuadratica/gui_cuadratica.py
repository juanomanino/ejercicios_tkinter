from cmath import sqrt
from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter import messagebox
import math

def calcular():
    d=int(b.get())**2-4*int(a.get())*int(c.get())
    if d>0:
        x1=(-int(b.get())+math.sqrt(d))/(2*int(a.get()))
        x2=(-int(b.get())-math.sqrt(d))/(2*int(a.get()))
        t_exit.insert(INSERT, "x1="+str(x1)+ "\nx2="+str(x2)+ "\n Son dos raíces diferentes")
    elif d==0:  
        x1=-int(b.get())/2*int(a.get())
        t_exit.insert(INSERT, "x1="+str(x1)+"\nx1 y x2 son iguales \n Son dos raíces reales diferentes" )
    else:
        t_exit.insert(INSERT,"Es parte de las raíces imaginarias o complejas.\n No tiene solución en los números reales" )

def borrar():
    a.set("")
    b.set("")
    c.set("")
    t_exit.delete("1.0", "end")

def exit():
    ventana_main.destroy()



ventana_main=Tk()
ventana_main.title("Calculadora de ecuación cuadrática")
ventana_main.geometry("1000x500")
ventana_main.resizable(0,0)

ventana_main.iconphoto(False, tk.PhotoImage(file='gui_cuadratica/img/kuku.png'))


ventana_main.config(bg="black")

# -------------------
# variables globales
# -------------------
a = StringVar()
b = StringVar()
c = StringVar()
d = IntVar()
x1= IntVar()
x2= IntVar()

# frame left
frame_left=Frame(ventana_main)
frame_left.config(bg="purple", width=320,height=480)
frame_left.place(x=10, y=10)

titulol=Label(frame_left, text="Botones")
titulol.config(bg="purple", fg="red", font=("Ubuntu", 16))
titulol.place(x=110,y=30)

bt_cal=PhotoImage(file="gui_cuadratica/img/calculator.png")
bt_calc=Button(frame_left, image=bt_cal, width=120, height=110, command=calcular)
bt_calc.place(x=90, y=80)

bt_borr=PhotoImage(file="gui_cuadratica/img/board.png")
bt_borrar=Button(frame_left, image=bt_borr, width=120, height=110, command=borrar)
bt_borrar.place(x=90, y= 210)

bt_ex=PhotoImage(file="gui_cuadratica/img/exit.png")
bt_exit=Button(frame_left, image=bt_ex, width=120, height=110, command=exit)
bt_exit.place(x=90, y=340)

# frame middle
frame_middle=Frame(ventana_main)
frame_middle.config(bg="ivory2", width=340, height=480)
frame_middle.place(x=330, y=10)

titulo=Label(frame_middle, text="Ecuaciones Cuadráticas")
titulo.config(bg="ivory2", fg="blue", font=("Ubuntu", 16))
titulo.place(x=50,y=30)

logo=PhotoImage(file="gui_cuadratica/img/ec.png")
etiq_logo=Label(frame_middle, image=logo)
etiq_logo.place(x=30, y=410)


etiq_a=Label(frame_middle, text="a=")
etiq_a.config(bg="white", fg="black", font=("Ubuntu", 16), anchor=CENTER)
etiq_a.place(x=80, y=100)

entry_a=Entry(frame_middle, width=6, textvariable=a)
entry_a.config(font=("Ubuntu", 16), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=120,y=100)

etiq_b=Label(frame_middle, text="b=")
etiq_b.config(bg="white", fg="black", font=("Ubuntu", 16), anchor=CENTER)
etiq_b.place(x=80, y=200)

entry_b=Entry(frame_middle, width=6, textvariable=b)
entry_b.config(font=("Ubuntu", 16), justify=CENTER)
entry_b.focus_set()
entry_b.place(x=120,y=200)

etiq_c=Label(frame_middle, text="c=")
etiq_c.config(bg="white", fg="black", font=("Ubuntu", 16), anchor=CENTER)
etiq_c.place(x=80, y=300)

entry_c=Entry(frame_middle, width=6, textvariable=c)
entry_c.config(font=("Ubuntu", 16), justify=CENTER)
entry_c.focus_set()
entry_c.place(x=120,y=300)

# frame right
frame_right=Frame(ventana_main)
frame_right.config(bg="PaleGreen1", width=320, height=480)
frame_right.place(x=670, y=10)

t_exit=Text(frame_right, width=25, height=18)
t_exit.config(bg="SkyBlue1", fg="black", font=("Ubuntu", 16))
t_exit.place(x=8, y=15)

ventana_main.mainloop()
