from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Simulação de armazenamento em memória
fake_db = []

class DataItem(BaseModel):
    id: int
    name: str
    value: float

@app.post("/data")
def create_data(item: DataItem):
    fake_db.append(item)
    return {"message": "Item criado com sucesso", "item": item}

@app.get("/data", response_model=List[DataItem])
def get_data():
    return fake_db
