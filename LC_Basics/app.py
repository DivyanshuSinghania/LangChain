from Functions.helper_LC import translate, batch_translate
from typeModels.models import translateInput
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# Single Translation
@app.get("/single_translate")
async def translate_(fromlanguage: str, tolanguage: str, text: str, model:str):
    return await translate(fromlanguage, tolanguage, text, model)

# Batch Translation
@app.get("/batch_translate")
async def translate_(input: translateInput):
    return await batch_translate(input)



if __name__ == "__main__":
    pass
