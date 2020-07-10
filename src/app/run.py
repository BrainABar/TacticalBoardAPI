from fastapi import FastAPI
from app.routers import map_api
import uvicorn

# CORS NEEDED
# DEFAULT CONFIGS TO ALLOW SAMPLE DATABASES FOR TESTING

app = FastAPI()
app.include_router(map_api, prefix='/v1', )

if __name__ == '__main__':
    uvicorn.run(app)