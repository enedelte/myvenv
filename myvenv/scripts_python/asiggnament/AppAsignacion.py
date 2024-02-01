import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from asiggnament import consulta_asignacion, mostrar_ventana


#rutas imagenes
def obtener_ruta_absoluta(*relativas):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), *relativas))

# Crear la interfaz gráfica
ventana_ppl = tk.Tk()

# Rutas relativas a los recursos (icono e imagen)
icono_path = obtener_ruta_absoluta("icono.ico")
imagen_path = obtener_ruta_absoluta("imagen.png")
version = "V.1.0.4"
# Verificar la existencia de la imagen
if os.path.exists(imagen_path):
    # Cargar y ajustar la imagen
    imagen = tk.PhotoImage(file=imagen_path)
    imagen = imagen.subsample(2, 2)
    # Crear la etiqueta para la imagen
    imagen_label = tk.Label(ventana_ppl, image=imagen, bg="#002633")
    imagen_label.image = imagen
    imagen_label.pack(pady=1, padx=1, side="top", fill="both")

ventana_ppl.title("DevGOPS")#nombre ventana
ventana_ppl.configure(bg="#002633") # Código de color para verde marino oscuro
ventana_ppl.geometry("250x300-100-50")# Configurar el tamaño ventana
ventana_ppl.maxsize(250, 300)
ventana_ppl.minsize(250, 300)
ventana_ppl.iconbitmap(icono_path)

# Configurar el encabezado verde marino oscuro
encabezado_frame = tk.Frame(ventana_ppl, bg="#001a21", height=10)
encabezado_frame.pack(side="right", fill="both")

# Botón para seleccionar documentos a convertir a PDF
# def boton_seleccionar_word():
#     btn_seleccionar_word = tk.Button(ventana, text='Imprimir mis pdf', command=seleccionar_rutas, width=10, bg="#00526c", fg="white", relief="flat")
#     btn_seleccionar_word.pack(pady=1, padx=20, side=None, fill="both")

# boton_seleccionar_word()

# Botón para crar archivo CSV
def actualizar_asignacion():
    btn_actualizar_asignacion = tk.Button(ventana_ppl, text="Actualizar consulta", command=consulta_asignacion, width=10, bg="#00526c", fg="white", relief="flat")
    btn_actualizar_asignacion.pack(pady=1, padx=20, side=None, fill="both")

actualizar_asignacion()


# Botón Salir
def cerrar_ventana():
    resultado = messagebox.askokcancel("Salir", "¿Estás seguro que quieres salir?")
    if resultado:
        ventana_ppl.destroy()

btn_salir = tk.Button(ventana_ppl, text= "Salir", command=cerrar_ventana, width=10, bg="#f44336", fg="white", relief="flat" )
btn_salir.pack(pady=20, padx=90, side=None, fill="both")
#etiqueta versión
etiqueta = tk.Label(ventana_ppl, text=version, width=50, border=10, bg="#002633", fg="white", relief="flat", justify="center")
etiqueta.pack(pady=1, padx=1, side="right", fill="both")

# Iniciar el bucle principal de la interfaz gráfica
ventana_ppl.mainloop()

