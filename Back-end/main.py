from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("users/{user_id}")
def road_user(user_id:int):
  return 























"""  basic CRUD example
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/items/")
def create_item(name: str, price: float):
    return {"name":name, "price": price}

@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, price: float):
    return {"item_id": item_id, "name": name, "price": price}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted successfully"}

""" 


""" basic pydantic eexample
class Item(BaseModel):
    name: str
    price: float


@app.post("/items1/")
def create_try(item: Item):
    return {"Name":item.name, "price":item.price}
"""