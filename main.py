from typing import Union, Optional
from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from database.db import connect, sponsored, Client
from dependencies.get_db import get_db
from schemas.models import ClientModel

app = FastAPI()


###########
## GET
###########


@app.get("/api/get/clients")
async def get_all_clients(db: Session = Depends(get_db)):
    data = db.query(Client).all()
    return data



@app.get("/api/get/client/{id}", status_code=status.HTTP_200_OK)
async def get_client_by_id(id:int, res : Response):
    client = sponsored.query(Client).filter(Client.id == id).first()
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"We not Found Client with id= {id}")
    return client


###########
## POST
###########

@app.post("/api/post/client", status_code=status.HTTP_201_CREATED)
def new_client(client: ClientModel , db: Session = Depends(get_db)):
    new_client = Client(id = client.id, client_name = client.client_name, post_url = client.post_url, price=client.price, days_number = client.days_number, is_finished = client.is_finished)
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return client


###########
## DELETE
###########

@app.delete('/api/delete/client/{id}', status_code=status.HTTP_200_OK)
def remove_client(id : int, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == id)
    if not client.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"We not Found Client with id= {id}")
    
    client.delete()
    db.commit()
    return {"Msg" : "Done!"}



###########
## PUT
###########

@app.put("/api/put/client", status_code=status.HTTP_201_CREATED)
def new_client(client: ClientModel , db: Session = Depends(get_db)):
    new_client = Client(id = client.id, client_name = client.client_name, post_url = client.post_url, price=client.price, days_number = client.days_number, is_finished = client.is_finished)
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return client
