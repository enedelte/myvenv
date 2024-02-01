import pandas as pd
import pyarrow
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def cargar_archivo():
    # Abre el cuadro de diálogo para seleccionar un archivo
    ruta_archivo = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Archivos CSV", "*.csv")])
    if not ruta_archivo:
        messagebox.showwarning("Advertencia", "No se seleccionó la ubicación para guardar el archivo CSV.")
        return
   
    if ruta_archivo:
        reporte = pd.read_csv(ruta_archivo, header=0, index_col=0, sep='\t', encoding='utf-16', engine='python', nrows=42000)
        messagebox.showinfo("Completado", f"Se ha leído con exito el documento CSV seleccionado en: '{ruta_archivo}'.")
    
cargar_archivo()