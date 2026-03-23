from fastapi import FastAPI

apps = FastAPI()


@apps.get("/")
def read_root():
    return {"Hello": "World"}

