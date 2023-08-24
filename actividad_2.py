# un palindromo es una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda ejemplo: oso, ojo, otto.
# su mision es conocer un algoritmo que permita conocer una palabra dad por el usuario si es un palindromo o no 

def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

palabra_usuario = input("Ingrese una palabra o frase: ")

if es_palindromo(palabra_usuario):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
