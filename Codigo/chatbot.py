#================================
# Módulo: chatbot.py
#================================

from extraer_texto import cargar_pdf_original, extraer_texto_original
from preparar_texto import dividir_en_parrafos, filtrar_parrafos, limpiar_parrafos
from preprocesamiento import preprocesar_parrafos
from tfidf import entrenar_tfidf, obtener_respuesta
from efectos import escribir_lento
import spacy



#================================================
# Función bucle conversacional
# Carga texto -> preparar -> entrenar -> conversar
#=================================================

nlp = spacy.load("es_core_news_sm")

def iniciar_chatbot(ruta_pdf):

    print("\n=== Chatbot iniciado ===")
    print("Escriba 'salir' para terminar.\n")


    # 1. Cargar PDF
    pdf = cargar_pdf_original(ruta_pdf)
    texto = extraer_texto_original(pdf)

    # 2. Preparar texto
    parrafos = dividir_en_parrafos(texto)
    parrafos = filtrar_parrafos(parrafos)
    parrafos_preparados = limpiar_parrafos(parrafos)
    parrafos_preprocesados = preprocesar_parrafos(parrafos_preparados, nlp)

    # 3. Entrenar TF‑IDF
    vectorizador, matriz_tfidf = entrenar_tfidf(parrafos_preprocesados)

    # 4. Bucle conversacional con memoria contextual (últimas 3 preguntas)

    conversar = True
    historial = []

    while conversar == True:
        pregunta = input("Tú: ")

        if pregunta.lower() in ('salir', 'exit', 'adios', 'adiós'):
            conversar = False
            print('Chatbot: Hasta luego.')
            break

        #Añadir pregunta al historial

        historial.append(pregunta)

        # Si ya hay 3 preguntas, borrar historial y empezar de cero para no mezclar preguntas nuevas con antiguas
        if len(historial) > 3:
            historial = [pregunta] #solo se guarda la nueva pregunta sobreescibiendo la lista historial con otra nueva llamada historial también
                                   # el anterior historial queda huerfano y Python se encargará de borrarlo (Garabage Collector)

        #Construir pregunta con contexto (últimas 3 preguntas) -> Las 2 ó 3 preguntas almacenadas en historial se pasan juntas al modelo
        pregunta_con_contexto = ' '.join(historial[-3:])

        respuesta = obtener_respuesta(
            pregunta_original=pregunta_con_contexto,
            nlp=nlp,
            vectorizador=vectorizador,
            matriz_tfidf=matriz_tfidf,
            parrafos_originales=parrafos_preparados
        )

        escribir_lento('Chatbot: ' + respuesta)