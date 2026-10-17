import asyncio
from database import crear_producto, obtener_producto, actualizar_stock, eliminar_producto, evaluar_stock, registrar_venta, vender_producto

async def prueba_estres():
    print("-----Iniciando prueba--------")
    tarea_ventas = [
        vender_producto("m001", 3),
        vender_producto("m002", 6),
        vender_producto("m003", 8),
        vender_producto("m004", 1)
    ]

    try: 
        await asyncio.gather(*tarea_ventas)
        print("Ventas realizadas exitosamente")
        return registrar_venta()
    except Exception as e:
        print(f"Error en la venta: {e}")

    print("\nActualizar y consultar")
asyncio.run(prueba_estres())