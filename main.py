from fastapi import FastAPI, status, Response, HTTPException
from typing import Union, Any
from pydantic import BaseModel
from pythonAPI.models.item_model import Item # type: ignore
from pythonAPI.models.item_model import test_items # type: ignore
from pythonAPI.models.item_model import ItemUpdate # type: ignore

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int) -> Item:
   try:
        return next(x for x in test_items if x.id == item_id)
   except StopIteration:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No item found")

@app.get("/items/")
def read_all_items() -> list[Item]:
    return test_items


@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    if item.id <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item id must be greater than zero")
    if any(x.id == item.id for x in test_items):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item with that id already exists")
    test_items.append(item)
    return {"message":"Item accepted"}

@app.patch("/items/", status_code=status.HTTP_200_OK)
def accept_item(item_id: int):
    try:
        found_item = next(x for x in test_items if x.id == item_id)
        found_item.accepted = True
        return {"message": "Item updated to accepted"}
    except StopIteration:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No item found")
    
@app.post("/items", status_code=status.HTTP_202_ACCEPTED)
def update_item(update_item: ItemUpdate) -> Item:
    try:
        found_item = next(x for x in test_items if x.id == update_item.id)
        if update_item.name is not None:
            found_item.name = update_item.name
        if update_item.description is not None:
            found_item.description = update_item.description
        if update_item.price is not None:
            found_item.price = update_item.price
        return found_item
    except StopIteration:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No item found")
    
@app.delete("/items/", status_code=status.HTTP_200_OK)
def delete_item(item_id: int):
    try:
        found_item = next(x for x in test_items if x.id == item_id)
        test_items.remove(found_item)
        return {"message":"Item was removed"}
    except StopIteration:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No item found")
    
