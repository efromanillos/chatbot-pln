"""
==============================================
menus.py
Donde se diseña el menu principal del programa
==============================================
"""


from elegir_pdf import seleccionar_texto
from chatbot import iniciar_chatbot
import os


def mostrar_menu_principal():

    ruta_pdf = None

    while True:
        os.system('cls')
    
        print('=======================================')
        print('         CHATBOT PLN (v1)              ')
        print('=======================================')
        print('1. Elegir documento del Corpus')
        print('2. Iniciar chatbot')
        print('3. SALIR')
        print('=======================================')

        opc = input('Seleccione una opción: ')

        match opc:
            case '1':
                ruta_pdf= seleccionar_texto()
                print('Ruta selecccionada: ', ruta_pdf)
                input('\nPresione [ENTER] para continuar')
            case '2':
                if ruta_pdf is None:
                    print('Primero debe elegir un Texto')
                    input('\nPresione [ENTER] para continuar')
                else:
                    iniciar_chatbot(ruta_pdf)
            case '3':
                print('\nSaliendo del programa...')
                break
            case _:
                print('Opción NO válida.')
                input('\nPresione [ENTER] para continuar')

if __name__ == "__main__":
    mostrar_menu_principal()