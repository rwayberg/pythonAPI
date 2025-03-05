from fastapi import FastAPI, status, Response
from typing import Union, Any
from pydantic import BaseModel
from pythonAPI.models.item_model import Item # type: ignore
from pythonAPI.models.item_model import test_items # type: ignore

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/items/")
def read_all_items() -> list[Item]:
    return test_items


@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(item: Item) -> Any:
    test_items.append(item)
    return {"message":"Item accepted"}