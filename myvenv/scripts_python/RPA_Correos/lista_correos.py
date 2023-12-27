import pandas as pd 
import csv
import os


lista_correos = {'Nombre Archivo' : 'Prueba',
                 'Correo Electronico' : 'karen.prieto@nuevaeps.co',
                 'Adjunto' : 'prueba.pdf'
}


correos = pd.DataFrame([lista_correos])

print(correos)

ruta = ('C:\\Users\\dapache\\python_scripts\\myvenv\\scripts_python\\mytools\\')

correos.to_csv(ruta + 'archivo.csv', index=False)
