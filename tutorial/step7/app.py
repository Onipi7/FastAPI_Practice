# ボディ - フィールド
from typing import Union

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field   # Fieldは（Query・Body・Path）とは違いpydanticなことに注意

app = FastAPI()

# Queryと同様にFieldでバリデーションやメタデータを追加できる
class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results