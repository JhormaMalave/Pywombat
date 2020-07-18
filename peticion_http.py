"""
Dado el siguiente endpoint.
https://pokeapi.co/api/v2/pokemon/1/
Mostrar en consola el nombre del Pokemon.
Ejemplo
El nombre del pokemon es: bulbasaur
Ayuda:
    Una muy buena idea es utilizar la librería requests para realizar peticiones HTTP.
    JSONView es una extensión de Chrome que nos permite visualizar los objetos JSON de una manera mucho más legible.
"""

from requests import get
response = get('https://pokeapi.co/api/v2/pokemon/1/').json()
print('El nombre del pokemon es {}'.format(response['forms'][0]['name']))