import modules.inventario as inventario
import modules.ventas as ventas
import modules.aggData as aggD

def menu():
    
    while True:
        print("\nSistema de Gestión de Ventas y Compras")
        print("1. Ver inventario")
        print("2. Ver ventas")
        print("3. Registrar sucursales")
    
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            inventario.gestionInventario()
        elif opcion == "2":
            None
        elif opcion == "3":
            aggD.añadirSucursal()
        else:
            print("Opción no válida. Por favor, seleccione nuevamente.")
if __name__ == "__main__":
    menu()