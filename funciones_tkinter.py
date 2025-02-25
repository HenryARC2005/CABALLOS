import tkinter as tk
from tkinter import messagebox


def text_info(mensaje):
    root=tk.Tk()

    root.withdraw()

    messagebox.showinfo('Mensaje', mensaje)

    root.destroy()


def confirmacion(mensaje):
    root=tk.Tk()

    root.withdraw()

    respuesta=messagebox.askyesno("Confirmacion", mensaje)
    root.destroy()
    return respuesta
    


def text_error(mensaje):
    root=tk.Tk()

    root.withdraw()

    messagebox.showerror('Error', mensaje)

    root.destroy()