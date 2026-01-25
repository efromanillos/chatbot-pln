"""
===========================================================================
tfidf.py
Módulo para vectorizar el texto preprocesado y la pregunta del usuario
buscar similitud, obtener el párrafo más adecuado a la pregunta,
devolver más de un párrafo si se encuentra similitud en más de uno

Funciones:
tfidf.py
           
    - crear_vectoriazador()
    - entrenar_tfidf()
    - vectorizar_pregunta()
    - buscar_similitud()
    - obtener_mejor_parrafo()
    - obtener_top_k()

===========================================================================

"""

from sklearn.feature_extraction.text import TfidfVectorizer

#=============================================================================================================
#Crear un vectorizador vacío para poder entrenarlo después: ahora es como un "diccionario vacío sin palabras"
#Cuando se entrena con el texto del Corpus contendrá las palabras y puede convertirlas en vectores.
#=============================================================================================================
def crear_vectorizador():
    return TfidfVectorizer(
        lowercase=False, #no es necesario que convierta a minúsculas porque el texto ya viene preprocesado con Spacy

        analyzer=str.split  # Obliga a TF-IDF a usar split() como analizador,
                            # respetando exactamente los tokens generados por spaCy.
                            # Se separa con split() por espacios.
                            # si no se especifica, TF-IDF aplicaría su propio tokenizador interno.
                            #NOTA: un analizador es un componente que:
                                # recibe un texto completo (una cadena)
                                # Lo procesa según unas reglas
                                # Devuelve una lista de tokens (palabras, caracteres, n-gramas)
                                # Ese proceso es el que scikit-learn llama analyzer
                            #NOTA: El analizador de scikit-learn tokeniza según reglas pensadas en inglés
                            #      como el texto está en español, mejor puentear su analizador interno ->split()
    )

#=======================================================
#Entrenar a TF-IDF para que contenga el texto del Corpus
#=======================================================

def entrenar_tfidf(parrafos_preprocesados):
    """
    Entrena el vectorizador TF-IDF con los párrafos ya preprocesados.
    
    Parámetros
    ----------
    parrafos_preprocesados : list[str]
        Lista de párrafos limpios y tokenizados (salida del preprocesamiento).

    Devuelve
    --------
    vectorizador : TfidfVectorizer
        El vectorizador ya entrenado con el vocabulario del corpus.
    
    matriz_tfidf : scipy.sparse matrix
        Matriz TF-IDF donde cada fila representa un párrafo.
    """
    vectorizador = crear_vectorizador()
    matriz_tfidf = vectorizador.fit_transform(parrafos_preprocesados)
    return vectorizador, matriz_tfidf