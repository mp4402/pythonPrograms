#importacion de librerias
from fastapi import FastAPI
from enum import Enum
from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

#declaracion de variable
app = FastAPI()

description = {"resnet": "you selected resnet model",
               "alexnet": "you selected alexnet model",
               "lenet": "you selected lenet model"}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class ModelName(str, Enum):
    resnet="resnet"
    alexnet="alexnet"
    lenet="lenet"

#declaracion de metodos
@app.get("/")
async def root():
    return {"message": "Hello World"}

#declaracion de variables dentro del path
#@app.get("/items/{item_id}")
#async def read_item(item_id):
#    return {"item_id":item_id}

#declaracion de variables dentro del path, pero con rigideza de tipos
@app.get("/items_strict/{item_id}")
async def read_items(item_id:int):
    return {"item_id":item_id}

@app.get("/users/me")
async def read_user_me():
    return{"user_id":"the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id:str):
    return{"user_id":user_id}

@app.get("/models/{model_name}")
async def  get_model_data(model_name: ModelName):
    return {"model" : model_name, "description" : description[model_name]}

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.post("/items/")
async def create_item(item: Item):
    if not item.tax:
        item.tax = item.price * 0.11
    return item

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}