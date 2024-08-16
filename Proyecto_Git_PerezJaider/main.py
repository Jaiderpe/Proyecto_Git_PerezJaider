import json
import modules.funcionesGlobales as fg
import modules.corefiles as cf
import ui.menu.menuPrincipal as uiMenu

def main():
    fg.borrar_pantalla()
    cf.iniciarRegistroSucurrsales()
    while True:
        opcion = uiMenu()
        if opcion == 4:
            break

if __name__ == '__main__':
    main()