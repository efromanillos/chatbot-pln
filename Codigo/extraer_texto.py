"""
En extraer_texto.py se:

 - Carga el PDF original
 - Extrae el texto del PDF
 - Prepara el texto para el posterior preprocesamiento lingüistico
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


def preparar_texto_original(texto):
    """
    Limpieza estructural del texto extraído del PDF:
    - elimina saltos de línea innecesarios
    - une líneas partidas por guiones
    - corrige espacios múltiples
    - elimina espacios al inicio y final
    """

    # 1. Unir palabras cortadas por guiones al final de línea
    texto = texto.replace('-\n', '')

    # 2. Reemplazar saltos de línea por espacios
    texto = texto.replace('\n', ' ')

    # 3. Quitar espacios dobles o triples
    while '  ' in texto:
        texto = texto.replace('  ', ' ')

    # 4. Eliminar espacios al inicio y final
    texto = texto.strip()

    return texto




#PARA HACER PRUEBAS

if __name__ == "__main__":
   pdf = cargar_pdf_original('../Texto_pdf/historia_IA.pdf')
   texto_extraido = extraer_texto_original(pdf)
   texto_preparado = preparar_texto_original(texto_extraido)
   print(texto_preparado)
