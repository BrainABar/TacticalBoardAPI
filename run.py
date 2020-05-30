from flask import Flask
from apis.api import api
from database.data import db_session

app = Flask(__name__)
api.init_app(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


app.run(debug=True)
