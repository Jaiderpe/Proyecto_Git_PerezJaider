import json

def gestionInventario():

    with open('data/sucursales.json', 'r') as file:
                data = json.load(file)

    ventas = data.get('sucursales', {})
    total_ingresos = 0

    print(f"Informe de Ventas desde {fecha_inicio_str} hasta {fecha_fin_str}:")
    for transaccion in ventas:
        fecha_transaccion = datetime.strptime(transaccion['Fecha de la transacción'], '%Y-%m-%d')
        if fecha_inicio <= fecha_transaccion <= fecha_fin:
            print(f"Fecha: {transaccion['Fecha de la transacción']}")
            print(f"Cliente: {transaccion['Nombre del cliente']}")
            print(f"Dirección: {transaccion['Dirección del cliente']}")
            print(f"Empleado: {transaccion['Empleado']}")
            print(f"Cargo: {transaccion['Cargo']}")
            print("Productos vendidos:")
            for producto in transaccion['Productos']:
                print(f"  Producto: {producto['Producto']}, Cantidad: {producto['Cantidad']}, Precio: {producto['Precio']}")
                total_ingresos += float(producto['Precio']) * float(producto['Cantidad'])
            print()