from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
import secrets
import json

json_path = "notes.json"

notes = {}

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="JESUS_IS_LORD"+secrets.token_hex(16))

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory= BASE_DIR/"templates")


app.mount("/static",StaticFiles(directory=BASE_DIR / "static"),name="static")


@app.get('/', response_class=HTMLResponse)
def landing_page(request: Request):
    if "user_id" not in request.session:
        request.session["user_id"] = secrets.token_hex(16)
    user_id = request.session["user_id"]
    with open (file=json_path, mode="r") as f:
        notes_data = json.load(f)
    
    return templates.TemplateResponse("index.html",{"request": request , "notes": notes_data.get(user_id, [])})


@app.post("/add-note", response_class=HTMLResponse)
def add_note(request:Request, content:str = Form(...)):
    user_id = request.session.get("user_id")
    if not user_id:
        user_id = secrets.token_hex(16)
    if user_id not in notes:
        notes[user_id] = []
    
    notes[user_id].append(content)

    with open (file=json_path, mode="w") as f:
        json.dump(notes, f, indent=4)
        
    with open (file=json_path, mode="r") as f:
        notes_data = json.load(f)
    return RedirectResponse(url="/", status_code=303)