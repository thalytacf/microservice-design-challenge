from models import DataItem


_fake_db: list[DataItem] = []

def create_item(item: DataItem) -> dict:
    _fake_db.append(item)
    return {"message": "Item criado com sucesso", "item": item}

def get_all_items() -> list[DataItem]:
    return _fake_db

def reset_db():
    _fake_db.clear() 
