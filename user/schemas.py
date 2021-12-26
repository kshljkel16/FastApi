from pydantic import BaseModel, Field


class UserList(BaseModel):
    id: str
    username: str
    password: str
    first_name: str
    last_name: str
    gender: str
    create_at: str
    status: str

class UserEntry(BaseModel):
    username: str = Field(..., example="test")
    password: str = Field(..., example="test1212")
    first_name: str = Field(..., example="test")
    last_name: str = Field(..., example="test")
    gender: str = Field(..., example="F")

class UserUpdate(BaseModel):
    id: str = Field(..., example="Enter your id")
    first_name: str = Field(..., example="test")
    last_name: str = Field(..., example="test")
    gender: str = Field(..., example="F")
    status: str = Field(..., example="1")

class UserDelete(BaseModel):
    id: str = Field(..., example="Enter your id")