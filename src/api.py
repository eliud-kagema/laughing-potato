from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def hello_world():
    return {"hello": "world"}



@app.get("/users/{id}")
async def get_user(id: int):
    return {"id": id}