# Escribe un programa que genere los primeros n números de la secuencia de 
# Fibonacci, donde n es ingresado por el usuario. El valor de n debe estar entre 1 y 50
x = int(input(" ingrese un numero entre 1 y 50 "))
a=0
b=1
for i in range (x):
    a,b = b, a+b
    print(b)