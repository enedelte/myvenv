import pandas as pd
import os
import csv
from datetime import datetime, timedelta


#DECRETO 923/17
#https://www.suin-juriscol.gov.co/viewDocument.asp?id=30030705#ver_30114064

rangos_documentos = [
    (2, range(0, 8)),
    (3, range(8, 15)),
    (4, range(15, 22)),
    (5, range(22, 29)),
    (6, range(29, 36)),
    (7, range(36, 43)),
    (8, range(43, 50)),
    (9, range(50, 57)),
    (10, range(57, 64)),
    (11, range(64, 70)),
    (12, range(70, 76)),
    (13, range(76, 82)),
    (14, range(82, 88)),
    (15, range(88, 94)),
    (16, range(94, 100))
]

def verificar_documento(digitos_documento, rangos_documentos):
    for rango, digitos_rango in rangos_documentos:
        if digitos_documento in digitos_rango:
            return rango
    return None

def dia_habil_en_mes(fecha):
    dias_habiles = []
    fecha_actual = datetime(fecha.year, fecha.month, 1)
    while fecha_actual.month == fecha.month:
        if fecha_actual.weekday() < 5:  # 0 es lunes, 4 es viernes
            dias_habiles.append(fecha_actual)
        fecha_actual += timedelta(days=1)
    return dias_habiles

fecha = datetime(2023, 12, 15)
dias_habiles = dia_habil_en_mes(fecha)
print("Días hábiles en diciembre de 2023:", dias_habiles)

documento = 1231201
ultimos_digitos = int(str(documento)[-2:])
rango_documento = verificar_documento(ultimos_digitos, rangos_documentos)
if rango_documento is not None:
    print(f"Los últimos dos dígitos del documento corresponden al rango {rango_documento}.")
else:
    print("Los últimos dos dígitos del documento no corresponden a ningún rango.")
