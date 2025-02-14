# Escribe un programa que sume todos los elementos de una lista de n
n= int(input("ingrese el numero de elementos de la lista "))
lista=[]
for i in range (n):
    x=int(input(f"ingrese el elemento {i+1} "))
    lista.append(x)
sum=0
for i in lista:
    sum+= i
print("la suma de todos los elementos es de ", sum)