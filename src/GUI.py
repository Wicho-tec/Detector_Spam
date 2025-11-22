import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Aviso", "Botón presionado")

#GUI
root = tk.Tk()
root.title("Detector de Spam")

label = tk.Label(root, text = "Hola mundo") #Agregar widgets de texto
label.pack(pady = 10)

button = tk.Button(root, text="Haz clic aquí", command = mostrar_mensaje) #Agregar botones
button.pack(pady = 10)

# Finalizar GUI
root.mainloop()