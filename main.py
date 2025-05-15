from fastapi import FastAPI

from models import DataItem
from service import create_item, get_all_items

app = FastAPI()

@app.post("/data")
def create_data(item: DataItem):
    return create_item(item)

@app.get("/data", response_model=list[DataItem])
def get_data():
    return get_all_items()
