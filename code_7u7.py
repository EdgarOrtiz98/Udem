def calcular_media(lista):
    suma = sum(lista)
    media = suma / len(lista)
    return media

muestra = [1, 2, 3, 4, 5, 6, 7, 9, 10] 
resultado = calcular_media(muestra)
print("La media de la muestra es:", resultado)