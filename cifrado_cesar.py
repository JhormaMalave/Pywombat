"""
Mediante una función implementar el cifrado cesar.
    La función debe tener por nombre cifrado.
    La función debe poseer dos parámetros: sentencia de tipo string y llave de tipo entero.
    El parámetro sentencia será el texto a cifrar.
    El parámetro llave hará referencia a la cantidad de espacios a desplazar.
    Por default el parámetro llave tendrá el valor de 10.
    La función debe retornar el texto cifrado.
    Los números y espacios dentro de la sentencia deben conservarse.
    La función debe retornar el cifrado en minúscula (No importa que la entrada haya tenido mayúsculas).
    Al hacer el llamado de la función es posible omitir un valor para el parámetro llave.
Ejemplos
>>> cifrado('Hola Como estas', 23)
elix zljl bpqxp
>>> cifrado('supersentencia')
cezobcoxdoxmsk
>>> cifrado('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 23)
cezobcoxdoxmsk
Ayuda: Puedes apoyarte de la biblioteca string para generar la lista de letras del alfabeto.
"""

def cifrado(sentencia:str, llave:int=10)->str:
    sentencia = sentencia.lower()
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    palabras = sentencia.split(' ')

    texto_cifrado = []
    for palabra in palabras:
        palabra_nueva = ''
        for letra in palabra:
            indice = abecedario.index(letra) + llave
            if indice < len(abecedario):
                palabra_nueva += abecedario[indice]
            else:
                palabra_nueva += abecedario[indice - len(abecedario)]
        texto_cifrado.append(palabra_nueva)

    texto_cifrado = ' '.join(texto_cifrado)
    return texto_cifrado