# Escribe un programa que encuentre el número mayor y el número menor en una lista de números ingresada por el 
# usuario. Se pueden usar las funciones sort, max y/o min.
n= int(input("ingrese el numero de elementos de la lista "))
lista=[]
for i in range (n):
    x=int(input(f"ingrese el elemento {i+1} "))
    lista.append(x)
lista.sort()
print(f"el numero menor es de {lista[0]} y el mayor es de {lista[n-1]}")