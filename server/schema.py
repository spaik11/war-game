from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str = None
    wins: int

    class Config:
        orm_mode = True
