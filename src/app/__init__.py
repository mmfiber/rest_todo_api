from flask import Flask
from .db.database import init_db
from .entry.route import init_route

def create_app():
  app = Flask(__name__)
  app.config.from_object('app.config.Config')

  init_db(app)
  init_route(app)

  return app

app = create_app()