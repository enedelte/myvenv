import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def cargue_masivos():
    # Inicializar Tkinter
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter
    
    # Seleccionar múltiples archivos
    archivos_csv = filedialog.askopenfilenames(title='Seleccione los archivos CSV', filetypes=[('CSV Files', '*.csv')])
    
    # Lista de posibles codificaciones
    codificaciones = ['utf-8', 'utf-16', 'latin-1', 'ISO-8859-1']
    
    # Diccionario para almacenar los DataFrames
    dataframes = {}
    
    for archivo in archivos_csv:
        num_filas, num_columnas = None, None
        
        for codificacion in codificaciones:
            try:
                reporte = pd.read_csv(archivo, header=0, index_col=None, sep=',', encoding=codificacion, engine='python').copy()
                df = pd.DataFrame(reporte)
                df.reset_index(drop=True, inplace=True)
                num_filas, num_columnas = df.shape
                dataframes[archivo] = df
                messagebox.showinfo("Éxito", f'Cargue de {archivo} exitosa con codificación: {codificacion}')
                break
            except (UnicodeDecodeError, Exception) as e:
                messagebox.showerror("Error", f'Error al cargar {archivo} con codificación: {codificacion}. Error: {e}')
        
        if num_filas is not None and num_columnas is not None:
            messagebox.showinfo("Éxito", f'Cargue de {archivo} exitosa\nNúmero de filas: {num_filas}\nNúmero de columnas: {num_columnas}')
        else:
            messagebox.showerror("Error", f'No se pudo cargar {archivo} con ninguna de las codificaciones proporcionadas.')
    
    if dataframes:
        mostrar_datos(dataframes)
    else:
        messagebox.showwarning("Advertencia", "No se cargaron datos.")



def mostrar_datos(dataframes):
    # Crear una nueva ventana
    ventana_datos = tk.Toplevel()
    ventana_datos.title("Datos Cargados")
    ventana_datos.configure(bg="#002633")
    ventana_datos.geometry("800x600")
    
    # Crear un Treeview para mostrar los datos
    tree = ttk.Treeview(ventana_datos, columns=("Columnas"), show='headings')
    tree.pack(expand=True, fill='both')
    
    # Crear un marco para el Treeview
    marco = tk.Frame(ventana_datos)
    marco.pack(expand=True, fill='both')

    # Configurar la barra de desplazamiento horizontal y vertical
    scrollbar_y = tk.Scrollbar(marco, orient='vertical', command=tree.yview)
    scrollbar_y.pack(side='right', fill='y')
    
    scrollbar_x = tk.Scrollbar(marco, orient='horizontal', command=tree.xview)
    scrollbar_x.pack(side='bottom', fill='x')
    
    tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
    
    def configurar_treeview(df):
        columnas = df.columns.tolist()
        tree.config(columns=columnas)
        
        # Definir encabezados
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor='center')
        
        # Insertar datos en el Treeview
        for _, row in df.iterrows():
            tree.insert("", tk.END, values=row.tolist())
    
    for archivo, df in dataframes.items():
        configurar_treeview(df)
        tree.insert("", tk.END, values=["" for _ in df.columns])  # Fila en blanco como separador
    
    # Función para confirmar el cierre de la ventana
    def confirmar_cierre():
        if messagebox.askokcancel("Salir", "¿Estás seguro que quieres salir?"):
            ventana_datos.destroy()
    
    # Configurar el evento de cierre de ventana
    ventana_datos.protocol("WM_DELETE_WINDOW", confirmar_cierre)
    
    # Configurar el botón para cerrar la ventana
    btn_cerrar = tk.Button(ventana_datos, text="Cerrar", command=confirmar_cierre, width=10, bg="#f44336", fg="white", relief="flat")
    btn_cerrar.pack(pady=10)
