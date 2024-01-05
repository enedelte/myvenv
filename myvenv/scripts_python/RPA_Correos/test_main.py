import tkinter as tk
from tkinter import filedialog, messagebox
import os
from docx2pdf import convert
import win32com.client as win32
import pandas as pd
import sys

outlook = win32.Dispatch("Outlook.Application")
ruta_base = r"C:\Users\dapache\GOPS"  # Cambiar según tu directorio
alias = "respuestas.pqr@nuevaeps.com.co"

def enviar_correo_desde_alias(destinatario, asunto, cuerpo, adjunto, alias):
    mail = outlook.CreateItem(0)
    mail.SentOnBehalfOfName = alias
    mail.To = destinatario
    mail.Subject = asunto
    mail.Body = cuerpo

    ruta_completa = os.path.join(ruta_base, adjunto)

    if os.path.exists(ruta_completa):
        mail.Attachments.Add(ruta_completa)
    else:
        print(f"No se pudo encontrar el archivo: {ruta_completa}")

    mail.Send()

def enviar_correos_desde_csv(archivo_csv):
    df = pd.read_csv(archivo_csv)

    for index, fila in df.iterrows():
        destinatario = fila['Correo Electronico']
        asunto = 'RESPUESTA SOLICITUD {}'.format(fila['Nombre Archivo'])
        cuerpo = 'Reciba un cordial saludo en nombre de NUEVA EPS S.A. Agradecemos su confianza al exponernos sus inquietudes.\n\n Adjunto remitimos respuesta a su Solicitud.\n\nPorque nos interesa ofrecerle un mejor servicio, queremos que nos cuente cómo fue su experiencia con la solución de su solicitud PQRS para lo cual lo invitamos a contestar dos preguntas en el siguiente enlace https://forms.office.com/r/pJaFmjkLW1\n\n“En el presente mensaje se tuvo en cuenta la protección de datos consagrada en la Ley 1581 DE 2012. Por favor no responda a este mensaje ya que la cuenta de correo se encuentra configurada sólo para generar respuestas masivas”.\n\n PRUEBA ELECTRÓNICA: Al recibir el acuse de recibo con destino a ésta oficina, se entenderá como aceptado y tendrá recepción como documento prueba de la entrega del usuario. (Ley 527 del 18/08/1999).\n\nAtentamente,\n\nDirección de Gestión Operativa\nVicepresidencia de Operaciones\n Bogotá D.C. - Colombia\n https://www.nuevaeps.com.co/'.format(fila['Nombre Archivo'])

        enviar_correo_desde_alias(destinatario, asunto, cuerpo, adjunto, alias)

def convertir_word_a_pdf(carpeta_origen, carpeta_destino):
    # Obtener las rutas de los archivos DOCX en la carpeta de origen
    rutas_word = [os.path.join(carpeta_origen, archivo) for archivo in os.listdir(carpeta_origen) if archivo.lower().endswith('.docx')]

    if not rutas_word:
        messagebox.showwarning("Advertencia", f"No se encontraron archivos DOCX en la carpeta de origen: {carpeta_origen}.")
        return

    # Convertir los archivos DOCX a PDF en la carpeta de destino
    for word_path in rutas_word:
        try:
            # Obtener el nombre del archivo sin extensión y construir la ruta de destino para el archivo PDF
            nombre_archivo, _ = os.path.splitext(os.path.basename(word_path))
            pdf_path = os.path.join(carpeta_destino, f"{nombre_archivo}.pdf")

            # Convertir el archivo DOCX a PDF
            convert(word_path, pdf_path)
        except Exception as e:
            messagebox.showerror("Error", f"Error al convertir {word_path} a PDF: {e}")

    messagebox.showinfo("Completado", f"La conversión se ha completado. Archivos PDF guardados en: {carpeta_destino}")

def seleccionar_rutas_y_convertir():
    # Crear la ventana principal de Tkinter
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    # Solicitar la carpeta de origen donde se encuentran los archivos DOCX
    carpeta_origen = filedialog.askdirectory(title="Seleccionar carpeta de origen para archivos DOCX")

    if not carpeta_origen:
        messagebox.showwarning("Advertencia", "No se seleccionó la carpeta de origen.")
        return

    # Solicitar la carpeta de destino para guardar los archivos PDF
    carpeta_destino = filedialog.askdirectory(title="Seleccionar carpeta de destino para PDF")

    if not carpeta_destino:
        messagebox.showwarning("Advertencia", "No se seleccionó la carpeta de destino.")
        return

    try:
        # Llamar a la función para convertir los archivos DOCX a PDF
        convertir_word_a_pdf(carpeta_origen, carpeta_destino)
    except Exception as e:
        messagebox.showerror("Error general", f"Error general: {e}")

    ventana.destroy()  # Cerrar la ventana Tkinter
    sys.exit()  # Salir del script

def enviar_correos_desde_csv_seleccionar():
    archivo_csv = filedialog.askopenfilename(title="Seleccionar archivo CSV", filetypes=[("Archivos CSV", "*.csv")])
    if archivo_csv:
        enviar_correos_desde_csv(archivo_csv)
        messagebox.showinfo('Se han enviado por completo los correos relacionados')

# Crear la interfaz gráfica
ventana = tk.Tk()
ventana.title("Operaciones con Correos y Archivos")

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


# Botón para convertir archivos Word a PDF
btn_convertir_pdf = tk.Button(ventana, text="Convertir Word a PDF", command=seleccionar_rutas_y_convertir)
btn_convertir_pdf.pack(pady=10)

# Botón para enviar correos desde CSV
btn_enviar_correos = tk.Button(ventana, text="Enviar Correos Automaticamente", command=enviar_correos_desde_csv_seleccionar)
btn_enviar_correos.pack(pady=10)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
