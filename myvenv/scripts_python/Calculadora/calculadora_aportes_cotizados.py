import pandas as pd
import numpy as np 
import os

datos = (r"C:\Users\dapache\OneDrive - NUEVA EPS\GO_PQR\pagos_cartera.TXT")

df = pd.read_csv(datos, sep= '\t', encoding="ISO-8859-1", index_col=None, header=0)

df2 = df[['afi_identific', 'afi_fechafil', 'dau_peridecla','dau_diastraba', 'dau_ingbascot','dau_aporempl', 'eau_emp_identific']]

df3 = df2.rename(columns={'afi_identific':'Identificación',
                         'afi_fechafil': 'Fecha Afiliación', 
                         'dau_peridecla': 'Periodo Cotización',
                         'dau_ingbascot': 'IBC',
                         'dau_aporempl': 'Aporte',
                         'eau_emp_identific':'Aportante',
                         'dau_diastraba': 'Días Cotizados'})


df3['Fecha Afiliación'] = pd.to_datetime(df3['Fecha Afiliación'], format='%d/%m/%Y %H:%M:%S').dt.strftime('%d/%m/%Y')
df3['Periodo Cotización'] = pd.to_datetime(df3['Periodo Cotización'], format='%d/%m/%Y %H:%M:%S').dt.strftime('%m/%Y')

tabla_aportes = pd.DataFrame(df3)

arrays = np.array(tabla_aportes)

print(tabla_aportes.head())