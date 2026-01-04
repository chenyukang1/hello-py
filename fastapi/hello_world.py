from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

items=[]

@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.post('/item')
def add_item(item: Item):
    print(f'Add {item}')
    items.append(item)
    return "success"
