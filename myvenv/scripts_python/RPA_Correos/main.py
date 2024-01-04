from functions import enviar_correo_desde_alias, enviar_correos_desde_csv, seleccionar_archivo
import tkinter as tk
from tkinter import filedialog
import customtkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Crear la interfaz gráfica
ventana = tk.Tk()
ventana.geometry("250x250")
ventana.title("Enviar Correos Automáticos")

# Botón para seleccionar el archivo CSV
btn_seleccionar = tk.Button(ventana, text="Ubica el archivo que vas a enviar", command=seleccionar_archivo, width=30)
btn_seleccionar.pack(pady=100)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()