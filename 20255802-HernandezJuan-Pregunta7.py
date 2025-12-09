from os import system
if system("clear") != 0: system("cls")

d_u_i = input("")
condicion1 = (len(d_u_i) == 10)
condicion2 = (d_u_i[8]=="-")
condicion3 = (d_u_i[-1].isdigit()==True)
print(condicion1 and condicion2 and condicion3)