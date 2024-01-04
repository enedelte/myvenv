from functions import enviar_correo_desde_alias, enviar_correos_desde_csv, seleccionar_archivo
import tkinter as tk
from tkinter import filedialog
import customtkinter
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Crear la interfaz gráfica
ventana = tk.Tk()

# Configurar el fondo verde marino
ventana.configure(bg="#002633")  # Código de color para verde marino oscuro

# Configurar el tamaño y los bordes redondos
ventana.geometry("400x400")
ventana.title("Enviar Correos Automáticos")

# Configurar el encabezado verde marino oscuro
encabezado_frame = tk.Frame(ventana, bg="#001a21", height=20)
encabezado_frame.pack(side="top", fill="x")

imagen_path = "imagen.png"  # Reemplaza con la ruta correcta de tu imagen
if os.path.exists(imagen_path):
    imagen = tk.PhotoImage(file=imagen_path)

# Ajustar el tamaño de la imagen (puedes cambiar los valores de subsample según sea necesario)
    imagen = imagen.subsample(3, 3)
    imagen_label = tk.Label(ventana, image=imagen, bg="#002633")
    imagen_label.image = imagen  # ¡Importante para evitar que la imagen se elimine por el recolector de basura!
    imagen_label.pack(pady=10)

# Botón para seleccionar el archivo CSV
btn_seleccionar = tk.Button(ventana, text="Ubica el archivo que vas a enviar", command=seleccionar_archivo, width=50, bg="#00526c", fg="white", relief="flat")
btn_seleccionar.pack(pady=30)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
