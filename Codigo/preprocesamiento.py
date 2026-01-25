"""
============================================================
preprocesamiento.py
Donde se preprocesa el texto, preprocesamiento lingüistico

1. procesar_spacy(texto)
   - tokenizar
   - lematizar
   - eliminar stopwords
   - eliminar puntuación
   - filtrar tokens vacíos

2. normalizar_lemas(lemas)
   - pasar a minúsculas
   - opcional: eliminar números
   - opcional: eliminar tokens muy cortos

3. reconstruir_texto(lemas)
   - unir lemas en un string final

4. dividir_en_chunks(texto, tamaño)
   - útil si el PDF es muy largo
============================================================

"""
# preprocesamiento.py

import spacy

from extraer_texto import cargar_pdf_original, extraer_texto_original
from preparar_texto import *

doc2 = []

# Cargar modelo de spaCy en español
nlp = spacy.load("es_core_news_sm")

def preprocesar_texto(texto):
    """
    Preprocesa un párrafo:
    - pasa por spaCy
    - lematiza
    - elimina stopwords
    - elimina puntuación
    - convierte a minúsculas
    """
    #----------------------------------------------------------------------------------------------------------------------
    # ¿Qué hace doc = nlp(texto)?

    #Suponemos que el texto es "Alan Turing publicó un artículo en 1936."
    # Al pasar al modelo nlp(texto) genera una lista doc habiendo:
    # Dividido el texto en una lista de tokens (separa el texto en unidades mínimas, palabras, signos, números, símbolos):
    # ["Alan", "Turing", "publicó", "un", "artículo", "en", "1936", "."]

    # Asignado categoría gramatical (NOUN, VERB, ADJ, ADV, PROPN, DET):
    #Alan → PROPN
    #Turing → PROPN
    #publicó → VERB
    #artículo → NOUN
    #1936 → NUM
    #. → PUNCT

    # Calculado el lema: (publicó -> publicar, números -> número, computables -> computable)

    # Marcado stopwords, puntuación, números, etc. -> Marca cada token con True si es stopword, puntuación, número, etc.

    #"el" → is_stop = True
    #"." → is_punct = True
    #"1936" → like_num = True
    #"Alan" → is_title = True

    #------------------------------------------------------------------------------------------------------------------------

    doc = nlp(texto)

    tokens_limpios = []

    for token in doc:
        if token.is_stop:
            continue #filtrado de stopwords
        if token.is_punct:
            continue #filtrado de signos de puntuación
        if token.like_num:
            continue #filtrado de números

        lema = token.lemma_.lower().strip() #lematización de los tokens + pasados a minúsculas + eliminación de espacios al principio y final (strip)
        if lema:
            tokens_limpios.append(lema) #solo se añade si existe lema se evita añadir vacios

    return ' '.join(tokens_limpios) #reconstrucción del texto preprocesado con Spacy retornado en una lista


def preprocesar_parrafos(lista_parrafos):
    return [preprocesar_texto(p) for p in lista_parrafos]



# PRUEBAS
if __name__ == "__main__":

    
    pdf = cargar_pdf_original('../Corpus/Rodriguez-Cronologia-de-la-Inteligencia-Artificial.pdf')
    texto_extraido = extraer_texto_original(pdf)
    texto_parrafos = dividir_en_parrafos(texto_extraido)
    parrafos_preparados = preparar_parrafos(texto_parrafos)
    print(preprocesar_parrafos(parrafos_preparados))




    """
    Para imprimir lo que nlp() hace al texto:
     
    doc2 = nlp(str(parrafos_preparados))
    for token in doc2:
        print(token.text, token.lemma_, token.pos_) 
    """


    
    