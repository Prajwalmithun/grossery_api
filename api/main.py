from typing import Optional
from unicodedata import name
from fastapi import FastAPI
import os
from pydantic import BaseModel
import uvicorn

# Client should send in JSON
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None 
    price : float
    tax: Optional[float] = None


# create an instance
app = FastAPI()


# fake_items_db = [{"item_name":"Rice"}, 
#                   {"item_name":"Wheat"},
#                   {"item_name":"Oil"}]

# list to store all items: Item objects
items_added_by_user = []
# [
#     {
#         "id": 0,
#         "name": "sugar",
#         "description": "Makes your life sweet!",
#         "price": 40.0,
#         "tax": 2
    
#     },
#     {
#         "id": 1,
#         "name": "chilli",
#         "description": "Makes your life hot!",
#         "price": 140.0,
#         "tax": 20
#     }
# ]


# create the routes (In APIs, they are called "paths")
# Note path operations happens in same order as they are written here
@app.get("/")
@app.get("/home")
async def welcome():
    return {"message":"Hello from FastAPI"}

# @app.get("/items/{item_id}")
# async def getPathParam(item_id):
#     return {"item_id": item_id}

# @app.get("/items/10")
# async def getPathParamMan():
#     return {"item_id": "manual"}

# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]

# List all items in 
@app.get("/items/")
async def listItems():
    return items_added_by_user


# Create items
# Request Body (Client -> to us)
# 1. import BaseModel from pyndantic
@app.post("/createItem/")
def create_item(item: Item):
    items_added_by_user.append(item)
    return {"message": "Item added to the list"}

# Delete items
@app.delete("/deleteItem/{u_id}")
def delete_item(u_id: int):
    for x in items_added_by_user:
        # print(type(x['id']))
        # print(type(u_id))
        print(x)
        print(type(x.id)) # int
        print(type(x))  # datatype of this object = Item
        if x.id == u_id:
            print("inside if")
            items_added_by_user.remove(x)
    return {"message": "Item deleted"}


# Just for testing purpose
print(items_added_by_user)

if __name__ == '__main__':
    port = int(os.environ.get("PORT","8000"))
    uvicorn.run(app, host='0.0.0.0',port=port,debug=True)