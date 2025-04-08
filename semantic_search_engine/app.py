from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from fastapi import FastAPI

app = FastAPI()


# Serve static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="frontend")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Single Translation
@app.get("/single_translate")
async def translate_(fromlanguage: str, tolanguage: str, text: str, model:str):
    return await translate(fromlanguage, tolanguage, text, model)

# Batch Translation
@app.post("/batch_translate")
async def translate_(input: translateInput):
    return await batch_translate(input)



if __name__ == "__main__":
    pass
