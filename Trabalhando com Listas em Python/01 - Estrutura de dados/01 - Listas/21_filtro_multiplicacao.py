numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []
for numero in numeros:
        quadrado.append(numero ** 2)
print(quadrado)


numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)