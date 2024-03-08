import os
import pandas as pd
import numpy as np
import csv


datos = (r'C:\Users\dapache\OneDrive - NUEVA EPS\GO_PQR\pagos_cartera.TXT')
codificaciones = ['utf-8', 'latin-1', 'ISO-8859-1']

for codificacion in codificaciones:
    try:
        reporte = pd.read_csv(datos, header=0, index_col=None, sep='\t', encoding=codificacion, engine='python', skiprows=None, nrows=None).copy()
        df = pd.DataFrame(reporte)
        df.reset_index(drop=True, inplace=True)
        df.columns
        num_filas, num_columnas = df.shape
        print(f'Cargue de información exitosa con codificación: {codificacion}')
        break
    except UnicodeDecodeError:
      print(f'Error al cargar con codificación: {codificacion}')

print('Cargue de información exitosa')
print("Número de filas:", num_filas)
print("Número de columnas:", num_columnas)

print(df)