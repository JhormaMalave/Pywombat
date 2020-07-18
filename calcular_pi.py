"""
π (pi) es sin duda una de las constantes matemáticas más importantes de todos los tiempos. Todos conocemos el valor de π (pi) , bueno, quizás solo sus primeros decimales.
3.1415
Es por ello que en esta ocasión es necesarios que implementes el _Problema de Basilea_ para encontrar el "valor" de π (pi).
Es obligatorio obtener por lo menos los primeros 6 decimales.
Pista: Tendrás que multiplicar por 6 y realizar una raíz cuadrada.
"""


from math import sqrt
operacion = 0
for i in range(1,10000000):
    operacion += 1 / i ** 2
operacion *= 6
resultado = sqrt(operacion)
print("Los seis primeros valores de PI son: {:.7}".format(resultado))