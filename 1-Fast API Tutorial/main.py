from fastapi import FastAPI
from typing import Optional
# Enum => to set the type
from enum import Enum
from pydantic import BaseModel



app = FastAPI()

#############################################
## Fast API Tutorial, Part 1: Introduction
#############################################

@app.get('/api/get', description="This is Our first Route", deprecated=False , tags=['Part 1: Introduction'])
async def get_root():
    data = {
        'name' : 'Mohamed',
        'age': 20,
    }
    return data


@app.post('/api/post', tags=['Part 1: Introduction'])
async def post_root():
    data = {
        'name' : 'Mohamed',
        'age': 20,
    }
    return data

#############################################
## Fast API Tutorial, Part 2: Path Parameters
#############################################

@app.get('/api/get/{id}', tags=[' Part 2: Path Parameters'])
async def get_user_by_id(id:int):
    data = {
        'id': id,
        'name' : 'Mohamed',
        'age': 20,
    }
    return data   


class MentionEnum(str, Enum):
    AssezBien = "AssezBien"
    Bien = "Bien"
    TresBien = "TresBien"

@app.get('/get/{mention_name}', tags=[' Part 2: Path Parameters'])
def get_mention(mention_name: MentionEnum):

    if mention_name.value == "AssezBien" :
        mesg = {
            "mention_name": mention_name ,
            "message": "Une mention 'assez bien' si sa moyenne est égale ou supérieure à 12/20 et inférieure à 14/20." 
        }
        return mesg

    if mention_name.value == "Bien" :
        mesg = {
            "mention_name": mention_name ,
            "message": "Une mention Bien si sa moyenne est au moins égale à 14/20 et inférieure à 16/20." 
        }

        return mesg

    mesg = {
        "mention_name": mention_name ,
        "message": "Une mention très bien s'il obtient une moyenne égale ou supérieure à 16/20." 
    }
    return mesg


###############################################
## Fast API Tutorial, Part 3: Query Parameters
###############################################

itmes_db =[
    {
    'item_id' : 1,
    'item_name' :'Foo',
    },
    {
    'item_id' :2,
    'item_name' :'Bar',
    },
    {
    'item_id' :3,
    'item_name' :'Baz',
    }
]

@app.get('/items',tags=['Part 3: Query Parameters'])
async def get_list_items(skip:int=0, limit: int=10 ):
    data = itmes_db[skip : skip + limit]
    return data


@app.get('/items/{id}',tags=['Part 3: Query Parameters'])
async def get_list_items_by_id(id:int, q:str |None = None, short: bool = False):
    data =  {
            'item_id' :id,
            'item_name' :'Mohamed',
            }
    if q:
        data.update({'q' : q})


    if short:
        data.update({'Description' : "Vestibulum aliquam sapien vitae odio suscipit tristique quis vel neque. Nam sit amet aliquet elit."})


    return data


@app.get('/user/{user_id}/items/{items_id}',tags=['Part 3: Query Parameters'])
async def get_list_items_by_2_id(user_id:int, items_id:int, q:str |None = None, short: bool = False):
    data =  {
            'user_id': user_id,
            'item_id' : items_id ,
            'User_name' :'Mohamed',
            }
    if q:
        data.update({'q' : q})


    if short:
        data.update({'Description' : "Vestibulum aliquam sapien vitae odio suscipit tristique quis vel neque. Nam sit amet aliquet elit."})


    return data


                  
###############################################
               # POST
## Fast API Tutorial, Part 4: Request Body
###############################################

class Item(BaseModel):
    name : str
    desc : str | None = None
    price : float
    tax : float | None = None


@app.post('/post/items', tags=['Part 4: Request Body'])
async def create_item(item: Item):
    item_dict = item.dict()

    if item.tax:
        price_with_tax =  item.tax + item.price
        item_dict.update({'price_with_tax':price_with_tax})

    return item_dict


###################################################################
# Fast API Tutorial, Part 5: Query Parameters and String Validation
###################################################################