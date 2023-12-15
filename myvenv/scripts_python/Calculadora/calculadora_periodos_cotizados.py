import pandas as pd
import numpy as np



datos = {
    'Semanas': [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41],
    'Días Gestación': [175, 182, 189, 196, 203, 210, 217, 224, 231, 238, 245, 252, 259, 266, 273, 280, 287],
    'Periodos Cotizados': [6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 10]
    }

tabla = pd.DataFrame(datos)


def obtener_periodos_cotizados(semanas, tabla):
    try:
        resultado = tabla.loc[tabla['Semanas'] == semanas, 'Periodos Cotizados'].values
        if len(resultado) > 0:
            return resultado[0]
        else:
            return f"No hay datos para {semanas} semanas."
    except IndexError:
        return f"No hay datos para {semanas} semanas."

# Solicitar al usuario que ingrese las semanas deseadas
semanas_input = input("Ingresa la cantidad de semanas que deseas buscar: ")

try:
    semanas_buscadas = int(semanas_input)
    periodos_cotizados = obtener_periodos_cotizados(semanas_buscadas, tabla)
    print(f"Para la cantidad de Semanas: {semanas_buscadas}, el usuario debe presentar la cantidad de Periodos Cotizados: {periodos_cotizados}")
except ValueError:
    print("Por favor, ingresa un número entero para las semanas.")