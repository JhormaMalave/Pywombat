"""
Definir una función la cual nos permita conocer cuantos dígitos posee un número.
    La función debe tener por nombre _cantidaddigitos.
    La función debe poseer el parámetro numero.
    La función debe retornar la cantidad de dígitos del parámetro.
    No es posible utilizar la función str.
Ejemplos
>>> cantitdad_digitos(10)
2
>>> cantitdad_digitos(2019)
4
>>> cantitdad_digitos(1234567890)
10
"""
def cantidad_digitos(numero:int)->int:
    contador = 0
    potencia = 1
    while numero >= potencia:
        potencia *= 10
        contador += 1
    return contador