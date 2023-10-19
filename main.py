from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from models import Role, Item, SessionLocal

app = FastAPI()

@app.post("/roles/")
def create_role(name: str):
    role = Role(name=name)
    db = SessionLocal()
    db.add(role)
    db.commit()
    db.refresh(role)
    return role

@app.post("/items/")
def create_item(name: str, description: str):
    item = Item(name=name, description=description)
    db = SessionLocal()
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
