from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from use import use_model

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/emotion/{text}")
def emotion(text: str):
    return use_model(text)
