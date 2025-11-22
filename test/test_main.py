import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200

    html = response.data.decode()

    assert "Maheswari" in html
    assert "Addition: 25" in html
    assert "Subtraction: 15" in html
    assert "Multiplication: 100" in html
    assert "Division: 4.0" in html
