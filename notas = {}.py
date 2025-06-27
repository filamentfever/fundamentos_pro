# Pedí al usuario nombres y notas hasta que escriba "salir".
# Guardá los datos en un diccionario.
# Luego mostrales las notas y el promedio por estudiante.

notas = {}
promedio = {}
while True:
    nombre = input('Ingrese el nombre del alumno: ')
    if nombre == 'salir':
        break
    notas[nombre] = []
    nota = 0
    suma = 0
    while nota != -1:
        nota = int(input('Ingrese las notas del alumno (-1 para salir): '))
        notas[nombre].append(nota)
    del notas[nombre][len(notas[nombre])-1]
    for x in notas[nombre]:
        suma += x
        prom = suma / len(notas[nombre])
    promedio[nombre] = prom
    print(notas)
    print(promedio)
for nom, nota in notas.items(): 
    for y,prom in promedio.items():
        if nom == y:
            print(f'las notas del alumno {nom} son {nota} y el promedio es {prom}')

