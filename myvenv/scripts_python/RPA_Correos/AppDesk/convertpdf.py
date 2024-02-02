import os
from docx2pdf import convert
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox

def convertir_word_a_pdf(carpeta_origen, carpeta_destino):
    # Obtener las rutas de los archivos DOCX en la carpeta de origen
    rutas_word = [os.path.join(carpeta_origen, archivo) 
                  for archivo in os.listdir(carpeta_origen) 
                  if archivo.lower().endswith('.docx')
                  and not archivo.startswith("~$")]

    if not rutas_word:
        messagebox.showwarning("Advertencia", f"No se encontraron archivos en la carpeta de origen: {carpeta_origen}.")
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

def seleccionar_rutas():
    # Crear la ventana principal de Tkinter
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    # Solicitar la carpeta de origen donde se encuentran los archivos DOCX
    carpeta_origen = filedialog.askdirectory(title="Seleccionar carpeta de respuestas")

    if not carpeta_origen:
        messagebox.showwarning("Advertencia", "No se seleccionó la carpeta de origen.")
        return

    # Solicitar la carpeta de destino para guardar los archivos PDF
    carpeta_destino = filedialog.askdirectory(title="Seleccionar carpeta de destino para respuestas en formato PDF")

    if not carpeta_destino:
        messagebox.showwarning("Advertencia", "No se seleccionó la carpeta de destino.")
        return

    try:
        # Llamar a la función para convertir los archivos DOCX a PDF
        convertir_word_a_pdf(carpeta_origen, carpeta_destino)
    except Exception as e:
        messagebox.showerror("Error general", f"Error general: {e}")
    
if __name__ == "__main__":
    # Llamar a la función que permite seleccionar las rutas
    seleccionar_rutas()
