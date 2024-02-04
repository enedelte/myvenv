from docx import Document
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk 
import os
import datetime
from assignment import consulta_asignacion

def obtener_ruta_absoluta(*relativas):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), *relativas))

proforma = obtener_ruta_absoluta("proforma.docx")

def crear_carta(proforma, dataframe):
    if os.path.exists(proforma):
        # Crea un nuevo documento Word
        carta = Document(proforma)

        # Itera sobre las filas del DataFrame
        for index, row in dataframe.iterrows():
            # Llama a la función consulta_asignacion para obtener la información por fila
            info_asignacion = consulta_asignacion(row['columna_de_referencia'])
            
            # Agrega la información al documento
            carta.add_paragraph(f"Nombre: {info_asignacion['Nombre']}, Edad: {info_asignacion['Edad']}")
        
        # Guarda el documento con un nombre único (puedes ajustar según tus necesidades)
        nombre_documento = f"VO-DGO-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}.docx"
        ruta_documento = obtener_ruta_absoluta(nombre_documento)
        carta.save(ruta_documento)

        # Muestra un mensaje de éxito
        messagebox.showinfo('Se ha creado la carta de manera exitosa', f"Documento guardado en: {ruta_documento}")
    else:
        messagebox.showerror("Error", "No se encuentra el documento en la ruta especificada.")
