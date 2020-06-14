from datetime import datetime
from app.db.database import db

class Todo(db.Model):

  __tablename__ = "todos"

  id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
  title = db.Column(db.String(255), nullable=False)
  duedate = db.Column(db.DateTime, nullable=False)
  stauts = db.Column(db.INTEGER, default=0, nullable=False)
  memo = db.Column(db.Text)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow)