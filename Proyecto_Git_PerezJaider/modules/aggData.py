import json
import modules.funcionesGlobales as fg

def añadirSucursal():
    nombreSucursal = input("Ingrese el nombre de la nueva sucursal: ")
    direccion = input("Ingrese la direccion: ")
    contacto = input("Ingrese el correo o telefono de la sucursal: ")
    id_gerente = input ("Ingrese el ID del gerente: ")
        
    datosSucursal = {
        'Nombre de Sucursal': nombreSucursal,
        'Direccion': direccion,
        'Telefono o Contacto: ': contacto,
        'ID del gerente': id_gerente,
        
        },

    aggDataSucursal('sucursales', datosSucursal)
    print("¡Se agrego correctamente!")
    fg.pausar_pantalla()
    

def aggDataSucursal(namespace, sucursal):
    try:
        with open('Proyecto_Git_PerezJaider\data\sucursales.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    if namespace not in data or not isinstance(data[namespace], list):
        data[namespace] = []

    data[namespace].append(sucursal)

    with open('Proyecto_Git_PerezJaider\data\sucursales.json', 'w') as file:
        json.dump(data, file, indent=4)