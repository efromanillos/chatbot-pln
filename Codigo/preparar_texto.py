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

#=================================
#Dividir todo el texto en parrafos
#=================================

def dividir_en_parrafos(texto):

    # Divide por saltos de línea dobles o múltiples
    parrafos_sucios = re.split(r'\n\s*\n', texto)
    parrafos_sucios = [p.strip() for p in parrafos_sucios if p.strip()]
    return parrafos_sucios

#====================================================
#Limpieza estructural de todos los párrafos del texto
#====================================================

def limpiar_parrafos(parrafos_sucios):
    parrafos_limpios = []

    for p in parrafos_sucios:
        parrafo = p.replace('-\n', '')
        parrafo = parrafo.replace('\n', ' ')
        while '  ' in parrafo:
            parrafo = parrafo.replace('  ', ' ')
        parrafo = parrafo.strip()
        parrafos_limpios.append(parrafo)

    return parrafos_limpios


#PARA HACER PRUEBAS

if __name__ == '__main__':
   
   pdf = cargar_pdf_original('../Corpus/Rodriguez-Cronologia-de-la-Inteligencia-Artificial.pdf')
   texto_extraido = extraer_texto_original(pdf)
   parrafos = dividir_en_parrafos(texto_extraido)
   parrafos_limpios = limpiar_parrafos(parrafos)
   print(parrafos)
   




  


