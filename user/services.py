from fastapi import APIRouter
from .schemas import UserList, UserEntry, UserUpdate, UserDelete
from typing import List
from db import databases, users
import uuid, datetime

user_router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@user_router.get('/', response_model=List[UserList])
async def find_all_users():
    query = users.select()
    return await databases.fetch_all(query)

@user_router.get("/{userId}", response_model=UserList)
async def find_user_by_id(userId: str):
    query = users.select().where(users.c.id == userId)
    return await databases.fetch_one(query)


@user_router.post("/", response_model=UserList)
async def register_user(user: UserEntry):
    gID = str(uuid.uuid1())
    gDate = str(datetime.datetime.now())
    query = users.insert().values(
        id = gID,
        username = user.username,
        password = user.password,
        first_name = user.first_name,
        last_name = user.last_name,
        gender = user.gender,
        create_at = gDate,
        status = "1"
    )

    await databases.execute(query)
    return {
        "id": gID,
        **user.dict(),
        "create_at": gDate,
        "status": "1"
    }

@user_router.put("/", response_model=UserList)
async def update_user(user: UserUpdate):
    gDate = str(datetime.datetime.now())
    query = users.update().where(users.c.id == user.id).values(
            first_name = user.first_name,
            last_name = user.last_name,
            gender = user.gender,
            status = user.status,
            create_at = gDate,
        )
    await databases.execute(query)
    return await find_user_by_id(user.id)

@user_router.delete("/{userId}")
async def delete_user(user: UserDelete):
    query = users.delete().where(users.c.id == user.id)
    await databases.execute(query)

    return {
        "status": True,
        "message": "User has been deleted"
    }