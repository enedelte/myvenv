import win32com.client
import os
import time

def imprimir_correo_en_pdf(entry_id, ruta_pdf):
    # Crear una instancia de la aplicación Outlook
    outlook_app = win32com.client.Dispatch("Outlook.Application")
    
    # Crear un objeto Namespace
    namespace = outlook_app.GetNamespace("MAPI")

    try:
        # Obtener el correo electrónico desde el EntryID
        correo_enviado = namespace.GetItemFromID(entry_id)

        # Configurar la impresora virtual de PDF como impresora predeterminada
        correo_enviado.GetInspector.WordEditor.Application.ActivePrinter = "Microsoft Print to PDF"
        
        # Esperar un breve periodo antes de imprimir
        time.sleep(2)
        
        # Imprimir el correo electrónico en la impresora predeterminada (PDF)
        correo_enviado.PrintOut()
        
        # Esperar a que la impresión se complete antes de continuar
        outlook_app.Application.GetNamespace("MAPI").SendAndReceive(True)
        
        # Mover el archivo PDF generado a la ruta especificada
        pdf_generado = os.path.join(os.path.expanduser("~"), "Documents", "Outlook PDF", f"{correo_enviado.Subject}.pdf")
        os.rename(pdf_generado, ruta_pdf)
        
        print(f"Correo electrónico impreso en PDF: {ruta_pdf}")
    
    except Exception as e:
        print(f"Error al imprimir el correo electrónico en PDF: {e}")

# Obtener el EntryID del último correo electrónico enviado
entry_id_ultimo_correo = "RESPUESTA 2808857 VO-DGO-2808857-24"  # Reemplaza con el EntryID real

# Especificar la ruta de destino para el PDF
ruta_destino_pdf = "C:\\Users\\dapache\\OneDrive - NUEVA EPS\\Escritorio\\RPQR"

# Llamar a la función para imprimir el correo en PDF
imprimir_correo_en_pdf(entry_id_ultimo_correo, ruta_destino_pdf)
