# Escribe un programa que sume todos los numeros pares del 1 al 100 usando un ciclo for
n=0
for i in range (0,101):
    if i % 2 == 0:
        n=i+n
print(n)
