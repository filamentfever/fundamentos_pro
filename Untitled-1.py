cartas = {}
def agregar_cartas(dicc, codigo, datos):
    if codigo not in dicc and energia:
        dicc[codigo] ={'nivel' : datos[0], 'energia' : datos[1]}
        return True
    return False

def usar_cartas(dicc, codigo, gasto):
    resta = 0
    if codigo in dicc: 
        if dicc[codigo]['energia'] and gasto <= dicc[codigo]['energia']:
                resta = dicc[codigo]['energia'] - gasto
                if resta >= 0:
                    dicc[codigo]['energia'] = resta
                    dicc[codigo]['nivel'] += '*'
                    return True
        else:
            print('Energia insuficente')
    return False
            
def listar_cartas(dicc):
    print()
    print(f'Cantidad de cartas actuales: {len(dicc)}')
    cantidad = 1
    for codigo, datos in dicc.items():
        print(f'{cantidad}. Carta codigo : {codigo} - nivel : {datos['nivel']} - energia : {datos['energia']}')
        cantidad += 1
    print()

def poca_energia(dicc, umbral):
    print()
    print('Cartas con energía baja: ')
    for codigo, datos in dicc.items():
        if datos['energia'] <= umbral: 
            print(f'Carta codigo : {codigo} tiene la energia baja.')
            
while True:
    print()
    print('Menú de cartas')
    print('1. Registrar una carta')
    print('2. Usar una carta en una batalla')
    print('3. Listar cartas')
    print('4. Mostrar cartas con baja energía')
    print('5. Salir')
    opcion = int(input('Ingrese una opción: '))
        
    if opcion == 1: 
        codigo = input('Ingrese código de la carta: ')
        try: 
            energia = int(input('Ingrese energía de la carta: '))
            if energia < 0:
                energia = False
        except ValueError:
            print('La energía debe ser un numero entero positivo')
            energia = False
            
        if agregar_cartas(cartas, codigo, ['', energia]):
            print('Ingreso con exito')
            print(cartas)
        else:
            print('Ha ocurrido un error, re intente')
    
    elif opcion == 2:
        codigo = input('Ingrese código de la carta: ')
        try:
            gasto = int(input('Ingrese la cantidad de energia a usar'))
            if gasto < 0:
                gasto = False
                print('La energía debe ser un numero entero positivo')
        except ValueError:
            print('La energía debe ser un numero entero positivo')
            gasto = False
        
        if usar_cartas(cartas, codigo, gasto):
            print('Energia usada con exito')
            print(cartas)
        else:
            print('Error')
            
    elif opcion == 3: 
        listar_cartas(cartas)
        
    elif opcion == 4:
        umbral = 10
        poca_energia(cartas, umbral)
        
    elif opcion == 5:
        break

    else:
        print('Opcion no permitida. Reingrese')
