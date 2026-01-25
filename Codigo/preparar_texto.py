"""
===========================================================================
preparar_texto.py
Módulo para preparar el texto previamente al preprocesamiento.
Normalización inicial (minúsculas, quitar saltos de línea, espacios, etc.).
Separación del texto original en párrafos

Limpieza estructural del texto extraído del PDF 
 - Elimina saltos de línea
 - Corrije espacios múltiples
 - Elimina espacios al principio y al final


===========================================================================

"""

from extraer_texto import cargar_pdf_original, extraer_texto_original
import re


def dividir_en_parrafos(texto):
    # Divide por saltos de línea dobles o múltiples
    parrafos = re.split(r'\n\s*\n', texto)
    parrafos = [p.strip() for p in parrafos if p.strip()]
    return parrafos


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

def preparar_parrafos(texto):
    parrafos_preparados = [preparar_texto_original(p) for p in texto]
    return parrafos_preparados

#PARA HACER PRUEBAS

if __name__ == '__main__':
   
   pdf = cargar_pdf_original('../Corpus/Rodriguez-Cronologia-de-la-Inteligencia-Artificial.pdf')
   texto_extraido = extraer_texto_original(pdf)
   texto_parrafos = dividir_en_parrafos(texto_extraido)
   parrafos_preparados = preparar_parrafos(texto_parrafos)

   for i, p in enumerate(parrafos_preparados, 1):
    print(f"--- Párrafo {i} ---")
    print(p)
    print()




  


