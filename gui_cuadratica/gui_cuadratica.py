from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter import messagebox




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

# frame left
frame_left=Frame(ventana_main)
frame_left.config(bg="purple", width=320,height=480)
frame_left.place(x=10, y=10)


# frame middle
frame_middle=Frame(ventana_main)
frame_middle.config(bg="ivory2", width=340, height=480)
frame_middle.place(x=330, y=10)

titulo=Label(frame_middle, text="Ecuaciones Cuadráticas")
titulo.config(bg="ivory2", fg="blue", font=("Ubuntu", 16))
titulo.place(x=50,y=30)

logo=PhotoImage(file="gui_cuadratica/img/ec.png")
etiq_logo=Label(frame_middle, image=logo)
etiq_logo.place(x=20, y=410)

# frame right
frame_right=Frame(ventana_main)
frame_right.config(bg="green", width=320, height=480)
frame_right.place(x=670, y=10)

ventana_main.mainloop()
