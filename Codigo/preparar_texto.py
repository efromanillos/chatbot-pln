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

"""
def dividir_en_parrafos(texto):

    # Divide por saltos de línea dobles o múltiples
    parrafos_sucios = re.split(r'\n\s*\n', texto)
    
    parrafos_sucios = [p.strip() for p in parrafos_sucios if p.strip()]
    return parrafos_sucios 
"""
    
"""
def dividir_en_parrafos(texto):
    # Convertir múltiples saltos en uno solo
    parrafos_sucios = re.sub(r"\n\s*\n", "\n\n", texto)
    # Dividir por doble salto
    parrafos_sucios = [p.strip() for p in parrafos_sucios.split("\n\n") if p.strip()]
    return parrafos_sucios
"""
import re

#==============================
#Función de segmentación:
#limpieza estructural del texto
#===============================

def dividir_en_parrafos(texto):
    lineas = texto.split("\n")
    parrafos = []
    actual = []

    for linea in lineas:
        l = linea.strip()

        # Saltar líneas vacías
        if not l:
            if actual:
                parrafos.append(' '.join(actual).strip())
                actual = []
            continue

        # Si la línea es muy corta (títulos, números, basura)
        if len(l) < 25 and not re.match(r"^\d{4}", l):
            # Si ya hay contenido acumulado, cerramos párrafo
            if actual:
                parrafos.append(' '.join(actual).strip())
                actual = []
            continue

        # Si la línea empieza con año → posible nuevo párrafo
        if re.match(r"^\d{4}", l):
            if actual:
                parrafos.append(' '.join(actual).strip())
                actual = []
            actual.append(l)
            continue

        # Si la línea es normal, la añadimos al párrafo actual
        actual.append(l)

    # Añadir el último párrafo
    if actual:
        parrafos.append(' '.join(actual).strip())

    return parrafos


#=================
# Filtrar parrafos
#=================
def filtrar_parrafos(parrafos):
    limpios = []
    for p in parrafos:
        if len(p.strip()) < 20:
            continue
        if len(p.split()) < 4:
            continue
        limpios.append(p)
    return limpios


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
   print(parrafos_limpios)
   




  


