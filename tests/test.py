from fastapi.testclient import TestClient

from database_test import Base
from api.database import get_db
from main import app

app.dependency_overrides[get_db] = Base.override_get_db
client = TestClient(app)

def test_create_user():
    response = client.post(
        "/api/message/",
        json={"customerId": 5, "type": "A", "amount": 100},
    )
    assert response.status_code == 200, response.text
    data = response.json()