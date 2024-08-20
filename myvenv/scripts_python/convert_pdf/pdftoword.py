from pdf2docx import Converter

# Ruta corregida del archivo PDF
pdf_file = 'C:/Users/dapache/OneDrive - Universidad Cooperativa de Colombia/Personal/CV_DAAR.pdf'

# Ruta donde deseas guardar el archivo de Word resultante
docx_file = 'C:/Users/dapache/OneDrive - Universidad Cooperativa de Colombia/Personal/CV_DAAR.docx'

# Crear un convertidor
cv = Converter(pdf_file)

# Convertir el archivo PDF a Word
cv.convert(docx_file, start=0, end=None)

# Cerrar el convertidor
cv.close()

print(f"El archivo PDF ha sido convertido a Word y guardado en '{docx_file}'")
