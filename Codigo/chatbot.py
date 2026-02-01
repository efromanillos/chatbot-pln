#================================
# Módulo: chatbot.py
#================================

from extraer_texto import cargar_pdf_original, extraer_texto_original
from preparar_texto import dividir_en_parrafos, filtrar_parrafos, limpiar_parrafos
from preprocesamiento import preprocesar_parrafos
from tfidf import entrenar_tfidf, obtener_respuesta
from efectos import escribir_lento, wrap_texto
from traducir import detectar_idioma, traducir



import spacy


# ===== Colores ANSI =====
RESET = "\033[0m"
AZUL = "\033[94m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
ROJO = "\033[91m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
BLANCO = "\033[97m"



#================================================
# Función bucle conversacional
# Carga texto -> preparar -> entrenar -> conversar
#=================================================

nlp = spacy.load("es_core_news_sm")

def iniciar_chatbot(ruta_pdf):

    print("\n=== Chatbot iniciado ===")
    print("Escriba 'salir' para terminar.\n")


    #PROCESOS RELATIVOS AL TEXTO
    #----------------------------------------------------------------------

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

    #---------------------------------------------------------------------

    # 4. Bucle conversacional con memoria contextual (últimas 3 preguntas)

    conversar = True
    historial = []

    while conversar == True:
        pregunta = input(f'{BLANCO}[Tú]: {RESET}')
        print(BLANCO + '─' * 100 + RESET)

        if pregunta.lower() in ('salir', 'exit', 'adios', 'adiós'):
            conversar = False
            print('Chatbot: Hasta luego.')
            break

        
        # 1.Detectar idioma
        idioma_usuario = detectar_idioma(pregunta)

        # 2. Traducir la pregunta a español
        pregunta_es = traducir(pregunta, origen='auto', destino='es')
        
        # 3. Memoria contextual: Añadir la pregunta traducida al historial (para que la memoria de contexto este en español)

        historial.append(pregunta_es)

        # Mantener solo las últimas 3 preguntas, borrar historial y empezar de cero para no mezclar preguntas nuevas con antiguas
        if len(historial) > 3:
            historial = [pregunta_es] #solo se guarda la nueva pregunta sobreescribiendo la lista historial con otra nueva llamada historial también
                                      #el anterior historial queda huerfano y Python se encargará de borrarlo (Garabage Collector)

        # 4. Construir pregunta con contexto (últimas 3 preguntas) -> Las 2 ó 3 preguntas almacenadas en historial se pasan juntas al modelo
        pregunta_con_contexto = ' '.join(historial[-3:])

        # 5. Obtener respuesta en español
        respuesta_es = obtener_respuesta(
            pregunta_original=pregunta_con_contexto,
            nlp=nlp,
            vectorizador=vectorizador,
            matriz_tfidf=matriz_tfidf,
            parrafos_originales=parrafos_preparados
        )

        # 6. Tradicir respuesta al idioma original del usuario

        respuesta_final = traducir(respuesta_es, origen='es', destino=idioma_usuario)
        
        texto_envuelto = wrap_texto(respuesta_final, ancho=90)
        escribir_lento(f'{VERDE}[Chatbot]: {RESET}' + texto_envuelto)
        print(BLANCO + '─' * 100 + RESET)

        

        