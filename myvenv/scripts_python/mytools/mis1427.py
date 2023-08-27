import os
import pandas as pd
import openpyxl
import warnings

certificados_1427_PQRS = (r"C:\Users\dapache\OneDrive - NUEVA EPS\CERTIFICADOS DECRECTO_1427_PQRS\certificados_1427_PQRS.xlsx")

with warnings.catch_warnings():
    warnings.simplefilter("ignore")

df = pd.read_excel(certificados_1427_PQRS)

print(df)
