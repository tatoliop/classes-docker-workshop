import json

from flask import Flask, jsonify, request, Response
from flask_swagger_ui import get_swaggerui_blueprint
import sqlite3
from flask.views import MethodView

from movie import Movie

# Init flask app
app = Flask(__name__)
# Init swagger
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'SQLite API'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
import db
db.init_app(app)


# Read data
@app.route("/movie/get/", methods=["GET"])
def movie_get():
    mydb = db.get_db()
    cur = mydb.cursor()
    cur.execute(f'SELECT * FROM movie')
    r = [dict((cur.description[i][0], value) \
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify(r)

# Write data
@app.route("/movie/put/", methods=["POST"])
def movie_put():
    in_data = request.get_json()
    if "title" not in in_data or "year" not in in_data or "score" not in in_data:
        return Response(json.dumps({"error": "Missing 1 or more keys 'year', 'year', 'score'"}), 500)
    mydb = db.get_db()
    cur = mydb.cursor()
    cur.execute(f'INSERT INTO movie (title, year, score) VALUES (?, ?, ?)',(in_data["title"], in_data["year"], in_data["score"]))
    mydb.commit()
    return jsonify({"Message": "OK"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
    # init-db

