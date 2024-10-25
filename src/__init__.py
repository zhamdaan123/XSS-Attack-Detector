import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from dotenv import load_dotenv

from src.middlewares.logger import Logger
from src.api import api
from src.demo import demo

load_dotenv()

app = FastAPI(title="XSS Attack Detector",
            description="Cross-Site Scripting Attack Detection and Prevention",
            docs_url='/api')

app.add_middleware(SessionMiddleware, secret_key=os.environ.get("SECRET_KEY"))
app.add_middleware(CORSMiddleware,
                allow_origins=["*"],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"])
app.add_middleware(Logger)

app.include_router(api)
app.include_router(demo)
app.mount("/static", StaticFiles(directory="src/static"), name="static")
app.mount("/", StaticFiles(directory="src/views", html=True), name="views")
