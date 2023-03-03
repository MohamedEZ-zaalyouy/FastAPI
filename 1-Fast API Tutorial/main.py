from fastapi import FastAPI

app = FastAPI()

#######
## GET
#######

@app.get('/api/get', description="This is Our first Route", deprecated=True)
async def get_root():
    data = {
        'name' : 'Mohamed',
        'age': 20,
    }
    return data


#######
## POST
#######

@app.post('/api/post')
async def post_root():
    data = {
        'name' : 'Mohamed',
        'age': 20,
    }
    return data