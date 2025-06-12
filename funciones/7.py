def cantidad(nombre):
    if len(nombre) > 6:
        return True
    else:
        return False
    
def mascota():
    nombres = input('Ingrese el nombre de su mascota: ')
    if cantidad(nombres):
        print('El nombre está bien :]')
    else: 
        print('El nombren está mal :[')
        
mascota()
