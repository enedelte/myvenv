import tkinter as tk
from tkinter import filedialog, messagebox
import os
from docx2pdf import convert
import win32com.client as win32
import pandas as pd
import sys 
from test_functions import enviar_correo_desde_alias, enviar_correos_desde_csv, seleccionar_archivo_csv
from test_convertpdf import seleccionar_rutas

#Crear la interfaz gráfica
ventana = tk.Tk()
# Configurar el fondo verde marino
ventana.configure(bg="#002633")  # Código de color para verde marino oscuro
# Configurar el tamaño ventana
ventana.geometry("400x400")
ventana.title("Enviar Correos Automáticos")
# Configurar el encabezado verde marino oscuro
encabezado_frame = tk.Frame(ventana, bg="#001a21", height=40)
encabezado_frame.pack(side="top", fill="x")

#Imagen NEPS
imagen_path = "imagen.png"  # Reemplaza con la ruta correcta de tu imagen
if os.path.exists(imagen_path):
    imagen = tk.PhotoImage(file=imagen_path)

# Ajustar el tamaño de la imagen (se puede ajustar el subsample según sea necesario)
    imagen = imagen.subsample(1, 1)
    imagen_label = tk.Label(ventana, image=imagen, bg="#002633")
    imagen_label.image = imagen  # ¡Importante para evitar que la imagen se elimine por el recolector de basura!
    imagen_label.pack(pady=1)

# Botón para seleccionar documentos a convertir a PDF
btn_seleccionar_word = tk.Button(ventana, text='Imprimir mis pdf', command=seleccionar_rutas, width=50, bg="#00526c", fg="white", relief="flat")
btn_seleccionar_word.pack(pady=5)
# Botón para seleccionar el archivo CSV
btn_seleccionar_csv = tk.Button(ventana, text="Enviar mis correos", command=seleccionar_archivo_csv, width=50, bg="#00526c", fg="white", relief="flat")
btn_seleccionar_csv.pack(pady=5)

btn_recuperar_email = tk.Button(ventana, text="Imprimir mis correos", width=50, bg="#00526c", fg="white", relief="flat")
btn_recuperar_email.pack(pady=5)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()