def correo(nombre,apellido): 
    correos = nombre + '.' + apellido + '@gmail'
    return correos

nom = 'martina'
ape = 'cordova'
print(correo(nom, ape))
