#variaveis
G=6.67*10e-11
m1=float(input("digite a massa do primeiro objeto em kg:"))
m2=float(input("digite a massa do segundo objeto em kg:"))
r=float(input("digite a distância entre os objetos em metros:"))
#calculo
F=G*(m1*m2)/r**2
#retorno
print("A força gravitacional entre os objetos é de", F, "N")