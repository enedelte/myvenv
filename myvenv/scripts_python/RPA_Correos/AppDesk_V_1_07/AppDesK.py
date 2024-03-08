import tkinter as tk
from tkinter import filedialog, messagebox
import os
from docx2pdf import convert
import win32com.client as win32
import pandas as pd
from funciones import main as main_func
#from convertpdf import seleccionar_rutas
from enviados import main

# Ruta global para acceder desde funciones
respuestas_path = ""

def obtener_ruta_absoluta(*relativas):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), *relativas))

# Crear la interfaz gráfica
ventana = tk.Tk()

# Rutas relativas a los recursos (icono e imagen)
icono_path = obtener_ruta_absoluta("icono.ico")
imagen_path = obtener_ruta_absoluta("imagen.png")

# Verificar la existencia de la imagen
if os.path.exists(imagen_path):
    # Cargar y ajustar la imagen
    imagen = tk.PhotoImage(file=imagen_path)
    imagen = imagen.subsample(3, 3)
else:
    messagebox.showerror("Error", "La imagen no se encuentra en la ruta especificada.")

# Crear la etiqueta para la imagen
imagen_label = tk.Label(ventana, image=imagen, bg="#002633")
imagen_label.image = imagen
imagen_label.pack(pady=1, padx=1, side="top", fill="both")

ventana.title("DevGOPS")  # nombre ventana
ventana.configure(bg="#002633")  # Código de color para verde marino oscuro
ventana.geometry("250x300-100-50")  # Configurar el tamaño ventana
ventana.maxsize(250, 300)
ventana.minsize(250, 300)
ventana.iconbitmap(icono_path)

# Configurar el encabezado verde marino oscuro
encabezado_frame = tk.Frame(ventana, bg="#001a21", height=10)
encabezado_frame.pack(side="right", fill="both")


# Botón Conversion PDF
# btn_convertir_pdf = tk.Button(ventana, text="Convertir PDF", command=seleccionar_rutas, width=10,
#                                 bg="#00526c", fg="white", relief="flat")
# btn_convertir_pdf.pack(pady=1, padx=20, side=None, fill="both")

# Botón envio correos
btn_enviar_email = tk.Button(ventana, text="Enviar Correos", command=main_func, width=10,
                                bg="#00526c", fg="white", relief="flat")
btn_enviar_email.pack(pady=1, padx=20, side=None, fill="both")

# Bóton guardar enviados
btn_enviar_email = tk.Button(ventana, text="Guardar Correos Enviados", command=main, width=10,
                                bg="#00526c", fg="white", relief="flat")
btn_enviar_email.pack(pady=1, padx=20, side=None, fill="both")

def cerrar_ventana():
    resultado = messagebox.askokcancel("Salir", "¿Estás seguro que quieres salir?")
    if resultado:
        ventana.destroy()

btn_salir = tk.Button(ventana, text="Salir", command=cerrar_ventana, width=10, bg="#f44336", fg="white", relief="flat")
btn_salir.pack(pady=25, padx=90, side=None, fill="both")

# etiqueta versión
etiqueta = tk.Label(ventana, text="Versión 1.0.7", width=50, border=10, bg="#002633", fg="white", relief="flat",
                    justify="center")
etiqueta.pack(pady=1, padx=1, side="right", fill="both")

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
