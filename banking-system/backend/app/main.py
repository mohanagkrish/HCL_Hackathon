from fastapi import FastAPI
from app.database import Base, engine
from app.controllers import account_controller

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Banking System - Account Creation API",
    version="1.0.0",
    description="API for creating new accounts in the Banking System"
)

app.include_router(account_controller.router)

@app.get("/")
def root():
    return {"message": "Welcome to Banking System API 🚀"}
