from . import todo

def init_route(app):
  app.register_blueprint(todo.bp)