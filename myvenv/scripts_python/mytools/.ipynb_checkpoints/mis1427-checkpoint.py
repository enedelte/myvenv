import os
import pandas as pd
import openpyxl as op

certificados_1427_PQRS = (r"C:\Users\dapache\OneDrive - NUEVA EPS\CERTIFICADOS DECRECTO_1427_PQRS\certificados_1427_PQRS.xlsx")

df = op.load_workbook(certificados_1427_PQRS)

print(df)
