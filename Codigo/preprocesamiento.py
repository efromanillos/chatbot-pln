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

from preparar_texto import *
#doc2 = []

# Cargar modelo de spaCy en español
nlp = spacy.load("es_core_news_sm")


#=====================================
# Preprocesamiento del texto con Spacy
#=====================================

def preprocesar_texto(texto, nlp):
    doc = nlp(texto)
    tokens_limpios = []

    for token in doc:
        if token.is_space or token.is_punct:
            continue

        # Conservar números (años)
        if token.like_num:
            tokens_limpios.append(token.text)
            continue

        # Conservar nombres propios
        if token.pos_ == "PROPN":
            tokens_limpios.append(token.lemma_.lower())
            continue

        # Conservar sustantivos, verbos y adjetivos aunque sean stopwords
        if token.pos_ in ("NOUN", "VERB", "ADJ"):
            tokens_limpios.append(token.lemma_.lower())
            continue

        # Conservar adverbios importantes
        if token.pos_ == "ADV":
            tokens_limpios.append(token.lemma_.lower())
            continue

    return " ".join(tokens_limpios)


#============================================================
# Preprocesamiento del texto a lista de strings (de parrafos)
#============================================================
def preprocesar_parrafos(lista_parrafos, nlp):

    return [preprocesar_texto(p, nlp) for p in lista_parrafos]



# PRUEBAS
if __name__ == "__main__":

    
    pdf = cargar_pdf_original('../Corpus/InteligenciaArtificialNuriaOliver.pdf')
    texto_extraido = extraer_texto_original(pdf)
    texto_parrafos = dividir_en_parrafos(texto_extraido)
    parrafos_preparados = limpiar_parrafos(texto_parrafos)
    print(preprocesar_parrafos(parrafos_preparados, nlp))
    
    



    """
    Para imprimir lo que nlp() hace al texto:
     
    doc2 = nlp(str(parrafos_preparados))
    for token in doc2:
        print(token.text, token.lemma_, token.pos_) 
    """


    
    