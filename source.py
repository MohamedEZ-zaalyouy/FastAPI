from typing import Union, Optional
from fastapi import FastAPI
from schemas.models import User
from database.db import *

app = FastAPI()


###########
## GET
###########


@app.get("/app/root")
def read_root():
    return {"Hello": "World"}



@app.get("/app/user")
def get_user(): 
    data ={
        'id' :125487963,
        'First Name': 'Mohamed',
        'Last Name': 'EZ-ZAALYOUY',
        'AGE': 24,
        'skills' : ['Django','Python','FsatAPI'],
        'status' : True,
    }
    return data



@app.get("/app/user/{id}&{status}")
def get_user_id(id:int , status:bool , age:Optional[int]= None):
    if  status == True:        
        data = {
        'id':id,
        'status':status,
        'username': 'Mohamed',
        "age": age
        }
    else:
        data = {
             'error status': "Sorry your status is not True",
        }
        
    return data


###########
## POST
###########

@app.post("/post/users")
def users(user : Client):
    data = user
    return data