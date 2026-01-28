"""
===========================================================================
tfidf.py
Módulo para vectorizar el texto preprocesado y la pregunta del usuario
buscar similitud, obtener el párrafo más adecuado a la pregunta,
devolver más de un párrafo si se encuentra similitud en más de uno.

Funciones:
tfidf.py
           
    - crear_vectoriazador()
    - entrenar_tfidf()
    - vectorizar_pregunta()
    - buscar_similitud()
    - obtener_respuesta()
    - obtener_mejor_parrafo()
    - obtener_top_k()

===========================================================================

"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocesamiento import preprocesar_texto

from extraer_texto import cargar_pdf_original, extraer_texto_original
from preparar_texto import *
from preprocesamiento import *



#=============================================================================================================
#Crear un vectorizador vacío para poder entrenarlo después: ahora es como un "diccionario vacío sin palabras"
#Cuando se entrena con el texto del Corpus contendrá las palabras y puede convertirlas en vectores.
#=============================================================================================================
def crear_vectorizador():
    return TfidfVectorizer(
        lowercase=False, 
        analyzer=str.split  
    )

#========================================================
#Entrenar a TF-IDF para que contenga el texto del Corpus
#========================================================

def entrenar_tfidf(parrafos_preprocesados):
 
    vectorizador = crear_vectorizador() 
    matriz_tfidf = vectorizador.fit_transform(parrafos_preprocesados) 
    return vectorizador, matriz_tfidf


#============================================================
# Vectorizar la preguna de usuario con vectorizador entrenado
#============================================================

def vectorizar_pregunta(pregunta_preprocesada, vectorizador):
    
    vector_pregunta = vectorizador.transform([pregunta_preprocesada])

    return vector_pregunta


#=============================================================================================================
# Buscar la similitud entre la pregunta vectorizada y todos los párrafos del corpus.
# Devuelve el índice del párrafo más similar.
#=============================================================================================================
def buscar_similitud(vector_pregunta, matriz_tfidf):
   
    similitudes = cosine_similarity(vector_pregunta, matriz_tfidf)[0]
    indice_max = similitudes.argmax()

    return indice_max, similitudes

#=============================================================================================================
# Obtener la respuesta del chatbot:
# Preprocesa la pregunta, la vectoriza, calcula similitud y devuelve el párrafo más parecido.
#=============================================================================================================
def obtener_respuesta(pregunta_original, nlp, vectorizador, matriz_tfidf, parrafos_originales):
    
    pregunta_preprocesada = preprocesar_texto(pregunta_original, nlp)
    vector_pregunta = vectorizar_pregunta(pregunta_preprocesada, vectorizador)
    indice_max, similitudes = buscar_similitud(vector_pregunta, matriz_tfidf)
    return parrafos_originales[indice_max]



# PRUEBAS
if __name__ == "__main__":

    pregunta = '¿Unimate?'

    pdf = cargar_pdf_original('../Corpus/Rodriguez-Cronologia-de-la-Inteligencia-Artificial.pdf')
    texto_extraido = extraer_texto_original(pdf)

    # 1) Dividir en párrafos
    texto_parrafos = dividir_en_parrafos(texto_extraido)

    # 2) Filtrar párrafos basura  ← 🔥 AQUÍ
    texto_parrafos = filtrar_parrafos(texto_parrafos)


    # 3) Limpiar párrafos (quitar guiones, saltos, espacios)
    parrafos_preparados = limpiar_parrafos(texto_parrafos)

    # 4) Preprocesar para TF‑IDF
    parrafos_preprocesados = preprocesar_parrafos(parrafos_preparados, nlp)

    # 5) Entrenar TF‑IDF
    vectorizador, matriz_tfidf = entrenar_tfidf(parrafos_preprocesados)

    # 6) Obtener respuesta
    respuesta = obtener_respuesta(
        pregunta_original=pregunta,
        nlp=nlp,
        vectorizador=vectorizador,
        matriz_tfidf=matriz_tfidf,
        parrafos_originales=parrafos_preparados
    )

    print(respuesta)
#print(preprocesar_texto("1842, la matemática y escritora británica Ada Lovelace programa el primer algoritmo destinado a ser procesado por una máquina.", nlp))