import os
import win32com.client as win32
import pandas as pd
import tkinter as tk
from tkinter import filedialog

outlook = win32.Dispatch("Outlook.Application")
ruta_base = r"C:\Users\dapache\OneDrive - NUEVA EPS\Escritorio\RPQR"

def enviar_correo(destinatario, asunto, cuerpo, adjunto):
    mail = outlook.CreateItem(0)
    mail.To = destinatario
    mail.Subject = asunto
    mail.Body = cuerpo

    # Construir la ruta completa del archivo
    ruta_completa = os.path.join(ruta_base, adjunto)

    # Adjuntar archivo si existe
    if os.path.exists(ruta_completa):
        mail.Attachments.Add(ruta_completa)
    else:
        print(f"No se pudo encontrar el archivo: {ruta_completa}")

    mail.Send()

def abrir_seleccionador_archivo():
    ruta_archivo = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Archivos CSV", "*.csv")])
    if ruta_archivo:
        df = pd.read_csv(ruta_archivo)
        for index, fila in df.iterrows():
            destinatario = fila['Correo Electronico']
            asunto = 'Adjunto: {}'.format(fila['Nombre Archivo'])
            cuerpo = 'Adjunto: {}\n\nEste es un mensaje de prueba.'.format(fila['Nombre Archivo'])
            adjunto = fila['Adjunto']

            # Enviar el correo
            enviar_correo(destinatario, asunto, cuerpo, adjunto)

# Crear la interfaz gráfica
ventana = tk.Tk()
ventana.title("Envío de Correos")

# Botón para abrir el seleccionador de archivos
boton_seleccionar = tk.Button(ventana, text="Seleccionar Archivo CSV", command=abrir_seleccionador_archivo)
boton_seleccionar.pack(pady=20)

# Iniciar el bucle de eventos de la interfaz gráfica
ventana.mainloop()
