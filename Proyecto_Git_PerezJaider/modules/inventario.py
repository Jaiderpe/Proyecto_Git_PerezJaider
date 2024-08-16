import json
from datetime import datetime

def validar_sucursal(sucursal):
    try:
        (sucursal)
        return True
    except ValueError:
        return False

def generar_informe_sucursales(sucursal):
    if not (validar_sucursal(sucursal)):
        print("Error: Las fechas deben estar en el formato 'YYYY-MM-DD' y ser válidas.")
        return

    try:
        
        with open('Proyecto_Git_PerezJaider\data\sucursales.json', 'r') as file:
            data = json.load(file)
        
        ventas = data.get('sucursales', [])

        print(f"Informe de {sucursal}:")
        for sucursal in ventas:
            if sucursal :
                print(f"Nombre del Sucursal: {sucursal['Nombre de Sucursal']}")
                print(f"Direccion: {sucursal['Direccion']}")
                print(f"Contacto: {sucursal['Telefono o Contacto']}")
                print(f"ID del gerente: {sucursal['ID del gerente']}")
                
                print()


    except FileNotFoundError:
        print("No se encontró el archivo de datos de transacciones.")
    except json.JSONDecodeError:
        print("Error al leer el archivo de datos de transacciones. El archivo puede estar corrupto o mal formateado.")
    except Exception as e:
        print(f"Error al generar el informe de ventas: {e}")

   