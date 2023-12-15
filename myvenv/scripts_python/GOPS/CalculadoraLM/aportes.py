import pandas as pd 
import os


aportes = (r"C:\Users\dapache\OneDrive - NUEVA EPS\GO_PQR\pagos_cartera.TXT")

df = pd.read_csv(aportes, sep= '')

print(df)
