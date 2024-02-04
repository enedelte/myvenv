from docx import Document
from tkinter import filedialog, messagebox
import os
from assignment import cargar_y_consultar_asignacion  # Asegúrate de que el nombre del módulo sea correcto
import pandas as pd

def obtener_ruta_absoluta(*relativas):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), *relativas))

def crear_carta(proforma, dataframe):
    if os.path.exists(proforma) and dataframe is not None:
        # Crea un nuevo documento Word
        carta = Document(proforma)

        # Itera sobre las filas del DataFrame
        for index, row in dataframe.iterrows():
            # Asegúrate de que 'columna_de_referencia' sea una columna válida en tu DataFrame
            info_asignacion = cargar_y_consultar_asignacion(row['columna_de_referencia'])
            
            # Agrega la información al documento
            carta.add_paragraph(f"Nombre: {info_asignacion['Nombre']}, Edad: {info_asignacion['Edad']}")

        # Solicita al usuario la ubicación y el nombre del archivo
        ruta_documento = filedialog.asksaveasfilename(
            defaultextension=".docx",
            filetypes=[("Documentos de Word", "*.docx"), ("Todos los archivos", "*.*")],
            title="Guardar como"
        )

        # Verifica si el usuario canceló la operación
        if not ruta_documento:
            messagebox.showinfo("Cancelado", "No se seleccionó ningún archivo. La operación ha sido cancelada.")
            return None

        # Guarda el documento en la ubicación seleccionada por el usuario
        carta.save(ruta_documento)

        # Muestra un mensaje de éxito con la ruta del documento
        mensaje = f"Documento guardado en: {ruta_documento}"
        messagebox.showinfo('Se ha creado la carta de manera exitosa', mensaje)
        return ruta_documento
    else:
        messagebox.showerror("Error", "No se encuentra el documento en la ruta especificada o DataFrame es nulo.")
        return None

# Ejemplo de llamada con DataFrame válido
# ruta_creada = crear_carta(proforma, dataframe=tu_data_frame)
# if ruta_creada:
#     print(f"Documento creado en: {ruta_creada}")
