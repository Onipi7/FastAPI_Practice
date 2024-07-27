# クエリパラメータと文字列の検証
from typing import Union, List

from fastapi import FastAPI, Query

app = FastAPI()

# "Query(default=None, max_length=50"で50文字以下であることを強制
# default=Noneは必須パラメータではないことを明示。必須の場合defaultを宣言しない。
@app.get("/items/")
async def read_items(q: Union[str, None] = Query(default=None, min_length=3, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# 正規表現も扱える
@app.get("/items2/")
async def read_items(
    q: Union[str, None] = Query(
        default="fixedquery", min_length=3, max_length=50, pattern="^fixedquery$"
    ),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# クエリパラメータのリスト / 複数の値
# http://localhost:8000/items3/?q=foo&q=bar
# = Query(default=Noneがなければリクエストボディと解釈される
@app.get("/items3/")
async def read_items(q: Union[List[str], None] = Query(default=["foo", "bar"])):
    query_items = {"q": q}
    return query_items


# title・discriptionなども追加できるdocsで確認！
@app.get("/items4/")
async def read_items(
    q: Union[str, None] = Query(
        default=None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    ),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results