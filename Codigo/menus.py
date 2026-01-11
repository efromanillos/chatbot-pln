"""
==============================================
menus.py
Donde se diseña el menu principal del programa
==============================================
"""


from elegir_pdf import seleccionar_texto
import os

def mostrar_menu_principal():

    while True:
        os.system('cls')
    
        print('=======================================')
        print('         CHATBOT PLN (v1)              ')
        print('=======================================')
        print('1. Elegir documento del Corpus')
        print('2. SALIR')
        print('=======================================')

        opc = input('Seleccione una opción: ')

        match opc:
            case '1':
                ruta= seleccionar_texto()
                print('Ruta selecccionada: ', ruta)
                input('\nPresione [ENTER] para continuar')
            case '2':
                print('\nSaliendo del programa...')
                break
            case _:
                print('Opción NO válida.')
                input('\nPresione [ENTER] para continuar')

if __name__ == "__main__":
    mostrar_menu_principal()