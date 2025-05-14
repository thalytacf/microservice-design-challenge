from pydantic import BaseModel, Extra


class DataItem(BaseModel):
    id: int
    name: str
    value: float


    class Config:
        extra = Extra.forbid
