from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from use import predict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/nationality/{surname}")
def get_nationality_by_surname(surname: str):
    return predict(surname)
