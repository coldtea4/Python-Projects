from fastapi import FastAPI

app = FastAPI()

@app.get("/pasta")
async def root():
    return {"message": "Gnocchi"}

@app.get("/pizza")
async def root():
    return {"message": "Grandma"}

@app.get("/number_crunch")
async def root():
    num = 9 + 10
    return {"message": num + 2}