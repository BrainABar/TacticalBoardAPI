from flask import Flask
from blueprints.maps import api as map_blueprint

app = Flask('TacticalBoardAPI')
app.register_blueprint(map_blueprint, url_prefix='/api/v1')


app.run(debug=True)
