from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.notes.models import Note
from app.modules.notes.schemas import NoteCreate, NoteUpdate


def get_notes(db: Session) -> list[Note]:
    return list(db.scalars(select(Note).order_by(Note.id)))


def get_note(db: Session, note_id: int) -> Note | None:
    return db.get(Note, note_id)


def create_note(db: Session, data: NoteCreate) -> Note:
    note = Note(**data.model_dump())
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


def update_note(db: Session, note: Note, data: NoteUpdate) -> Note:
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(note, field, value)
    db.commit()
    db.refresh(note)
    return note


def delete_note(db: Session, note: Note) -> None:
    db.delete(note)
    db.commit()