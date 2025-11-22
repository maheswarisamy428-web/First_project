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
    assert "<p><b>Addition:</b> 25</p>" in html
    assert "<p><b>Subtraction:</b> 15</p>" in html
    assert "<p><b>Multiplication:</b> 100</p>" in html
    assert "<p><b>Division:</b> 4.0</p>" in html
