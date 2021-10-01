# war-game

## How to build

`docker-compose build`

## How to run db

`docker-compose up`

## Run Migrations

```
alembic revision --autogenerate -m "first commit"
alembic upgrade head
```
