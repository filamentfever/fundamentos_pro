
def sumar():
    suma = 0
    for i in range(15):
        n = int(input('Ingrese un numero: '))
        suma = suma + n
    return suma

final = sumar()
print(final)