from os import system
if system("clear") != 0: system("cls")

V1 = float(input())

print(V1 == int(V1))

#condicion1 = (V1.isdigit()==True)
#print(condicion1)

#para comparar tipos es 
print(type(V1) is int)