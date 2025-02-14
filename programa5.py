# Escribe un programa que cuente el número de vocales en una cadena de texto ingresada por el usuario. 
tx = input("ingrese un texto: ").lower()
vocales = "aeiou"
print(tx)
sum = 0
for i in tx:
    if i in vocales:
        sum = sum +1
print(" la cantidad de vocales es de ", sum)
