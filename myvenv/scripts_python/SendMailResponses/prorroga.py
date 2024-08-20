import pandas as pd
from datetime import datetime
import csv

ruta_archivo = r'C:\Users\dapache\OneDrive - NUEVA EPS\Escritorio\Incapacidadxestado.txt'
codificaciones = ['utf-8', 'utf-16', 'latin-1', 'ISO-8859-1']
num_filas, num_columnas = None, None

for codificacion in codificaciones:
    try:
        reporte = pd.read_csv(ruta_archivo, header=0, index_col=None, sep='\t', encoding=codificacion, engine='python').copy()
        df = pd.DataFrame(reporte)
        df.reset_index(drop=True, inplace=True)
        num_filas, num_columnas = df.shape
        print(f'Cargue de información exitosa con codificación: {codificacion}')
        break
    except UnicodeDecodeError:
        print(f'Error al cargar con codificación: {codificacion}')
    except Exception as e:
        print(f'Error al cargar con codificación: {codificacion}. Error: {e}')

if num_filas is not None and num_columnas is not None:
    print('Cargue de información exitosa')
    print("Número de filas:", num_filas)
    print("Número de columnas:", num_columnas)
else:
    print('No se pudo cargar la información con ninguna de las codificaciones proporcionadas.')

print(df)