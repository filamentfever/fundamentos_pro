#aventureros = {}

"""aventureros = {
    'AV123': {
        'nombre': 'Kevin',
        'edad': 20,
        'puntaje': [100, 512]
    },

    'AV456': {
        'nombre': 'Marcela',
        'edad': 33,
        'puntaje': []
    }
}"""

aventureros = {
    'AV001': {
        'nombre': 'Elena',
        'edad': 28,
        'puntaje': [200, 300, 400]
    },
    'AV002': {
        'nombre': 'Mario',
        'edad': 35,
        'puntaje': []
    },
    'AV003': {
        'nombre': 'Sofía',
        'edad': 22,
        'puntaje': [120, 150]
    },
    'AV004': {
        'nombre': 'Tomás',
        'edad': 28,
        'puntaje': [500]
    },
    'AV005': {
        'nombre': 'Lucía',
        'edad': 35,
        'puntaje': [80, 90, 70]
    }
}

def registrar_aventureros(lista_av, codigo_av, nombre_av, edad_av):
    if codigo_av not in lista_av:
        lista_av[codigo_av] = {'nombre' : nombre_av, 'edad' : edad_av, 'puntaje' : []}
        print('Aventurero ingresado exitosamente. ')
        return True
    elif codigo_av in lista_av:
        print('El código que se intenta ingresar ya está en uso. No se ha registrado su aventurero ')
        return False

def registro_ptj(lista_av, codigo_av, puntaje_av):
    if codigo_av in lista_av:
        lista_av[codigo_av]['puntaje'].append(puntaje_av)
        print('Puntaje ingresado exitosamente. ')
        return True
    elif codigo_av not in lista_av:
        print('El codigo no existe')
        return False
    
def mod_puntaje(lista_av, codigo_av, sesion_av, nuv_ptj):
    if codigo_av in lista_av and 0 <= sesion_av < len(lista_av[codigo_av]['puntaje']): 
        lista_av[codigo_av]['puntaje'][sesion_av] = nuv_ptj
        return True
    else:
        print('Codigo o sesion incorrecta')
        return False

def mostrar_av(lista_av):
    for codigo, datos in lista_av.items():
        promedio = 0
        suma = 0
        nombre = lista_av[codigo]['nombre']
        puntaje = lista_av[codigo]['puntaje']
        for ptj in puntaje:
            suma += ptj
        try:
            promedio = suma / len(puntaje)
            print(f'Aventurero código {codigo} con nombre {nombre} acumula un puntaje de {puntaje} con promedio {promedio}')
        except:
            print(f'No se han encontrado puntajes para calcular promedio del aventurero codigo {codigo}')
        

def prom_bajo(lista_av, umbral):
    for codigo, datos in lista_av.items():
        promedio = 0
        suma = 0
        nombre = datos['nombre']
        puntaje = datos['puntaje']
        for ptj in puntaje:
            suma += ptj
        if len(puntaje):
            promedio = suma / len(puntaje)
        if promedio < umbral:
            print(f'Aventurero codigo {codigo} : {nombre} tiene un promedio bajo el umbral ({promedio})')


def listar_aventureros(lista_av):
    sum = 0
    for codigo, datos in lista_av.items():
        sum = sum + 1
        print(f'AVENTURERO {sum}. codigo : {codigo} / nombre : {datos['nombre']} / edad : {datos['edad']} / puntaje : {datos['puntaje']}')

def ob_av_edad(lista_av, edad):
    encontrar = False
    for codigo, datos in lista_av.items():
        if datos['edad'] == edad:
            print(f'Aventurero codigo : {codigo} > nombre {datos['nombre']} tiene {edad}')
            encontrar = True
    if not encontrar:
        print('No se han encontrado aventureros con la edad presentada')
    
    
while True:
    print("1. Registrar aventurero")
    print("2. Agregar puntaje de sesión")
    print("3. Modificar puntaje")
    print("4. Ver participación total y promedio")
    print("5. Ver aventureros con bajo promedio")
    print("6. Listar aventureros y puntajes")
    print("7. Listar aventureros por edad")
    print("8. SALIR")

    opcion = int(input("Opción: "))

    if opcion == 1:
        nombre = input('Nombre: ')
        codigo = input('Codigo: ')
        edad = int(input('Edad: '))
        registrar_aventureros(aventureros, codigo, nombre, edad)
        print(aventureros)
    
    elif opcion == 2:
        codigo = input('Ingrese un codigo existente: ')
        puntaje = int(input('Ingrese el puntaje del codigo'))
        registro_ptj(aventureros, codigo, puntaje)
        print(aventureros)
    
    elif opcion == 3:
        codigo = input('Ingrese un codigo valido: ')
        sesion = int(input('Ingrese una sesion: '))
        sesion = sesion - 1
        nuevo_puntaje = int(input('Ingrese el puntaje nuevo: '))
        mod_puntaje(aventureros, codigo, sesion, nuevo_puntaje)
        print(aventureros)
    
    elif opcion == 4:
        mostrar_av(aventureros)
    
    elif opcion == 5:
        umbral = 250 #(promedio para no pasar)
        prom_bajo(aventureros, umbral)
    
    elif opcion == 6: 
        listar_aventureros(aventureros)
    
    elif opcion == 7:
        edad = int(input('Ingrese una edad: '))
        ob_av_edad(aventureros, edad)
        
    elif opcion == 8:
        break