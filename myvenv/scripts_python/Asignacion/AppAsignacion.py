import tkinter as tk
from tkinter import filedialog, messagebox, ttk, Label, Listbox
import os
from assignment import cargar_y_consultar_asignacion
from funciones import main as main_func
from creador_cartas import crear_carta

# Crear la interfaz gráfica
ventana_ppl = tk.Tk()

#rutas imagenes
def obtener_ruta_absoluta(*relativas):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), *relativas))

# Rutas relativas a los recursos (icono e imagen)
icono_path = obtener_ruta_absoluta("icono.ico")
imagen_path = obtener_ruta_absoluta("imagen.png")

# Verificar la existencia de la imagen
if os.path.exists(imagen_path):
    # Cargar y ajustar la imagen
    imagen = tk.PhotoImage(file=imagen_path)
    imagen = imagen.subsample(3, 3)
    # Crear la etiqueta para la imagen
    imagen_label = tk.Label(ventana_ppl, image=imagen, bg="#002633")
    imagen_label.image = imagen
    imagen_label.pack(pady=1, padx=1, side="top", fill="both")

ventana_ppl.title("DevGOPS")#nombre ventana
ventana_ppl.configure(bg="#002633") # Código de color para verde marino oscuro
ventana_ppl.geometry("600x600-100-50")# Configurar el tamaño ventana
ventana_ppl.maxsize(600, 600)
ventana_ppl.minsize(600, 600)
ventana_ppl.iconbitmap(icono_path)

# Configurar el encabezado verde marino oscuro
encabezado_frame = tk.Frame(ventana_ppl, bg="#001a21", height=10)
encabezado_frame.pack(side="right", fill="both")


# Botón para crar archivo CSV
def actualizar_asignacion():
    btn_actualizar_asignacion = tk.Button(ventana_ppl, text="Actualizar Asignación", command=cargar_y_consultar_asignacion, width=20, bg="#00526c", fg="white", relief="flat")
    btn_actualizar_asignacion.pack(pady=1, padx=1, side=None, fill="both")
    btn_actualizar_asignacion.place(x=40, y=160)
actualizar_asignacion()

def enviar_correos():

    btn_enviar_email = tk.Button(ventana_ppl, text="Enviar Correos", command=main_func, width=20, bg="#00526c", fg="white", relief="flat")
    btn_enviar_email.pack(pady=10, padx=20, side=None, fill="both")
    btn_enviar_email.place(x=40, y=220)

enviar_correos()

def crear_carta():

    btn_crear_carta = tk.Button(ventana_ppl, text="Crear Respuesta", command=None, width=20, bg="#00526c", fg="white", relief="flat")
    btn_crear_carta.pack(pady=10, padx=20, side=None, fill="both")
    btn_crear_carta.place(x=40, y=190)

crear_carta()

# Botón Salir
def cerrar_ventana():
    resultado = messagebox.askokcancel("Salir", "¿Estás seguro que quieres salir?")
    if resultado:
        ventana_ppl.destroy()



lbl = Label(ventana_ppl, text="Casos Asignados")
listbox = Listbox(ventana_ppl)
listbox.insert(1, cargar_y_consultar_asignacion)
lbl.pack(pady=50, padx=30, side='right', fill="both")
listbox.pack()



def salir():
    btn_salir = tk.Button(ventana_ppl, text= "Salir", command=cerrar_ventana, width=10, bg="#f44336", fg="white", relief="flat" )
    btn_salir.pack(pady=1, padx=1, side=None, fill="both")
    btn_salir.place(x=40, y=500)
    
salir()

#etiqueta versión
def version():
    version = "V.1.0.6"
    etiqueta = tk.Label(ventana_ppl, text=version, width=10, border=10, bg="#002633", fg="white", relief="flat", justify="center")
    etiqueta.pack(pady=1, padx=1, side="right", fill="both")
    etiqueta.place(x=250, y=550)

version()

# Iniciar el bucle principal de la interfaz gráfica
ventana_ppl.mainloop()

