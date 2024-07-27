from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


# pydanticのBaseModelを継承
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

app = FastAPI()

# リクエストボディ
# 引数にItemクラスを指定しておくことでdocsで対話的に確認できる
@app.post("/items/")
async def create_item(item: Item):
    return item


# リクエストボディ＋パスパラメータ＋クエリパラメータ
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

# resultの形式
# {item_id: {
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None}
# }