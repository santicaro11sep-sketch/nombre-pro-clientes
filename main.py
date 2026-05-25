from fastapi import FastAPI


app = FastAPI()
@app.get("/")
def cliente():
    return {"mensaje":"Este es el proyecto de clientes a desarollar"}

@app.get("/clientes")
def lista_clientes():
    lista = ["cliente1","cliente2","cliente3","cliente4","cliente5"]
    return [lista]

