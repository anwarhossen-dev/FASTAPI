from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

#define requst body schema
class Course(BaseModel):
    name: str
    instructor:str
    duration: float
    website: HttpUrl

    @app.post("/post")
    def create_post(Post:Course):
        return{"data": Post}

@app.get("/")
def devherozone():
    return{"Django":"API"}

@app.get("/home")
def home():
    return{"course":"Django & Backend API development with python"}

@app.get("/django/api")
def home():
    return{"Type":"Django basic to advanced"}