from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
import secrets
import json
import os 
from dotenv import load_dotenv
from pydantic import BaseModel


class Note(BaseModel):
    content: str

load_dotenv()
secret_key = os.getenv("SECRET_KEY") 
json_path = "notes.json"

note_counter = 0

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key= secret_key, max_age=315360000)

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
    global note_counter
    user_id = request.session.get("user_id")
    if not user_id:
        user_id = secrets.token_hex(16)

    with open (file=json_path, mode="r") as f:
        note_data = json.load(f)
    if user_id not in note_data:
        note_data[user_id] = []
    
    note_counter += 1
    new_note = {
        "id": note_counter,
        "content": content
    }
    
    note_data[user_id].append(new_note)

    with open (file=json_path, mode="w") as f:
        json.dump(note_data, f, indent=4)
        
    return RedirectResponse(url="/", status_code=303)

@app.get("/edit-note/{note_id}", response_class=HTMLResponse)
def edit_note(request:Request, note_id:int):
    user_id = request.session.get("user_id", [])

    with open(file=json_path,mode="r") as f :
        notes_data = json.load(f)

    user_note = notes_data.get(user_id,[])
    print(user_note)
    for i in user_note:
        id = i.get("id")
        if id == note_id:
            print(i.get("content"))
            return templates.TemplateResponse("edit.html",{"request": request ,"note_id": note_id, "note_content": i.get("content")})

@app.post("/edit-note", response_class=HTMLResponse)
def update_note(request: Request, note_id: int = Form(...), content: str = Form(...)):
    user_id = request.session.get("user_id")

    with open(file=json_path, mode="r") as f:
        notes_data = json.load(f)

    user_notes = notes_data.get(user_id, [])

    for note in user_notes:
        if note["id"] == note_id:
            note["content"] = content
            break

    with open(file=json_path, mode="w") as f:
        json.dump(notes_data, f, indent=4)

    return RedirectResponse(url="/", status_code=303)

@app.post("/delete-note")
def delete_note(request: Request, note_id: int = Form(...)):
    user_id = request.session.get("user_id")

    if not user_id:
        return RedirectResponse(url="/login", status_code=303)

    with open(json_path, "r") as f:
        note_data = json.load(f)

    user_notes = note_data.get(user_id, [])

    # Remove note safely
    user_notes = [note for note in user_notes if note["id"] != note_id]
    note_data[user_id] = user_notes

    with open(json_path, "w") as f:
        json.dump(note_data, f, indent=4)

    return RedirectResponse(url="/", status_code=303)
