"""
============================================================
preprocesamiento.py
Donde se preprocesa el texto, preprocesamiento lingüistico
convertir_texto_minusculas()
eliminar_puntuacion()
tokenizar()
dividir_en_chunks()
============================================================

"""



import spacy

nlp = spacy.load('es_core_news_sm')