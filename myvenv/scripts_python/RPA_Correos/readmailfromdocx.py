import os
import docx
import re
import csv

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
