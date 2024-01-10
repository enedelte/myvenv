import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from docx2pdf import convert
import win32com.client as win32
import pandas as pd
import sys 
from functions import enviar_correo_desde_alias, enviar_correos_desde_csv, seleccionar_archivo_csv, main
from convertpdf import seleccionar_rutas

#Crear la interfaz gráfica
ventana = tk.Tk()
icono = "C:\\Users\\dapache\\python_scripts\\myvenv\\scripts_python\\RPA_Correos\\test\\icono.ico"
version = "V.1.0.1"
imagen_path = "C:\\Users\\dapache\\python_scripts\\myvenv\\scripts_python\\RPA_Correos\\test\\imagen.png"  #Imagen NEPS

if os.path.exists(imagen_path):
    imagen = tk.PhotoImage(file=imagen_path)

# Ajustar el tamaño de la imagen (se puede ajustar el subsample según sea necesario)
    imagen = imagen.subsample(2, 2)
    imagen_label = tk.Label(ventana, image=imagen, bg="#002633")
    imagen_label.image = imagen  # ¡Importante para evitar que la imagen se elimine por el recolector de basura!
    imagen_label.pack(pady=1, padx=1, side="top", fill="both")


ventana.title("DevGOPS")#nombre ventana
ventana.configure(bg="#002633") # Código de color para verde marino oscuro
ventana.geometry("250x300-100-50")# Configurar el tamaño ventana
ventana.maxsize(250, 300)
ventana.minsize(250, 300)
ventana.iconbitmap(icono)

# Configurar el encabezado verde marino oscuro
encabezado_frame = tk.Frame(ventana, bg="#001a21", height=10)
encabezado_frame.pack(side="right", fill="both")
# Botón para seleccionar documentos a convertir a PDF
btn_seleccionar_word = tk.Button(ventana, text='Imprimir mis pdf', command=seleccionar_rutas, width=10, bg="#00526c", fg="white", relief="flat")
btn_seleccionar_word.pack(pady=1, padx=20, side=None, fill="both")
# Botón para crar archivo CSV
btn_recuperar_email = tk.Button(ventana, text="Organizar mis correos", command=main, width=10, bg="#00526c", fg="white", relief="flat")
btn_recuperar_email.pack(pady=1, padx=20, side=None, fill="both")

# Botón para seleccionar el archivo CSV
btn_seleccionar_csv = tk.Button(ventana, text="Enviar mis correos", command=seleccionar_archivo_csv, width=10, bg="#00526c", fg="white", relief="flat")
btn_seleccionar_csv.pack(pady=1, padx=20, side=None, fill="both")

# Botón Salir
def cerrar_ventana():
    resultado = messagebox.askokcancel("Salir", "¿Estás seguro que quieres salir?")
    if resultado:
        ventana.destroy()

btn_salir = tk.Button(ventana, text= "Salir", command=cerrar_ventana, width=10, bg="#f44336", fg="white", relief="flat" )
btn_salir.pack(pady=20, padx=90, side=None, fill="both")
#etiqueta versión
etiqueta = tk.Label(ventana, text=version, width=50, border=10, bg="#002633", fg="white", relief="flat", justify="center")
etiqueta.pack(pady=1, padx=1, side="right", fill="both")

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
