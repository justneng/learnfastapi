from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    neng = "neng"
    justneng = "justnent"
    realneng = "realneng"


app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.neng:
        return {"model_name": model_name, "greeting": "Greeting " + model_name}

@app.get("/items")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]