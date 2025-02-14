#Escribe un programa que cuente el número de veces que aparece un carácter 
#específico en una cadena de texto ingresada por el usuario. 
tx=input("ingrese el texto ")
nc=input("ingrese el caracter a contar ")
sum=0
for i in tx:
    if i == nc:
        sum+=1
print(f"el numero de veces que aparece {nc} es de {sum}")
