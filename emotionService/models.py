import pydantic

class Output(pydantic.BaseModel):
    prediction: str
    score: float