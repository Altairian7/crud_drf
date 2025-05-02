# models.py

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    due_date = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "dueDate": self.due_date.isoformat() if self.due_date else None
        }

def create_task(title, dueDate=None):
    due_date_obj = None
    if dueDate:
        due_date_obj = datetime.fromisoformat(dueDate)
    task = Task(title=title, due_date=due_date_obj)
    db.session.add(task)
    db.session.commit()
    return task.to_dict()
