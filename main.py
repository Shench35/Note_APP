from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.staticfiles import StaticFiles

note_list = []

app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory= BASE_DIR/"templates")


app.mount("/static",StaticFiles(directory=BASE_DIR / "static"),name="static")


@app.get('/', response_class=HTMLResponse)
def landing_page(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})

@app.post("/add-note", response_class=HTMLResponse)
def add_note(request:Request, content:str = Form(...)):
    note_list.append(content)
    return templates.TemplateResponse("index.html", {"request": request, "notes": note_list})