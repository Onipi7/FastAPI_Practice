# パスパラメータと数値の検証
from typing import Union

from fastapi import FastAPI, Path, Query

app = FastAPI()


# Pathではパスパラメータは必須入力
@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(title="The ID of the item to get"),
    q: Union[str, None] = Query(default=None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# パラメータを並び替えることができる
@app.get("/items1/{item_id}")
async def read_items(q: str, item_id: int = Path(title="The ID of the item to get")):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# 最初の引数が"*"だとそれ以降のパラメータの順番を入れ替えられる
@app.get("/items2/{item_id}")
async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# 数値のチェック"ge=1"だと1以上の値（Grater Eqoual）
# 以下は"le"で指定
@app.get("/items/{item_id}")
async def read_items(
    *, item_id: int = Path(title="The ID of the item to get", ge=1), q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results