from pydantic import BaseModel


class User(BaseModel):
    id : int
    username : str
    age : int
    skills : list[str] = []
    description: str | None = None
    status : bool


#Create Table Client
class ClientModel(BaseModel): 
    id : int
    client_name : str
    post_url : str
    price : float
    days_number : int
    is_finished : bool