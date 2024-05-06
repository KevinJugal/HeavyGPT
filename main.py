from fastapi import FastAPI
from pydantic import BaseModel
from utils import generate_description
app = FastAPI()

class Order(BaseModel):
    item: str
    units: int

class Product(BaseModel):
    name: str
    notes: str
@app.get("/ok")
async def ok_endpoint():
    return {"message": "OK"} 

@app.get("/hello")
async def hello_endpoint(name: str = 'world'):
    return {"message":f"Hello,{name}!"}

@app.post("/orders")
async def orders_place(item: str, units: int):
    return {"message": f"Order for {units} of {item} placed successfully"}

@app.post("/orders_pydantic")
async def orders_place(order: Order):
    return {"message": f"Order for {order.units} of {order.item} placed successfully"}




