"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    lista_float = []
    lista_string = []

    for element in lista:
        if(isinstance(element, int)):
            lista_float.append(element)
        else:
            lista_string.append(element)
    
    return lista_string+lista_float


# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    lista_float = [element for element in lista if isinstance(element, int)]
    lista_string = [element for element in lista if isinstance(element, str)]
    return lista_string+lista_float


# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    return sorted(lista, key = lambda x: isinstance(x, int))



# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    lista_float = [element for element in filter(lambda x: isinstance(x,int), lista)]
    lista_string = [element for element in filter(lambda x: isinstance(x,str), lista)]
    return lista_string+lista_float




# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################
"""
CHALLENGE OPCIONAL - Re-escribir de forma recursiva.
def numeros_al_final_recursivo(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    pass # Completar


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN
"""
