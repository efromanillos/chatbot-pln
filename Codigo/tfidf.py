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

#=============================================================================================================
#Crear un vectorizador vacío para poder entrenarlo después: ahora es como un "diccionario vacío sin palabras"
#Cuando se entrena con el texto del Corpus contendrá las palabras y puede convertirlas en vectores.
#=============================================================================================================
def crear_vectorizador():
    return TfidfVectorizer(
        
        #no es necesario que convierta a minúsculas porque el texto ya viene preprocesado con Spacy
        lowercase=False, 
        
        
        # analyzer=str.split: 
        # Obliga a TF-IDF a usar split() como analizador,
        # respetando exactamente los tokens generados por spaCy.
        # Se separa con split() por espacios.
        # Si no se especifica, TF-IDF aplicaría su propio tokenizador interno.
        #
        # NOTA: un analizador es un componente que:
            # Recibe un texto completo (una cadena)
            # Lo procesa según unas reglas
            # Devuelve una lista de tokens (palabras, caracteres, n-gramas)
            # Ese proceso es el que scikit-learn llama analyzer
        #    
        # NOTA: El analizador de scikit-learn tokeniza según reglas pensadas en inglés.
        #       Como el texto está en español, mejor puentear su analizador interno ->split()
        analyzer=str.split  
    )

#========================================================
#Entrenar a TF-IDF para que contenga el texto del Corpus
#========================================================

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
    #Creación de un vectorizador vacío sin vocabulario ni IDF
    vectorizador = crear_vectorizador() 

    # Entrenar el vectorizador y generar la matriz TF-IDF:

    # Al aplicar matriz_tfidf = vectorizador.fit_transform(parrafos_preprocesados) 
    # ocurren dos procesos simultáneos:

    #PROCESO 1: El vectorizador aprende el vocabulario del corpus.

    # - Identifica todas las palabras únicas del corpus.
    # - Las ordena alfabéticamente.
    # - Asigna un índice a cada palabra.
    # - Calcula los valores IDF.
    # - Guarda todo en sus atributos internos (vocabulary_, idf_, stop_wrods_, etc).
    
    #PROCESO 2: Se genera la matriz TF-IDF (representación numérica del corpus)

    # - Cada párrafo se convierte en un vector numérico.
    # - Cada vector tiene tantas columnas como palabras del vocabulario.
    # - Cada celda contiene el valor TF‑IDF correspondiente.
    # - El resultado es una matriz dispersa (sparse matrix).

    matriz_tfidf = vectorizador.fit_transform(parrafos_preprocesados) 
    return vectorizador, matriz_tfidf


#============================================================
# Vectorizar la preguna de usuario con vectorizador entrenado
#============================================================

def vectorizar_pregunta(pregunta_preprocesada, vectorizador):
    """
    Convierte la pregunta preprocesada en un vector TF-IDF usando el vectorizador entrenado.

    Parámetros
    ----------
    pregunta_preprocesada : str
        Pregunta ya limpia y tokenizada (salida del preprocesamiento).

    vectorizador : TfidfVectorizer
        Vectorizador previamente entrenado con el corpus.

    Devuelve
    --------
    vector_pregunta : scipy.sparse matrix
        Vector TF-IDF de la pregunta, con la misma dimensionalidad que la matriz del corpus.
    """

    # Transformar la pregunta usando el vectorizador entrenado.
    # IMPORTANTE:
    # - Se usa transform() y no fit_transform(), porque el vectorizador ya está entrenado.
    # - La pregunta debe ir dentro de una lista, ya que transform() espera una colección de documentos.
    # - El resultado es un vector disperso (sparse matrix) con forma (1, n_palabras_unicas).
    vector_pregunta = vectorizador.transform([pregunta_preprocesada])

    return vector_pregunta


#=============================================================================================================
# Buscar la similitud entre la pregunta vectorizada y todos los párrafos del corpus.
# Devuelve el índice del párrafo más similar.
#=============================================================================================================
def buscar_similitud(vector_pregunta, matriz_tfidf):
    """
    Calcula la similitud del coseno entre la pregunta y cada párrafo del corpus.

    Parámetros
    ----------
    vector_pregunta : scipy.sparse matrix
        Vector TF-IDF de la pregunta (forma: 1 x vocabulario).

    matriz_tfidf : scipy.sparse matrix
        Matriz TF-IDF del corpus (forma: n_parrafos x vocabulario).

    Devuelve
    --------
    indice_max : int
        Índice del párrafo más similar a la pregunta.

    similitudes : numpy.ndarray
        Array con los valores de similitud para cada párrafo (útil para depuración).
    """

    # Calcular la similitud del coseno entre:
    # - el vector de la pregunta (1 x vocabulario)
    # - la matriz del corpus (n_parrafos x vocabulario)
    #
    # Resultado:
    # - Un array de forma (1, n_parrafos) con un valor de similitud por párrafo.
    similitudes = cosine_similarity(vector_pregunta, matriz_tfidf)[0]

    # Obtener el índice del párrafo con mayor similitud.
    # Este será el párrafo que el chatbot devolverá como respuesta.
    indice_max = similitudes.argmax()

    return indice_max, similitudes

#=============================================================================================================
# Obtener la respuesta del chatbot:
# Preprocesa la pregunta, la vectoriza, calcula similitud y devuelve el párrafo más parecido.
#=============================================================================================================
def obtener_respuesta(pregunta_original, nlp, vectorizador, matriz_tfidf, parrafos_originales):
    """
    Procesa la pregunta del usuario y devuelve el párrafo más similar del corpus.

    Parámetros
    ----------
    pregunta_original : str
        Pregunta tal como la escribe el usuario.

    nlp : spaCy model
        Modelo spaCy ya cargado para el preprocesamiento.

    vectorizador : TfidfVectorizer
        Vectorizador TF-IDF previamente entrenado con el corpus.

    matriz_tfidf : scipy.sparse matrix
        Matriz TF-IDF del corpus (n_parrafos x vocabulario).

    parrafos_originales : list[str]
        Lista de párrafos originales (sin preprocesar), para devolver la respuesta final.

    Devuelve
    --------
    respuesta : str
        El párrafo más similar a la pregunta del usuario.
    """

    # 1. Preprocesar la pregunta con spaCy
    #    Esto garantiza que la pregunta se convierta en tokens limpios,
    #    igual que los párrafos del corpus.
    pregunta_preprocesada = preprocesar_texto(pregunta_original, nlp)

    # 2. Vectorizar la pregunta usando el vectorizador entrenado
    #    IMPORTANTE: transform() usa el vocabulario e IDF ya aprendidos.
    vector_pregunta = vectorizar_pregunta(pregunta_preprocesada, vectorizador)

    # 3. Calcular la similitud entre la pregunta y todos los párrafos del corpus
    indice_max, similitudes = buscar_similitud(vector_pregunta, matriz_tfidf)

    # 4. Devolver el párrafo más similar
    return parrafos_originales[indice_max]