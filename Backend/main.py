from fastapi import FastAPI
from pydantic import BaseModel
import json
from pathlib import Path

app = FastAPI()

FILE_PATH = Path("users.json")
data_path = Path("phones.json")


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

class phone(BaseModel):
    id : int
    brand : str
    model : str
    operating_system : str
    price : int
    color : str

class users_phone(BaseModel):
    id : int | None = None
    brand : str | None = None
    model : str | None = None
    operating_system : str | None = None
    price : int | None = None
    color : str | None = None

@app.post("/post_phones")
def mobile(p_type : phone):
    if data_path.exists():
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []

    new_data = p_type.model_dump()
    data.append(new_data)

    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)   

    return {
        "text" : "Phone info saved successfully",
        "data" : new_data
    }

# PUT Request - basically used to update exisiting data/field or replace it with new data.
@app.put("/update_phones/{id}")
def mobile(p_type : phone, id : int):
    if data_path.exists():
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []

    updated_data = p_type.model_dump()

    for idx, item in enumerate(data):
        if item["id"] == id:
            data[idx] = updated_data

            with open(data_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent = 4)

            return {
                "text" : "Phone info updated successfully",
                "data" : updated_data
            }
        
    return {
        "text" : "Phone info not found"
    }

#PATCH Request - allows to update specific field of an existing data
@app.patch("/patch_phones/{id}")
def mobile(p_type : users_phone, id : int):
    if data_path.exists():
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []

    updated_data = p_type.model_dump(exclude_unset=True)

    for idx, item in enumerate(data):
        if item["id"] == id:
            data[idx].update(updated_data)

            with open(data_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent = 4)

            return {
                "text" : "Phone info updated successfully",
                "data" : data[idx]
            }
        
    return {
        "text" : "Phone info not found"
    }

@app.delete("/delete_phones/{id}")
def mobile(id : int):
    if data_path.exists():
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []

    for idx, item in enumerate(data):
        if item["id"] == id:
            deleted_data = data.pop(idx)

            with open(data_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent = 4)

            return {
                "text" : "Phone info deleted successfully",
                "data" : deleted_data
            }
        
    return {
        "text" : "Phone info not found"
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}