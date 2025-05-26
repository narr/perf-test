# main.py
from fastapi import FastAPI
import uvicorn

# import time
import asyncio

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "message": f"This is item {item_id}"}


@app.get("/delay/{seconds}")
async def delay_response(seconds: int):
    """
    지정된 초만큼 응답을 지연시키는 엔드포인트
    """
    # time.sleep(seconds)
    await asyncio.sleep(seconds)
    return {"message": f"Delayed for {seconds} seconds"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
