from cProfile import label
from re import T
import tkinter
import tkinter as tk
from turtle import heading
import smtplib

def correo():
    fromaddr = tb2.get()
    toaddrs = tb1.get()
    msg = tb3.get()

    username = 'aylmao@gmail.com'
    password = 'ZaptyzuwuuwuZaptyz'

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

ventana = tk.Tk()
ventana.geometry("450x300")
lbTitulo = tkinter.Label(ventana, text="Semana 11")
lb1 = tkinter.Label(ventana, text="Enviar a:")
lb2 = tkinter.Label(ventana, text="Usuario:")
tb1 = tkinter.Entry(ventana)
tb2 = tkinter.Entry(ventana)
tb3 = tkinter.Entry(ventana)
btn1 = tkinter.Button(ventana, text="Enviar", width=4, height=2, command=correo)

lbTitulo.place(relx=0, rely=0)
lb1.place(relx=0.3, rely=0.3)
lb2.place(relx=0.3, rely=0.5)
tb1.place(relx=0.5, rely=0.3)
tb2.place(relx=0.5, rely=0.5)
tb3.place(relx=00, rely=0.7, relheight=0.3, relwidth=1)
btn1.place(relx=0.2, rely=0.9, relwidth=0.9)