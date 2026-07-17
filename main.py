from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def devherozone():
    return{"Django":"API"}