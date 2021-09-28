from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str = None
    record: int

    class Config:
        orm_mode = True
