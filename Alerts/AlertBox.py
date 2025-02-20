import tkinter as tk
from tkinter import ttk

def Show_popup(message):
    #creamos la pagina
    popup=tk.Toplevel()
    popup.title("Messaje")
    popup.geometry("400x200")
    popup.configure(bg="black")
    #le indicamos donde se encuentra el elemento (popup)
    label=ttk.Label(popup,text=message,style="TLabel",wraplength=280)   
    label.pack(pady=10)

    close_button = ttk.Button(popup, text="Cerrar", command=popup.destroy)
    close_button.pack(pady=10)