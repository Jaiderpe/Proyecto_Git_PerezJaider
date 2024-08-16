import json
import modules.movesJson as mj

DATABASE_SUCURSALES = 'data/sucursales.json'
DATABASE_INVENTARIO = 'data/compras.json'

def iniciarRegistroSucurrsales():
    mj.checkfile(DATABASE_SUCURSALES, {"sucursales": []})
    mj.checkfile(DATABASE_INVENTARIO, {"inventario": []})