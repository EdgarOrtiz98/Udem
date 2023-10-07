
numero = int(input("Introduce un número entero positivo: "))
impares = []
for i in range(1, numero + 1):
    if i % 2 != 0:
        impares.append(i)
impares_str = ', '.join(map(str, impares))
print("Números impares desde 1 hasta", numero, ":",impares_str)