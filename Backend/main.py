from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/wahab")
def read_root():
    return {"Hello": "Wahab"}

@app.get("/Alhassan")
def user():
    return "Hello Alhassan!"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}