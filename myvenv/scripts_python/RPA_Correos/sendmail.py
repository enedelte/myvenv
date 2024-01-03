import win32com.client as win32

def enviar_correo(desde, para, asunto, cuerpo):
    outlook = win32.Dispatch("Outlook.Application")

    # Crear un nuevo correo
    mail = outlook.CreateItem(0)
    mail.Subject = asunto
    mail.Body = cuerpo
    mail.To = para

    # Establecer la dirección de correo desde el alias o carpeta compartida
    mail.SentOnBehalfOfName = desde

    # Enviar el correo
    mail.Send()

def main():
    # Dirección de correo del alias o carpeta compartida
    correo_desde = "respuestas.pqr@nuevaeps.com.co"

    # Dirección de correo del destinatario
    correo_para = "daalejoar@gmail.com"

    asunto = "Asunto del correo"
    cuerpo = "Cuerpo del correo de prueba."

    # Enviar el correo desde el alias o carpeta compartida
    enviar_correo(correo_desde, correo_para, asunto, cuerpo)

if __name__ == "__main__":
    main()
