# Escribe un programa que sume los dígitos de un número entero ingresado por el usuario. 
x= input("ingrese un numero ")
sum=0
for i in x:
    sum+= int(i)
print("la suma de los digitos del numero es de ", sum)