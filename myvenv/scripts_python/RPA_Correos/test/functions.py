import os
import win32com.client as win32
import pandas as pd
from tkinter import filedialog 
import docx
import re
import csv

outlook = win32.Dispatch("Outlook.Application")
ruta_base = r"C:\\Users\\" #cambiar dirección según tipo de usuario
alias = "respuestas.pqr@nuevaeps.com.co"

def enviar_correo_desde_alias(destinatario, asunto, cuerpo, adjunto, alias):
    mail = outlook.CreateItem(0)
    mail.SentOnBehalfOfName = alias
    mail.To = destinatario
    mail.Subject = asunto
    mail.Body = cuerpo

    ruta_completa = os.path.join(ruta_base, adjunto)

    if os.path.exists(ruta_completa):
        mail.Attachments.Add(ruta_completa)
    else:
        print(f"No se pudo encontrar el archivo: {ruta_completa}")

    mail.Send()

def enviar_correos_desde_csv(archivo_csv):
    df = pd.read_csv(archivo_csv)

    for index, fila in df.iterrows():
        destinatario = fila['Correo Electronico']
        asunto = 'RESPUESTA SOLICITUD {}'.format(fila['Nombre Archivo'])
        cuerpo = 'Reciba un cordial saludo en nombre de NUEVA EPS S.A. Agradecemos su confianza al exponernos sus inquietudes.\n\n Adjunto remitimos respuesta a su Solicitud.\n\nPorque nos interesa ofrecerle un mejor servicio, queremos que nos cuente cómo fue su experiencia con la solución de su solicitud PQRS para lo cual lo invitamos a contestar dos preguntas en el siguiente enlace https://forms.office.com/r/pJaFmjkLW1\n\n“En el presente mensaje se tuvo en cuenta la protección de datos consagrada en la Ley 1581 DE 2012. Por favor no responda a este mensaje ya que la cuenta de correo se encuentra configurada sólo para generar respuestas masivas”.\n\n PRUEBA ELECTRÓNICA: Al recibir el acuse de recibo con destino a ésta oficina, se entenderá como aceptado y tendrá recepción como documento prueba de la entrega del usuario. (Ley 527 del 18/08/1999).\n\nAtentamente,\n\nDirección de Gestión Operativa\nVicepresidencia de Operaciones\n Bogotá D.C. – Colombia\n https://www.nuevaeps.com.co/.'.format(fila['Nombre Archivo'])
        adjunto = fila['Adjunto']

        enviar_correo_desde_alias(destinatario, asunto, cuerpo, adjunto, alias)

def seleccionar_archivo_csv():
    archivo_csv = filedialog.askopenfilename(title="Seleccionar archivo CSV", filetypes=[("Archivos CSV", "*.csv")])
    if archivo_csv:
        enviar_correos_desde_csv(archivo_csv)
        print('Se han enviado por completo los correos relacionados')

def extract_emails_from_docx(docx_file):
    doc = docx.Document(docx_file)
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = []

    for para in doc.paragraphs:
        matches = re.findall(email_pattern, para.text)
        emails.extend(matches)

    return emails

def main():
    folder_path = r"C:\Users\dapache\OneDrive - NUEVA EPS\GO_PQR\GESTIÓN_PQR\2024\ENERO\05012024"

    # Lista para almacenar los correos electrónicos de todos los archivos
    all_emails = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".docx") and not filename.startswith('~$'):
            docx_file_path = os.path.join(folder_path, filename)
            emails = extract_emails_from_docx(docx_file_path)

            if emails:
                # Obtener el nombre del archivo sin la extensión .docx
                nombre_archivo_sin_extension = os.path.splitext(filename)[0]

                # Crear el nombre del archivo con extensión .pdf
                nombre_archivo_pdf = f"{nombre_archivo_sin_extension}.pdf"

                all_emails.append((nombre_archivo_sin_extension, emails, nombre_archivo_pdf))

    # Escribir los correos electrónicos en un archivo CSV
    csv_file_path = "archivo.csv"
    with open(csv_file_path, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Nombre Archivo", "Correo Electronico", "Adjunto"])
        for nombre_archivo, emails, nombre_archivo_pdf in all_emails:
            csv_writer.writerow([nombre_archivo, ', '.join(emails), nombre_archivo_pdf])

    print(f"Se han recolectado los correos electrónicos y se han guardado en '{csv_file_path}'.")

if __name__ == "__main__":
    main()


