from fastapi import FastAPI,HTTPException
from database import obtener_producto

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