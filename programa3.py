#Escribe un programa que determine si un número dado por el usuario es primo o no. 
x= int(input("ingrese un numero "))
if x%2 != 0:
    p=True
    for i in range(3, int(x**0.5) + 1, 2):  # Solo probamos impares
        if x % i == 0:
            p = False
            print("no es un numero primo ")
            break
    if p == True:
        print(" es un numero primo")
elif x == 1 or x == 2:

    print("es un numero primo")
else:

    print("no es un nuemro primo")