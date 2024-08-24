
from fastapi import HTTPException, FastAPI
from pydantic import BaseModel
from models.user import User
from PokeGame.Backend.mongoDb.mon import MongoDBService

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

