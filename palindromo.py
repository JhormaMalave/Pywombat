"""
Definir una función la cual permita conocer si un string es un palíndromo o no.
Un palíndromo es una palabra, o frase, que se lee igual de izquierda a derecha que de derecha a izquierda
Requerimientos:
    La función debe tener por nombre palíndromo.
    La función debe poseer como parámetro la variable sentencia.
    La función debe retornar verdadero(True) si el parámetro es una palíndromo, en caso contrario retornará falso(False).
Ejemplos
>>> palindromo('Anita lava la tina')
True
>>> palindromo('Sometamos o matemos')
True
>>> palindromo('Super palindromo')
False
"""
def palindromo(sentencia:str) -> str:
    sentencia = sentencia.lower()
    sentencia = sentencia.replace(' ','')
    return True if sentencia == sentencia[::-1] else False