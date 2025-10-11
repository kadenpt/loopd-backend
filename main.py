from fastapi import FastAPI
from app import models, database
from app.routers import users, posts, follow, like

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(users.router)
app.include_router(posts.router)
app.include_router(follow.router)
app.include_router(like.router)