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
    folder_path = r"C:\Users\dapache\OneDrive - NUEVA EPS\GO_PQR\GESTIÓN_PQR\2023\DICIEMBRE\27122023"

    # Lista para almacenar los correos electrónicos de todos los archivos
    all_emails = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".docx") and not filename.startswith('~$'):
            docx_file_path = os.path.join(folder_path, filename)
            emails = extract_emails_from_docx(docx_file_path)

            if emails:
                all_emails.append((filename, emails))  # Guardamos el nombre del archivo y los correos electrónicos en una tupla

    # Escribir los correos electrónicos en un archivo CSV
    csv_file_path = "emails_collected.csv"
    with open(csv_file_path, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Nombre del archivo", "Correos electrónicos"])
        for filename, emails in all_emails:
            csv_writer.writerow([filename, ', '.join(emails)])

    print(f"Se han recolectado los correos electrónicos y se han guardado en '{csv_file_path}'.")

if __name__ == "__main__":
    main()
