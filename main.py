from user.services import user_router
from fastapi import FastAPI
from db import metadata, databases, engine


metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await databases.connect()

@app.on_event("shutdown")
async def shutdown():
    await databases.disconnect()

app.include_router(user_router)

