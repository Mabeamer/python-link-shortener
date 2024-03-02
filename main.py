import secrets
import validators
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session


from . import models, schemas
from .database import SessionLocal, engine

def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)


app = FastAPI()
models.base.metadata.crate_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return "Welcome to the URL shortener API"

@app.post("/url", response_model=schemas.URLInfo)
def create_url(url: schemas.URLBase, db: Session = Depends(get_db)):
    if not validators.url(url.target_url):
        raise_bad_request(message="provided url is not valid")

#??
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "".join(secrets.choice(chars) for _ in range(5))
    secret_key = "".join(secrets.choice(chars) for _ in range(8))
    db_url = models.URL(
        target_url=url.target_url, key=key, secret_key=secret_key
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    db_url.url = key
    db_url.admin_url = secret_key
    #?
    #return f"TODO: CREATE DATABASE ENTERY FOR: {url.target_url}"
    return db_url
