from fastapi import FastAPI
from pydantic import BaseModel
class HelloRequest(BaseModel):
    name: str


app = FastAPI()


@app.get("/api/hello")
def hello(name: str = "World") -> dict:
    return {"message": f"Hello, {name}!"}


@app.post("/api/helloUser")
def hello_user(request: HelloRequest) -> dict:
    return {"message": f"Hello, {request.name}!"}