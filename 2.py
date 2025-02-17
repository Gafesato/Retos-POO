# Autor: Samuel Fernando Garzón Toro
# Reto 2

"""
He creado una función que verifica si una palabra es un palíndromo 
utilizando dos iteradores: uno desde el inicio y otro desde el final. 
En cada iteración se comparan los caracteres correspondientes; si son 
distintos, se devuelve `False`. Si al terminar el bucle no se encuentran 
diferencias, se retorna `True`.
"""

def verificar_palindromo(palabra: str) -> bool:
    """Verifica si una palabra es un palíndromo."""
    iterador_normal: int = 0
    iterador_reverso: int = len(palabra) - 1

    while iterador_reverso >= iterador_normal:
        if palabra[iterador_reverso] != palabra[iterador_normal]:
            return False
        iterador_normal += 1
        iterador_reverso -= 1

    return True


if __name__ == "__main__":
    print("Bienvenido al verificador de palíndromos.")
    palabra: str = input("Introduce una palabra sin espacios y en minúscula: ")
    resultado = verificar_palindromo(palabra)
    print(f"La palabra '{palabra}' es palíndromo: {resultado}")
