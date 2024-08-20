import tkinter as tk
from tkinter import filedialog, messagebox
from avaliable_mouse import mantener_disponible
import os


respuestas_path = ""

def obtener_ruta_absoluta(*relativas):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), *relativas))

ventana = tk.Tk()

icono_path = obtener_ruta_absoluta("icono.ico")
imagen_path = obtener_ruta_absoluta("imagen.png")

if os.path.exists(imagen_path):
    # Cargar y ajustar la imagen
    imagen = tk.PhotoImage(file=imagen_path)
    imagen = imagen.subsample(3, 3)
else:
    messagebox.showerror("Error", "La imagen no se encuentra en la ruta especificada.")

icono_path = obtener_ruta_absoluta("icono.ico")
imagen_path = obtener_ruta_absoluta("imagen.png")

# Verificar la existencia de la imagen
if os.path.exists(imagen_path):
    # Cargar y ajustar la imagen
    imagen = tk.PhotoImage(file=imagen_path)
    imagen = imagen.subsample(3, 3)
else:
    messagebox.showerror("Error", "La imagen no se encuentra en la ruta especificada.")

imagen_label = tk.Label(ventana, image=imagen, bg="#002633")
imagen_label.image = imagen
imagen_label.pack(pady=1, padx=1, side="top", fill="both")

ventana.title("Disponible") 
ventana.configure(bg="#002633")
ventana.geometry("250x300-100-50")
ventana.maxsize(300, 500)
ventana.minsize(250, 300)
ventana.iconbitmap(icono_path)

encabezado_frame = tk.Frame(ventana, bg="#001a21", height=10)
encabezado_frame.pack(side="right", fill="both")


btn_activar = tk.Button(ventana, text="Activar", command=mantener_disponible, width=10, bg="#00526c", fg="white", relief="flat")
btn_activar.pack(pady=1, padx=20, side=None, fill="both")

def cerrar_ventana():
    resultado = messagebox.askokcancel("Salir", "¿Estás seguro que quieres salir?")
    if resultado:
        ventana.destroy()

btn_salir = tk.Button(ventana, text="Salir", command=cerrar_ventana, width=10, bg="#f44336", fg="white", relief="flat")
btn_salir.pack(pady=25, padx=90, side=None, fill="both")


etiqueta = tk.Label(ventana, text="Beta 1.0.0", width=50, border=10, bg="#002633", fg="white", relief="flat", justify="center")
etiqueta.pack(pady=1, padx=1, side="right", fill="both")

ventana.mainloop()