import uvicorn
import os
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from sqlalchemy.sql.expression import func
from models import User as ModelUser
from schema import User as SchemaUser
from dotenv import load_dotenv
import bcrypt
from war import war

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()


app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


# @app.delete('/users/')
@app.post("/user/", response_model=SchemaUser)
def create_user(user: SchemaUser):

    hashed = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())

    db_user = ModelUser(
        username=user.username, password=hashed, wins=user.wins
    )
    db.session.add(db_user)
    db.session.commit()
    return db_user


@app.get("/users/")
def get_users():
    return db.session.query(ModelUser.id, ModelUser.username, ModelUser.wins).all()


@app.get("/war/")
def start_war():
    # grad two random players in the db
    player1, player2 = db.session.query(
        ModelUser.id, ModelUser.username, ModelUser.wins).order_by(func.random()).offset(0).limit(2).all()

    # play war! unpack the winner, total rounds, and the loser from the match
    (winner, total_rounds, loser) = war(player1, player2)

    # update the wins column in the db for the winner
    updateWinner = db.session.query(ModelUser).filter(
        ModelUser.id == winner.id).first()
    updateWinner.wins += 1
    db.session.commit()
    db.session.refresh(updateWinner)

    return f"{winner.username} beat {loser.username} in {total_rounds} rounds!"


@app.get('/seed/')
def seed():
    sql = """
    INSERT INTO users (id, username, password, wins) VALUES
    (
        1,
        'sung',
        '123',
        0
    ),
    (
        2,
        'bob',
        '123',
        0,
    ),
    (
        3,
        'nancy',
        '123',
        0
    ),
    (
        4,
        'robert',
        '123',
        0
    );
    """
    db.session.execute(sql)
    db.session.commit()
    return {
        "message": "db was seeded!"
    }


@app.get("/")
def home():
    return {
        "message": "Welcome to war!"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
