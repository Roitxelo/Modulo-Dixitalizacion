def calcular(numeros):

    minimo = min(numeros)
    maximo = max(numeros)
    media = sum(numeros) / len(numeros)

    return minimo, maximo, media


lista = [4, 7, 1, 9]

print(calcular(lista))