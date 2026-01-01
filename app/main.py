print("AUTH ROUTER FILE LOADED")
from fastapi import FastAPI
from app.database import engine, Base
from app.routers import menu, auth
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cafe Management System")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(menu.router)
app.include_router(auth.router)

@app.get("/")
def home():
    return {"message": "Cafe Management System Running"}



