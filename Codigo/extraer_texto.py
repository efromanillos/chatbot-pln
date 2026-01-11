"""
==================================================================
En extraer_texto.py se: abre el PDF y se devuleve el texto plano

 - Carga el PDF original
 - Extrae el texto del PDF (texto plano)
 - Prepara el texto para el posterior preprocesamiento lingüistico
==================================================================
"""

from PyPDF2 import PdfReader

def cargar_pdf_original(ruta_pdf):
    pdf_cargado = PdfReader(ruta_pdf)
    return pdf_cargado

def extraer_texto_original(pdf_cargado):
    texto_extraido = ''
    for pagina in pdf_cargado.pages:
        texto = pagina.extract_text()
        if texto:
            texto_extraido += texto +'\n'
    return texto_extraido  #de momento texto_extraido es el pdf separado en página





#PARA HACER PRUEBAS

if __name__ == "__main__":
   pdf = cargar_pdf_original('../Texto_pdf/historia_IA.pdf')
   texto_extraido = extraer_texto_original(pdf)
   print(texto_extraido)
