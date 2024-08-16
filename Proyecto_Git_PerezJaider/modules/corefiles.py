import json
import modules.movesJson as mj

DATABASE_SUCURSAL = 'Proyecto_Git_PerezJaider\data\sucursales.json'


def iniciarRegistroDataSucursales():
    mj.checkfile(DATABASE_SUCURSAL, {"sucursales": {}})
    