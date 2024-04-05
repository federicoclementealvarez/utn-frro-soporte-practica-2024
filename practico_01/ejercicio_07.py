"""Slicing."""


def es_palindromo(palabra: str) -> bool:
    return True if palabra == palabra[::-1] else False


# NO MODIFICAR - INICIO
assert not es_palindromo("amor")
assert es_palindromo("radar")
assert es_palindromo("")
# NO MODIFICAR - FIN


###############################################################################
import math

def mitad(palabra: str) -> str:
    return palabra[:math.ceil(len(palabra)/2)]


# NO MODIFICAR - INICIO
assert mitad("hello") == "hel"
assert mitad("Moon") == "Mo"
assert mitad("") == ""
# NO MODIFICAR - FIN
