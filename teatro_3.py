#while/for/if/else
entradaprecio = 1000
edades = []
cantidad_clientes = int(input("Ingrese el número de clientes por favor: "))
contador = 0
while contador < cantidad_clientes:
    edad = int(input("Ingrese la edad del cliente {}: ".format(contador+1)))
    edades.append(edad)
    contador += 1
for edad in edades:
    descuento = 0
    if edad < 5:
        print("Los niños menores de 5 años no pueden entrar al teatro.")
    else:
        if edad <= 14:
            descuento = 0.35
            print("Descuento del 35%.")
        elif edad <= 19:
            descuento = 0.25
            print("Descuento del 25%.")
        elif edad <= 45:
            descuento = 0.10
            print("Descuento del 10%.")
        elif edad <= 65:
            descuento = 0.25
            print("Descuento del 25%.")
        else:
            descuento = 0.35
            print("Descuento del 35%.")
    monto_final = entradaprecio - (entradaprecio * descuento)
    print("El monto final a pagar para el cliente de {} años es: ${}".format(edad, monto_final))
