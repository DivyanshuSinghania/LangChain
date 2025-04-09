# system libraries
from Functions.Summary import pdf_summary

# FastAPI imports
from fastapi import FastAPI, File, Form, UploadFile, Depends

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request


# Initialize FastAPI App
app = FastAPI()


# Serve static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



# PDF Summary
@app.post("/pdf_summary")
async def PDF_summary(
    file: UploadFile = File(...),
    ):
    try:
        summary = await pdf_summary(file)
        return {"summary" : summary.content}
    except Exception as e:
        return {"error": f"Failed to process PDF: {str(e)}"}
    