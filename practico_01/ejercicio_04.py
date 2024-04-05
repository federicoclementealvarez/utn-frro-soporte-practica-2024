"""Expresiones Booleanas."""


def es_vocal_if(letra: str) -> bool:
    if(letra[0].lower() == 'a'):
        return True
    elif (letra[0].lower() == 'e'):
        return True
    elif (letra[0].lower() == 'i'):
        return True
    elif (letra[0].lower() == 'o'):
        return True
    elif (letra[0].lower() == 'u'):
        return True
    return False




# NO MODIFICAR - INICIO
assert es_vocal_if("a")
assert not es_vocal_if("b")
assert es_vocal_if("A")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_if_in(letra: str) -> bool:
    vocales = 'aeiou'

    return True if(letra[0].lower() in vocales) else False


# NO MODIFICAR - INICIO
assert es_vocal_if_in("a")
assert not es_vocal_if_in("b")
assert es_vocal_if_in("A")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_in(letra: str) -> bool:
    vocales = 'aeiou'

    return (letra[0].lower() in vocales)


# NO MODIFICAR - INICIO
assert es_vocal_in("a")
assert not es_vocal_in("b")
assert es_vocal_in("A")
# NO MODIFICAR - FIN
