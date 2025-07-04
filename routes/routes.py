from fastapi import APIRouter
from config.config import fastapiCollection
from serializer.serializer import convertfastapi, convertfastapis
from bson import ObjectId
endPoints = APIRouter()

@endPoints.get('/')
def home():
    return {
        "Status" : "Ok",
        "Message": "My first api is run"
    }

# create a new user
@endPoints.post('/users')
def create_user(fastapi: dict):
    fastapiCollection.insert_one(fastapi)
    return {
        "Status": "Ok",
        "Message": "User created successfully",
        "Data": convertfastapi(fastapi)
    }

# get all users
@endPoints.get('/users')
def get_all_users():
    fastapis = fastapiCollection.find()
    converted_users = convertfastapis(fastapis)  # ✅ renamed variable
    return {
        "Status": "Ok",
        "Message": "All users fetched successfully",
        "Data": converted_users
    }

# get a user by id
@endPoints.get('/users/{id}')
def get_user_by_id(id: str):
    fastapi = fastapiCollection.find_one({"_id": ObjectId(id)})
    converted_fastapi = convertfastapi(fastapi)
    return {
        "Status": "Ok",
        "Message": "User fetched successfully",
        "Data": convertfastapi(fastapi)
    }


# update a user by id
@endPoints.put('/users/{id}')
def update_user(id: str, fastapi: dict):
    fastapiCollection.update_one({"_id": ObjectId(id)}, {"$set": fastapi})
    updated_fastapi = fastapiCollection.find_one({"_id": ObjectId(id)})
    return {
        "Status": "Ok",
        "Message": "User updated successfully",
        "Data": convertfastapi(updated_fastapi)
    }

# delete a user by id
@endPoints.delete('/users/{id}')
def delete_user(id: str):      
    fastapiCollection.delete_one({"_id": ObjectId(id)})
    return {
        "Status": "Ok",
        "Message": "User deleted successfully"
    }