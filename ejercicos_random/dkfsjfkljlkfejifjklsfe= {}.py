aventureros = {}

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
    if codigo_av in lista_av and sesion_av <= len(lista_av[codigo_av]['puntaje'])-1: 
        lista_av[codigo_av]['puntaje'][sesion_av] = nuv_ptj
        return True
    else:
        print('Codigo o sesion incorrecta')
        return False

def mostrar_av(lista_av):
    #promedio = 0
    for x in lista_av.items():
        print(lista_av[x]['puntaje'])
        
    
    
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
        
    elif opcion == 8:
        break