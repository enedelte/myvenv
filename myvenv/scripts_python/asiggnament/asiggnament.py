import pandas as pd
import tkinter as tk
from tkinter import messagebox, filedialog, Tk, Text, Scrollbar, Frame, END
import csv
import os
import warnings
warnings.simplefilter('ignore')


def consulta_asignacion():
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
                                 sep=';',
                                 delimiter=None,
                                 header=0,
                                 encoding='latin-1',
                                 engine='python',
                                 nrows=21,
                                 on_bad_lines='skip',
                                 quoting=csv.QUOTE_NONE
                                 )
        
        messagebox.showinfo("Completado", "Se ha cargado la asignación de manera exitosa.")

        mostrar_ventana(asignacion)

    except FileNotFoundError as e:
        messagebox.showerror("Error", str(e))

def mostrar_ventana(df):
    ventana = Tk()
    ventana.title("DataFrame Viewer")

    ventana.title("Asignación")#nombre ventana
    ventana.configure(bg="#002633") # Código de color para verde marino oscuro
    ventana.geometry("800x500-100-50")# Configurar el tamaño ventana
    ventana.maxsize(800, 500)
    ventana.minsize(500, 500)

    frame = Frame(ventana)
    frame.pack(expand=True, fill='both')

    text_widget = Text(frame, wrap='none', borderwidth=0, padx=10, pady=10, font=('Courier New', 10))
    text_widget.grid(row=0, column=0, sticky='nsew')

    scrollbar_y = Scrollbar(frame, command=text_widget.yview)
    scrollbar_y.grid(row=0, column=1, sticky='nsew')

    scrollbar_x = Scrollbar(frame, command=text_widget.xview, orient='horizontal')
    scrollbar_x.grid(row=1, column=0, sticky='nsew')

    text_widget['yscrollcommand'] = scrollbar_y.set
    text_widget['xscrollcommand'] = scrollbar_x.set

    text_widget.insert(END, df.to_string(index=False))

    ventana.mainloop()

consulta_asignacion()