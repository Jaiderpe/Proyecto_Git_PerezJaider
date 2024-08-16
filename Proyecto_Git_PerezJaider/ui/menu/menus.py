import modules.funcionesGlobales as fg
import modules.inventario as invet
def tittleInformes():
    tittleInfor = """
********************************
*           INFORMES           *
*      Sucursal Pradera        *
********************************
"""
    print(tittleInfor)

def MenuInformes():
    fg.borrar_pantalla()
    tittleInformes()
    menu_informes = """1. Generar Informe de Sucursales """
    print(menu_informes)
    print(" ")
    
    try:
        op = int(input("Ingrese la opción: "))
        if op == 1:
            fg.borrar_pantalla()
            sucursal = input("Ingrese el nombre de la sucursal: ")
            fg.borrar_pantalla()
            invet.generar_informe_sucursales(sucursal)
        elif op == 2:
            return 3
        else:
            print("Opción no válida")
    except ValueError:
        print("Ingrese una opción correcta")
    
    fg.pausar_pantalla()
    return None