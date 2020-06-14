from flask import Blueprint
from ..db.repository import todo

bp = Blueprint("todo", __name__, url_prefix="/todo")

@bp.route("/")
def todos():
  return todo.get_all()