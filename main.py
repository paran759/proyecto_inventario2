import asyncio
from database import crear_producto, obtener_producto, actualizar_stock, eliminar_producto

async def prueba_estres():
    print("-----Iniciando prueba--------")
    tarea_creacion = [
        crear_producto("m001", "llanta trasera", 10),
        crear_producto("m002", "Inyectores", 50),
        crear_producto("m003", "Tornillo culata", 25)
    ]

    try: 
        await asyncio.gather(*tarea_creacion)
        print("Productos creados exitosamente")
    except Exception as e:
        print(f"Error de creacpn: {e}")

    print("\nActualizar y consultar")
    try: 
        resultado = await asyncio.gather[
            actualizar_stock (8, "M001"),
            obtener_producto ("M002")
        ]
        
        print("Operaciones mixtas completas.")
        print(f"  -  Update devolution: {resultado[0]}")
        print(f"  -  Get devolution: {resultado[1]}")
    except Exception as e:
        print("Error en operaciones mixtas.")

asyncio.run(prueba_estres())