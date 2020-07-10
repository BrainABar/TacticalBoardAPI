from app.routers import map_api
from starlette.testclient import TestClient

client = TestClient(map_api)


def test():
    response = client.get('/references')
    assert response.status_code == 404
