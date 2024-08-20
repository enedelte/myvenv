import os
from docx2pdf import convert

def convert_word_to_pdf(word_path, pdf_path):
    convert(word_path, pdf_path)

if __name__ == "__main__":
    word_path = r"C:\Users\dapache\OneDrive - NUEVA EPS\GO_PQR\GESTIÓN_PQR\2024\ENERO\04012024"
    pdf_path = r"C:\Users\dapache\OneDrive - NUEVA EPS\Escritorio\RPQR"
    convert_word_to_pdf(word_path, pdf_path)