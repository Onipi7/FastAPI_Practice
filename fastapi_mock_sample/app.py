from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

# Pydanticモデルの作成
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int

# data.json からデータを読み込む
with open("data.json", "r") as f:
    data = json.load(f)
    users = [User(**user) for user in data["users"]]

@app.get("/users")
def get_users():
    return users

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
