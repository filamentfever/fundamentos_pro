def edad():
    edades = int(input('Ingrese su edad: '))
    es_mayor = edades > 18
    if es_mayor:
        return True

if edad():
    print('Es mayor de edad')
else: 
    print('Es menor de edad')
