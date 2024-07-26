from fastapi import FastAPI
import json

app = FastAPI()

# data.json からデータを読み込む
with open("data.json", "r") as f:
    data = json.load(f)

@app.get("/users")
def get_users():
    return data["users"]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
