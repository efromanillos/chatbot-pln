"""
=================================================================
elegir_pdf.py: donde se selecciona el pdf del directorio /Textos/ 
que sirve como "base de conocimiento".
=================================================================
"""



import os

def seleccionar_texto(ruta_textos='../Textos/'):
    """
    Lista los archivos PDF dentro del ruta_textos indicado y permite al usuario
    seleccionar uno. Devuelve la ruta completa del PDF elegido.
    """

    # 1. Comprobar que el ruta_textos existe
    if not os.path.isdir(ruta_textos):
        print(f'El directorio "{ruta_textos}" no existe.') #{ruta_textos} entre comillas porque muestra el texto no valor de una variable
        return None

    # 2. Obtener todos los archivos del ruta_textos
    elementos = os.listdir(ruta_textos) #elementos es una lista con los pdf que hay en el ruta_textos
    

    # 3. Filtrar solo los PDFs
    archivos = []
    for f in elementos:
        nombre_minusculas = f.lower() #se pasa a minúsculas toda la lista de elementos para 
        if nombre_minusculas.endswith('.pdf'):
            archivos.append(f)
            

    # 4. Comprobar si hay PDFs
    if not archivos:
        print('No se encontraron archivos PDF en el directorio.')
        return None

    # 5. Mostrar lista numerada de PDFs
    print('\nPDFs disponibles:\n')
    for i, nombre in enumerate(archivos, start=1):
        print(f'{i}. {nombre}')

    # 6. Pedir selección al usuario
    while True:
        opcion = input('\nSeleccione un PDF por número: ')

        # Validar que la entrada sea un número
        if not opcion.isdigit():
            print('Entrada no válida. Introduzca un número.')
            continue

        #Casting porque opcion es string y queremos entero para poder validar
        opcion = int(opcion) 

        # Validar que opcion esta entre 1 y total de elementos de la lista archivos
        if 1 <= opcion <= len(archivos):
            pdf_elegido = archivos[opcion - 1] #el usr elije comenzando por 1 pero el índice de las lista comienza en 0, si usr elije 2, accede al archivo cuyo índice es 1
            ruta_completa_pdf = os.path.join(ruta_textos, pdf_elegido)
            print(f'\nHas seleccionado: {pdf_elegido}\n')
            return ruta_completa_pdf
        else:
            print("Número fuera de rango. Inténtelo de nuevo.")

        
