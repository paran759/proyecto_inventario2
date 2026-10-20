from fastapi import FastAPI,HTTPException
from database import obtener_producto, leer_base_datos, guardar_base_datos 

app = FastAPI(
    title = "inventario Juan Carlos",
    description="API asincrona",
    version= "1.0.0"
)

@app.get("/")
async def ruta_principal():
    return {"mensaje": "Bienvenido a nuestra primera API"}

@app.get("/estado")
async def estado_servido():
    return {"status": "En linea", "servicios": "Operativos"}

@app.get("/suma")
async def suma_en_servidor():
    num1 = 50
    num2 = 25
    suma = num1 + num2
    return {"numero1": num1, "+" "numero2": num2, "=": suma}

@app.get("/producto/{codigo_producto}")
async def buscar_un_producto(codigo_producto: str):
    try:
        producto = await obtener_producto(codigo_producto)
        return producto
    except KeyError:
        raise HTTPException(status_code=404, detail="el producto solicitado no existe en la bas de datos")

@app.get("/productos")
async def listar_productos():
    datos = await leer_base_datos()
    return {"cantidad": len(datos), "productos": datos}

@app.get("/leer_categoria")
async def leer_categoria():
    try:
        datos = await leer_base_datos()
        categorias_unicas = set()

        for dato in datos:
            categoria_duplicada = dato.get("categoria")
            if categoria_duplicada:
                categorias_unicas.add(categoria_duplicada)

        return {"categorias": categorias_unicas}
    except Exception as e:
        return {"Error interno": str(e)}

@app.get("/atertas/stock")
async def stock_critico():
    try:
        datos = leer_base_datos()
        criticos = set()

        for dato in datos:
            productos_criticos = dato.get("stock")
            if productos_criticos <= 3:
                criticos.add(productos_criticos)

        return {"Productos criticos ": criticos}
    except Exception as e:
        return {"Error en bodega": e}
