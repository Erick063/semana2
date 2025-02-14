#Escribe un programa que genere una lista de n números aleatorios entre 1 y 100, 
#donde n es ingresado por el usuario.
import random
n = int(input("ingrese un numero "))
lista = []
for i in range (n):
    x=random.randint(1,100)
    lista.append(x)
print("los numeros generados aleatoriamente son ", lista)
