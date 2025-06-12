def rangos(min,max):
    suma = 0
    for numero in range(min,max):
        if numero % 2 != 0:
            suma = suma + numero
    print(suma)
    
min = 2
max = 10

rangos(min,max)
