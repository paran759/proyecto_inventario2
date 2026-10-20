import json
import aiofiles
import asyncio

ARCHIVO_BD = "Inventario.json"
db_lock = asyncio.Lock

async def leer_base_datos():
    try:
        async with aiofiles.open(ARCHIVO_BD, mode="r", encoding="utf-8" ) as f:
            contenido = await f.read()
            return json.loads(contenido)
    except FileNotFoundError:
        return [] # lista vacia

async def guardar_base_datos(datos):
    async with aiofiles.open(ARCHIVO_BD, node="w", encoding="ytf-8") as f:
        await f.write(json.dumps(datos, indent=4))

async def crear_producto(codigo, nombre, stock):# la info dentro del () son parametros
    async with db_lock:

        await asyncio.sleep(0.5)
        datos = await leer_base_datos()

        for dato in datos:
            if dato["codigo"] == codigo:
                raise ValueError(f"El producto con el codigo {codigo} ya existe.")
            
        nuevo_producto = {"codigo": codigo, "nombre": nombre, "stock": stock}
        datos.append(nuevo_producto)# agregar a los datos que ya existen el nuevo producto
        await guardar_base_datos(datos)
        return nuevo_producto

async def obtener_producto(codigo):
    async with db_lock:

        await asyncio.sleep(0.2)
        datos = leer_base_datos()

        for dato in datos:
            if dato["codigo"] == codigo:
                return dato
            raise KeyError(f"Producto {codigo} no a sido encontrado.")

async def actualizar_stock(nuevo_stock, codigo):
    async with db_lock:

        await asyncio.sleep(0.5)
        datos = leer_base_datos()

        for dato in datos:
            if dato["codigo"] == codigo:
                dato["stock"] = nuevo_stock
                await guardar_base_datos(datos)
                return dato

async def eliminar_producto(codigo):
    async with db_lock:

        await asyncio.sleep(0.5)
        datos = leer_base_datos

        nuevos_datos = [dato for dato in datos if datos[dato["codigo"] != codigo]]

        if len(datos) == len(nuevos_datos):
            raise KeyError(f"Hubo un error en la busqueda del producto del codigo {codigo}")

        await guardar_base_datos(nuevos_datos)
        return True

async def vender_producto(codigo, cantidad_vendida):
    async with db_lock:

        await asyncio.sleep(0.5)
        datos = leer_base_datos()

        for dato in datos:
            if dato["codigo"] != codigo:
                raise KeyError("Producto no encontrado")
            elif dato["stock"] > cantidad_vendida:
                raise ValueError("Stock insuficiente")

            nuevo_stock = dato["stock"] - cantidad_vendida
            await guardar_base_datos(nuevo_stock)
            return True

async def evaluar_stock():
    async with db_lock:

        await asyncio.sleep(0.7)
        datos = leer_base_datos()

        determinante = asyncio.create_task(dato for dato in datos if datos[stock] <= 3)

        if determinante == True:
            print("Precuaicion: Cantidad del producto en almacen muy baja ")

async def registrar_venta():
    async with db_lock:

        await asyncio.sleep(0.3)
        datos = leer_base_datos()
        cantidad_vender = vender_producto[cantidad_vendida]

        resumen_venta = {
            "estado": "exitoso",
            "producto": datos[nombre],
            "cantidad": cantidad_vender,
            "bodega": datos[stock]
        }
        return resumen_venta

    
    