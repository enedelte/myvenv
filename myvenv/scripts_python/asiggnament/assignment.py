import pandas as pd
from tkinter import messagebox, filedialog
import csv
import os
import warnings
warnings.simplefilter('ignore')

def cargar_y_consultar_asignacion():
    try:
        # Utiliza un path relativo para mayor portabilidad
        ruta_archivo = filedialog.askopenfilename(title="Seleccionar archivo TXT", filetypes=[("Archivos TXT", "*.txt")])

        # Verifica si el usuario canceló la selección
        if not ruta_archivo:
            messagebox.showinfo("Cancelado", "No se seleccionó ningún archivo.")
            return

        # Verifica la extensión del archivo
        if not ruta_archivo.lower().endswith('.txt'):
            messagebox.showerror("Error", "Por favor, seleccione un archivo TXT válido.")
            return

        asignacion = pd.read_csv(ruta_archivo,
                                 delimiter=None,
                                 header=0,
                                 encoding='latin-1',
                                 engine='python',
                                 nrows=30,
                                 on_bad_lines='skip',
                                 quoting=csv.QUOTE_NONE
                                 )

        messagebox.showinfo("Completado", "Se ha cargado la asignación de manera exitosa.")
        return asignacion

    except FileNotFoundError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")


