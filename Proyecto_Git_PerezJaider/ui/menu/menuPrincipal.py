from modules import inventario
from modules import ventas
from modules import aggData
def menu():
    sistema = inventario()
    sistemav=ventas()
    sistemad=aggData()
    while True:
        print("\nSistema de Gestión de Ventas y Compras")
        print("1. Ver inventario")
        print("2. Ver ventas")
        print("3. Registrar sucursales")
    
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            inventario(sistema)
        elif opcion == "2":
            ventas(sistemav)
        elif opcion == "3":
            aggData(sistema)
        else:
            print("Opción no válida. Por favor, seleccione nuevamente.")
if __name__ == "__main__":
    menu()