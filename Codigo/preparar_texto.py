"""
===========================================================================
preparar_texto.py
Módulo para preparar el texto previamente al preprocesamiento.
Normalización inicial (minúsculas, quitar saltos de línea, espacios, etc.).

Limpieza estructural del texto extraído del PDF 
 - Elimina saltos de línea
 - Corrije espacios múltiples
 - Elimina espacios al principio y al final
===========================================================================

"""

from extraer_texto import cargar_pdf_original, extraer_texto_original

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
