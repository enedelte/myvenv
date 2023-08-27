import os
from docx2pdf import convert

word_path = (r"C:\Users\dapache\OneDrive - NUEVA EPS\GO_PQR\GESTIÓN_PQR\2023\JULIO\19072023")
pdf_path = (r"C:\Users\dapache\OneDrive - NUEVA EPS\Escritorio\RPQR")

convert(word_path, pdf_path)