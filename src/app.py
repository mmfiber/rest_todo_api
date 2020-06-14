from flask import jsonify
from app import app

@app.route("/")
def index():
  return jsonify({
    "message": "I'm REST API server for masa's todo"
  })

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)