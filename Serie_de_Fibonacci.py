print ("Fibonacci")
print("Programa que obtiene la serie de Fibonacci y Atonal Linares Leonardo")
print ("Hecho por: Martinez Heerra Alondra")

n = int(input("\nIngrese la cantidad de terminos de la serie de Fibonacci: "))

a = 0
b = 1

print("Serie de Fibonacci: \n", end="")

for i in range (n):
    print(a, end=" ")
    temp = a 
    a = b 
    b = temp + b 
    
 