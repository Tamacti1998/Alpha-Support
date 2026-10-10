from fastapi import FastAPI
from pydantic import BaseModel
import json
from pathlib import Path

app = FastAPI()
FILE_PATH = Path("users.json")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/wahab")
def read_root():
    return {"Hello": "Wahab"}

@app.get("/Alhassan") # Get - to retrieve data
def user():
    firsName = "Alhassan"
    lastName = "Awal"
    
    return {"firstName": firsName, "lastName": lastName}


# POST REQUEST FOR SHOP ITEM DETAILS
class item(BaseModel):
    name : str
    price : int
    quantity : int

@app.post("/Alhassan") # Post - to create data
def create_shop_itemn(client: item):
    return {
        "name" : client.name,
        "price" : client.price,
        "quantity" : client.quantity
    }

# POST REQUEST FOR CAR DETAILS
class car(BaseModel):
    brand_name : str
    cost : int
    model : str
    mileage : int

@app.post("/Car")
def create_car(buyer: car):
    return {
        "brand_name" : buyer.brand_name,
        "cost" : buyer.cost,
        "model" : buyer.model,
        "mileage" : buyer.mileage
    }


# Submitting data to a JSON file


class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    # Read existing users, or start with an empty list
    if FILE_PATH.exists():
        with FILE_PATH.open("r", encoding="utf-8") as file:
            users = json.load(file)
    else:
        users = []

    # Add the new user
    users.append(user.model_dump())

    # Save all users back to the file
    with FILE_PATH.open("w", encoding="utf-8") as file:
        json.dump(users, file, indent=4) # dump() write JSON data to a file

    return {
        "message": "User saved successfully",
        "user": user
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}