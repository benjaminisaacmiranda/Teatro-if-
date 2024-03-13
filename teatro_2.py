precio_entrada = 1000

# Datos de los clientes
edad = int(input("Ingrese la edad del cliente: "))

# Calcular el descuento según la edad ingresada
descuento = 0
if edad < 5:
    print("Los niños menores de 5 años no pueden entrar al teatro.")
else:
    if edad <= 14:
        descuento = 0.35
        print("Descuento del 35% aplicado.")
    if edad >= 15 and edad <= 19:
        descuento = 0.25
        print("Descuento del 25% aplicado.")
    if edad >= 20 and edad <= 45:
        descuento = 0.10
        print("Descuento del 10% aplicado.")
    if edad >= 46 and edad <= 65:
        descuento = 0.25
        print("Descuento del 25% aplicado.")
    if edad >= 66:
        descuento = 0.35
        print("Descuento del 35% aplicado.")

# Calcular el monto final a pagar
monto_final = precio_entrada - (precio_entrada * descuento)
print("El monto final a pagar es: $", monto_final)
