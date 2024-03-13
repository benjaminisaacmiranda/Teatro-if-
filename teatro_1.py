#if
entradaprecio = 1000
edad = int(input("Ingrese la edad del cliente por favor: "))
descuento = 0
if edad < 5:
    print("Los niños menores de 5 años no pueden entrar al teatro.")
if edad >= 5 and edad <= 14:
    descuento = 0.35
    print("Descuento del 35%.")
if edad >= 15 and edad <= 19:
    descuento = 0.25
    print("Descuento del 25%.")
if edad >= 20 and edad <= 45:
    descuento = 0.10
    print("Descuento del 10%.")
if edad >= 46 and edad <= 65:
    descuento = 0.25
    print("Descuento del 25%.")
if edad >= 66:
    descuento = 0.35
    print("Descuento del 35%.")
monto_final = entradaprecio - (entradaprecio * descuento)
print("El monto final a pagar es: $", monto_final)
