from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def devherozone():
    return{"Django":"API"}

@app.get("/home")
def home():
    return{"course":"Django & Backend API development with python"}