from flask import Flask
from database.data import db_session
from blueprints.maps import api as map_blueprint

app = Flask('TacticalBoardAPI')
app.register_blueprint(map_blueprint, url_prefix='/api/v1')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


app.run(debug=True)
