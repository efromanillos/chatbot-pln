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


import spacy

#from extraer_texto import cargar_pdf_original, extraer_texto_original

#from preparar_texto import *
#doc2 = []

# Cargar modelo de spaCy en español
nlp = spacy.load("es_core_news_sm")


#=====================================
# Preprocesamiento del texto con Spacy
#=====================================

def preprocesar_texto(texto, nlp):
    """
    Preprocesa un texto usando spaCy:
    - tokeniza
    - pasa a minúsculas
    - elimina signos, espacios, stopwords, etc.
    - devuelve una cadena con tokens separados por espacios
    """

    #-----------------------------------------------------------------------------------------
    # ¿Qué hace doc = nlp(texto)?
    #
    # Suponemos que el texto es: "Alan Turing publicó un artículo en 1936."
    #
    # spaCy realiza:
    # - Tokenización → ["Alan", "Turing", "publicó", "un", "artículo", "en", "1936", "."]
    # - Etiquetado gramatical → PROPN, VERB, NOUN, etc.
    # - Lematización → publicó → publicar
    # - Marcado de stopwords, puntuación, números, etc.
    #-----------------------------------------------------------------------------------------

    doc = nlp(texto)

    tokens_limpios = []

    for token in doc:

        # Filtrado de stopwords

        if token.is_stop:
            continue 

        # Filtrado de signos de puntuación

        if token.is_punct:
            continue 

        # Filtrado de números

        if token.like_num:
            continue 

        #Lematización de los tokens + minúsculas + eliminación de espacios al principio y final (strip)

        lema = token.lemma_.lower().strip() 

        # Evitar añadir tokens vacíos

        if lema:
            tokens_limpios.append(lema) 

    #Reconstrucción del texto preprocesado con Spacy retornado en un string

    return ' '.join(tokens_limpios) 


#===============================================
# Preprocesamiento del texto a lista de parrafos
#===============================================
def preprocesar_parrafos(lista_parrafos, nlp):
    return [preprocesar_texto(p, nlp) for p in lista_parrafos]



# PRUEBAS
if __name__ == "__main__":

    """
    pdf = cargar_pdf_original('../Corpus/Rodriguez-Cronologia-de-la-Inteligencia-Artificial.pdf')
    texto_extraido = extraer_texto_original(pdf)
    texto_parrafos = dividir_en_parrafos(texto_extraido)
    parrafos_preparados = preparar_parrafos(texto_parrafos)
    print(preprocesar_parrafos(parrafos_preparados))

    """



    """
    Para imprimir lo que nlp() hace al texto:
     
    doc2 = nlp(str(parrafos_preparados))
    for token in doc2:
        print(token.text, token.lemma_, token.pos_) 
    """


    
    