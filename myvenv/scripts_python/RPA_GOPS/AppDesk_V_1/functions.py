import os
import win32com.client as win32
import pandas as pd
from tkinter import filedialog 

outlook = win32.Dispatch("Outlook.Application")
ruta_base = r"C:\Users\dapache\OneDrive - NUEVA EPS\Escritorio\RPQR" #cambiar dirección según tipo de usuario
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

def seleccionar_archivo():
    archivo_csv = filedialog.askopenfilename(title="Seleccionar archivo CSV", filetypes=[("Archivos CSV", "*.csv")])
    if archivo_csv:
        enviar_correos_desde_csv(archivo_csv)
        print('Se han enviado por completo los correos relacionados')




