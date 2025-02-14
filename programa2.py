# Escribe un programa que calcule el factorial de un número dado por el usuario
# usando un ciclo while. El número debe estar entre 1 y 20. 
x = int(input("ingrese un nuemero del 1 al 20 " ))
while  1 > x or x > 20:
     x = int(input("ingrese un nuemero del 1 al 20 " ))
y = x
if x == 1:
    print("el factorial es 1")
else :
    while x > 1:
        x=x-1
        y = y*x
    print(y)
    
