from fastapi import FastAPI  ## step-1 lIne(1-16)
from app.db import SessionLocal


app=FastAPI(
    title ="Electronic Ecommerce Project",
    description="Backend API for an electronics e-commerce platform",
    version="1.0.0"

)

@app.get("/")
def home():
    return{
        "message":"Welcome to the Electronic Ecommerce Project API"
    }