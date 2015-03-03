
lista = ["Papaya", "Banan", "Apelsin", "Banan", "Druvor", "Melon"]


def filter(lista, x):
    newlista = []
    for i in lista:
        if i == x:
            newlista.append(i)
    return newlista

print filter(lista,"Banan")

def exclude(lista, x):
    for i in range(len(lista)-1,-1,-1):
        if lista[i] == x:
            lista.pop(i)
    return lista

print exclude(lista, "Banan")