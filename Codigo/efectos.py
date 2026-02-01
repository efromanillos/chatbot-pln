
#====================================
# Módulo para efectos de escritura
# como efecto ""ma´quina de escribir"
# animación tipo: 'escibiendo...'
#====================================


import sys
import time
import textwrap

# ===== Colores ANSI =====
RESET = "\033[0m"
AZUL = "\033[94m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
ROJO = "\033[91m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
BLANCO = "\033[97m"



# ===== Banner de inicio =====
def banner():
    print(BLANCO + '+' + '─' * 46 + '+' + RESET)
    print(BLANCO + '│' + RESET + '                CHATBOT PLN (V1)              ' + BLANCO + '│' + RESET)
    print(BLANCO + '│' + RESET + '      Procesamiento del Lenguaje Natural      ' + BLANCO + '│' + RESET)
    print(BLANCO + '+' + '─' * 46 + '+' + RESET)
    print()



#===============================
# Función para que la respuesta
# se escriba letra por letra cada 
# cierto intervalo de tiempo
#================================

def escribir_lento(texto, velocidad=0.02):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidad)
    print()  # salto de línea al final
    return texto


#============================================
#Función para ajustar el texto de respuesta
#a un párrafo de anchura pasada por parámetro
#============================================

def wrap_texto(texto, ancho=80, indent=''):
    lineas = textwrap.wrap(texto, width=ancho)
    return '\n'.join(lineas)