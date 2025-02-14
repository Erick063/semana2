# Escribe un programa que genere la tabla de multplicar de un número dado por el usuario
x = int(input("Ingrese un número: "))

for i in range(1, 11):
    print(f"{x} x {i} = {x * i}")
