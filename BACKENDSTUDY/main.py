from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Note(BaseModel):
    text: str

all_notes = ["Hello World"]

#Health check
@app.get("/")
async def read_root():
    return({"app": "running"})

#Post a new note
@app.post("/note")
async def create_note(note: Note):
    all_notes.append(note.text)
    return({"new_note": note.text})

#Get all notes
@app.get("/notes")
async def get_all_notes():
    return({"notes": all_notes})

#Get one note using list index
@app.get("/notes/{id}")
async def get_note(id: int):
    return({"note": all_notes[id]})

#Update note
@app.patch("/note/{id}")
async def update_note(id: int, note: Note):
    all_notes[id] = note.text
    return({"updatednote": all_notes[id]})