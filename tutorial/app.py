from enum import Enum

from fastapi import FastAPI

# Enum（列挙型）とstr型を継承したクラス
# strを継承することで値が文字列でなければいけなくなる
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

# インスタンスの作成【uvicorn ファイル名:インスタンス名 --reload】で立ち上げ。
# この場合【uvicorn app:app --reload】
app = FastAPI()

# item_idがパスパラメータ
# int型以外で422エラー発生「http://127.0.0.1:8000/items/15」「http://127.0.0.1:8000/items/foo」
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# "/users/me" → "/users/{user_id}"の順に記述しないといけない。
# "/users/me"があとの場合user_id＝meになってしまう。
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# Enumを実装したクラスで入力によって異なる戻り値を返す
# 引数にModelNameクラスを指定することで入力可能な値が参照できる
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    # Enumクラスのメンバーと比較
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

# ファイルパスの場合
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}