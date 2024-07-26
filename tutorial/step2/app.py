from fastapi import FastAPI

from typing import Union

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# クエリパラメータ　step1に登場した"/items/{item_id}"はパスパラメータ
# "http://127.0.0.1:8000/items/?skip=0&limit=10"のように値の受け渡しができる
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# Union[str, None]はstr型でもNoneにマッチすればOK
# "q: Union[str, None] = None"で実装することでqがない場合に対応できる。
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item