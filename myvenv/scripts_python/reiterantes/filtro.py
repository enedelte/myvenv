import pandas as pd
import time

def lectura_base():
    ruta_archivo = r"C:\Users\dapache\Downloads\Tasa_Quejas_Operaciones_Gestion_Diarias.csv"
    reporte = pd.read_csv(ruta_archivo, header=0, index_col=0, sep='\t', encoding='utf-16', engine='python', nrows=42000)

    df = pd.DataFrame(reporte)
    
#    print("Antes de limpieza:")
#    print(df.shape)
#    print(df.columns)
    
#    print("\nDespués de limpieza:")
#    print(df_limpio.shape)
#    print(df_limpio.columns)
    time.sleep(1)
    print('Cargue de información exitosa')
    
    limpieza = df[['Tipo Proceso', 'Nombre', 'Fecha Radicacion', 'Número de Radicación', 'Número de identificación', 'Número de identificación.1']].copy()
    limpieza.replace('-', pd.NA, inplace=True)
    limpieza.dropna(subset=['Tipo Proceso', 'Nombre', 'Fecha Radicacion', 'Número de Radicación', 'Número de identificación', 'Número de identificación.1'], inplace=True)
    return limpieza

lectura_base()
time.sleep(1)

print('Limpieza de datos exitosa')


