from typing import Union

from fastapi import FastAPI, HTTPException
from src.core.boundery import get_item
from .application import app
from .error_handlers import storage_error_handler


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return get_item(item_id)

