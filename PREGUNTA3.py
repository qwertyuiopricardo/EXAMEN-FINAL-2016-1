while True:
    n = int(input("Ingresar numero: "))
    if n >= 1:
        break

while True:
    a = n % 10
    if a < 10:
        break
print("El ultimo digito del numero es:", a)
b = n
while True:
    b = b / 10
    if b < 10:
        break
print("El primero digito del numero es:", b)