from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import routes
import os

app = FastAPI()

app.include_router(routes.router, prefix="/api")

static_path = os.path.join(os.path.dirname(__file__), "static")
app.mount("/", StaticFiles(directory=static_path, html=True), name="static")
