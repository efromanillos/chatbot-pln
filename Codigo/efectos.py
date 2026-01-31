
#====================================
# Módulo para efectos de escritura
# como efecto ""ma´quina de escribir"
# animación tipo: 'escibiendo...'
#====================================


import sys
import time

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