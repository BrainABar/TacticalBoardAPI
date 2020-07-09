from fastapi import FastAPI
from app.routers import map_api

#app = Flask('TacticalBoardAPI')
#app.config['CORS_HEADER'] = 'Content-Type'
#app.register_blueprint(map_blueprint, url_prefix='/v1')

app = FastAPI()
app.include_router(map_api, prefix='/v1', )