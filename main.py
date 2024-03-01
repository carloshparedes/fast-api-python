from typing import Union
from fastapi import FastAPI
import mysql.connector 
from models import bicycles

midb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "test"
)

app = FastAPI()


@app.get("/")
def read_root():
  return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
  return {"item_id": item_id, "q": q}

# Read all records

@app.get("/products")
def get_all_products():
  cursor = "product-1"
  return cursor
