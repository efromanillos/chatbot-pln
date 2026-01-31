



lista = ['a','b','c','d']

for i, letra in enumerate(lista, 1):
    print(i,letra)
print('------------')

for i in range(len(lista)):
    print(i+1,lista[i])

print('------------')


lista2 = [1,2,3,4,5,6,7,8,9,10]
def n_cuadrados (lista):
    return [n**2 for n in lista]

print(n_cuadrados(lista2))

print('------------')

def n_cuadrados_pares(lista):
    return [n**2 for n in lista if n % 2 == 0]

print(n_cuadrados_pares(lista2))

print('------------')


#ejemplo de ' '.join
#une las palabras en la lista por el SEPARADOR (string) entre comillas

palabras = ['hola', 'mundo']
print('****'.join(palabras))
print('****'.join(palabras) + ' aleluya')


#pruebas de strip vs split

texto = """
            Hola, esto es un ejemplo para probar split y strip.   
            Aquí hay espacios al inicio y al final.    
            También hay    varios   espacios   entre   palabras.   '
        """

print('ORIGINAL:')
print(repr(texto))

print('\nstrip():')
print(repr(texto.strip()))

print('\nsplit():')
print(texto.split())
print('\n\n**************************************')

#Split + join

texto2 = 'Hola  mundo           azul'

print('\n',texto2)
print('\n', texto2.split())
print(texto2)


print('\n\n**************************************')

#Prueba de salida de lo que hace nlp(texto)

texto3 = 'Alan Turing descifró la máquina Enigna'

import spacy
nlp = spacy.load('es_core_news_sm')

doc = texto3.lower()
print('\n', doc)

doc = nlp(texto3)

for token in doc:
    print(token.text, token.pos_)