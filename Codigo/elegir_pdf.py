# elegir_pdf.py: donde se selecciona el pdf que sirve como base de conocimiento.

import os

def seleccionar_texto(directorio="../Texto_pdf/"):
    """
    Lista los archivos PDF dentro del directorio indicado y permite al usuario
    seleccionar uno. Devuelve la ruta completa del PDF elegido.
    """

    # 1. Comprobar que el directorio existe
    if not os.path.isdir(directorio):
        print(f"El directorio '{directorio}' no existe.")
        return None

    # 2. Obtener todos los archivos del directorio
    elementos = os.listdir(directorio)
    

    # 3. Filtrar solo los PDFs
    archivos = []
    for f in elementos:
        nombre_minusculas = f.lower()
        if nombre_minusculas.endswith(".pdf"):
            archivos.append(f)

    # 4. Comprobar si hay PDFs
    if not archivos:
        print("No se encontraron archivos PDF en el directorio.")
        return None

    # 5. Mostrar lista numerada de PDFs
    print("\nPDFs disponibles:\n")
    for i, nombre in enumerate(archivos, start=1):
        print(f"{i}. {nombre}")

    # 6. Pedir selección al usuario
    while True:
        opcion = input("\nSelecciona un PDF por número: ")

        # Validar que la entrada sea un número
        if not opcion.isdigit():
            print("Entrada no válida. Introduce un número.")
            continue

        opcion = int(opcion)

        # Validar que opcion esta entre 1 y total de elementos de la lista archivos
        if 1 <= opcion <= len(archivos):
            pdf_elegido = archivos[opcion - 1] #el usr elije comenzando por 1 pero el índice de las lista comienza en 0, si usr elije 2 accede al índice 1
            ruta_completa = os.path.join(directorio, pdf_elegido)
            print(f"\nHas seleccionado: {pdf_elegido}\n")
            return ruta_completa
        else:
            print("Número fuera de rango. Inténtelo de nuevo.")


    #PARA HACER PRUEBAS

if __name__ == "__main__":
    os.system('cls')
    ruta = seleccionar_texto()
    print("Ruta seleccionada:", ruta)