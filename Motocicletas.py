print("Base de datos MOTOCICLETAS")
print("Hecho por: Martinez Herrera Alondra y Atonal Linares Leonardo")
print("Base de datos que muestra la lista de motocicletas registradas")

contraseña = "1234"

while True:
    contraseñaI = input("\nIntroduce la contraseña: ")
    if contraseñaI == contraseña:
        print("Contraseña correcta.")
        print("Bienvenido a la Base de datos.")
        break
    else:
        print("Contraseña incorrecta. Intentelo de nuevo.")

motocicletas = {}

continuar = True
while continuar:
    print("\nMenú Principal")
    print("1) Agregar (Insertar/Alta)")
    print("2) Consulta (Mostrar)")
    print("3) Modificar (Editar)")
    print("4) Eliminar (Borrar)")
    print("5) Salir del programa")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre de la motocicleta: ")
        if nombre in motocicletas:
            print("El nombre ya existe.")
        else:
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            estado = input("Estado: ")
            color = input("Color: ")
            potencia = input("Potencia: ")
            motor = input("Motor: ")
            año = input("Año: ")
            válvulas = input("Válvulas: ")
            cilindros = input("Cilindros: ")
            capacidad = input("Capacidad de Combustible: ")

            motocicletas[nombre] = {
                "Nombre de la motocicleta": nombre,
                "Marca": marca,
                "Modelo": modelo,
                "Estado": estado,
                "Color": color,
                "Potencia": potencia,
                "Motor": motor,
                "Año": año,
                "Válvulas": válvulas,
                "Cilindros": cilindros,
                "Capacidad de Combustible": capacidad
            }
            print(f"Motocicleta {nombre} agregada exitosamente.")

    elif opcion == "2":
        nombre = input("Ingrese el nombre de la motocicleta para consultar: ")
        if nombre in motocicletas:
            print(f"\nInformación de {nombre}:")
            for clave, valor in motocicletas[nombre].items():
                print(f"{clave}: {valor}")
        else:
            print("El nombre de la motocicleta no existe.")

    elif opcion == "3":
        nombre = input("Ingrese el nombre de la motocicleta a modificar: ")
        if nombre in motocicletas:
            print(f"Modificando {nombre}")
            for clave in motocicletas[nombre]:
                nuevo_valor = input(f"Ingrese el nuevo valor para {clave} (deje vacío para no cambiar): ")
                if nuevo_valor:
                    motocicletas[nombre][clave] = nuevo_valor
            print(f"Motocicleta {nombre} modificada exitosamente.")
        else:
            print("La motocicleta no existe.")

    elif opcion == "4":
        nombre = input("Ingrese el nombre de la motocicleta a eliminar: ")
        if nombre in motocicletas:
            del motocicletas[nombre]
            print(f"Motocicleta {nombre} eliminada exitosamente.")
        else:
            print("La motocicleta no existe.")

    elif opcion == "5":
        print("Saliendo del programa. ¡Adiós!")
        continuar = False

    else:
        print("Opción no válida. Intente de nuevo.")
