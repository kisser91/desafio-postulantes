from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ruts")
async def get_ruts():
    return {"ruts:": "loren ipsum"}

#############