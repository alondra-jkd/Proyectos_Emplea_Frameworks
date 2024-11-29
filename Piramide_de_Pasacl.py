print ("Triangulo de Pascal")
print ("Hecho por: Martinez Herrera Alondra y Atonal Linares Leonardo")
print ("Programa que muestra el Triangulo de Pascal hasta la fila que el usuario indique.")

fil = int(input("\nIngresar el numero de filas del Triangulo de Pascal: "))

for i in range(fil):
    num = 1
    for j in range(i + 1):
        if j > 0:
            num = num * (i - j + 1) // j

        print (num, end=" ")
    print ("")
   
