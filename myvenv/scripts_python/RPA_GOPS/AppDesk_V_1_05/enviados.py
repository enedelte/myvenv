import win32com.client as win32
import os
import docx
import csv
import datetime
#from funciones import respuestas_path

outlook = win32.Dispatch("Outlook.Application")
enviados =  outlook.GetNamespace("MAPI").GetDefaultFolder(5)


def guardar_correos_en_csv(correos, nombre_archivo):
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Asunto', 'Remitente', 'Fecha de Envío', 'Destinatarios', 'Cuerpo', 'Adjuntos'])
        for correo in correos:
            writer.writerow([
                correo['Asunto'],
                correo['Remitente'],
                correo['Fecha de Envío'],
                correo['Destinatarios'],
                correo['Cuerpo'],
                correo['Adjuntos']
            ])

def correos_enviados_por_fecha(fecha_deseada):
    outlook = win32.Dispatch("Outlook.Application")
    enviados = outlook.GetNamespace("MAPI").GetDefaultFolder(5)
    
    correos_filtrados = []
    
    for item in enviados.Items:
        if item.Class == 43 and item.SentOn.date() == fecha_deseada:  # Verificar si es un correo electrónico y si la fecha de envío coincide
            correo = {
                "Asunto": item.Subject,
                "Remitente": item.SenderName,
                "Fecha de Envío": item.SentOn,
                "Destinatarios": item.To,
                "Cuerpo": item.Body,
                "Adjuntos": ';'.join([attachment.FileName for attachment in item.Attachments])
            }
            correos_filtrados.append(correo)
    
    return correos_filtrados

# Obtener la fecha deseada
#fecha_deseada = datetime.date(2024, 3, 15)  # Cambiar la fecha según sea necesario
fecha_deseada = datetime.date.today()

# Obtener los correos enviados en la fecha deseada
correos = correos_enviados_por_fecha(fecha_deseada)

# Guardar los correos en un archivo CSV
nombre_archivo = 'correos.csv'
guardar_correos_en_csv(correos, nombre_archivo)

print("Los correos enviados el {} han sido guardados en el archivo '{}'.".format(fecha_deseada, nombre_archivo))



# Ahora puedes usar estas listas según sea necesario en tu programa



## Se debe identificar correo de manera individual (por hoja tipo word?)
## Se debe imprimir y guardar en pdf