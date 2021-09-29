import uvicorn
from fastapi import FastAPI
import os
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from sqlalchemy.sql.expression import func
from models import User as ModelUser
from schema import User as SchemaUser
from dotenv import load_dotenv
import bcrypt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@app.post("/user/", response_model=SchemaUser)
def create_user(user: SchemaUser):

    hashed = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())

    db_user = ModelUser(
        username=user.username, password=hashed, record=user.record
    )
    db.session.add(db_user)
    db.session.commit()
    return db_user


@app.get("/users/")
def get_users():
    return db.session.query(ModelUser.username, ModelUser.record).all()


@app.get("/war/")
def start_war():
    player1, player2 = db.session.query(
        ModelUser.id, ModelUser.username, ModelUser.record).order_by(func.random()).offset(0).limit(2).all()
    return f"War has started with {player1.username} and {player2.username}!"


@app.get("/")
def home():
    return {
        "message": "Welcome to war!"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
