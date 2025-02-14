#Escribe un programa que ordene una lista de números ingresada por el usuario 
# de menor a mayo
n= int(input("ingrese el numero de elementos de la lista "))
lista=[]
for i in range (n):
    x=int(input(f"ingrese el elemento {i+1} "))
    lista.append(x)
lista.sort()
print("esta es la lista ordenada de menor a mayor ", lista ) 