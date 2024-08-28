# main.py
from fastapi import HTTPException, FastAPI
from pydantic import BaseModel
from UserManager.models.usermanager import User
from mongoDb.mon import MongoDBService
import uvicorn

app = FastAPI()
db_service = MongoDBService("mongodb://localhost:27017", "PokemonUsers")


class UserModel(BaseModel):
    user_id: str
    full_name: str
    phone: str
    email: str


@app.post("/users/")
def create_user(user: UserModel):
    user_obj = User(**user.dict())  # convert UserModel to User
    db_service.insert_user(user_obj)
    return {"msg": "User created"}


@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    db_service.delete_user(user_id)
    return {"msg": "user deleted"}


@app.get("/users/{user_id}")
def get_user(user_id: str):
    user = db_service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="user Not found!")
    return user


@app.put("/users/{user_id}")
def update_user(user_id: str, user: UserModel):
    user_data = user.dict(exclude={"user_id"})
    user_obj = User(user_id=user_id, **user_data)
    try:
        db_service.update_user(user_obj)
        return {"msg": f"User updated: {user.full_name}"}
    except HTTPException as e:
        raise e
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))


@app.get("/users/")
def get_all_users():
    users = db_service.get_all_users()
    return users


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
