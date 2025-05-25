import pytest
from app import create_app

@pytest.fixture
def client():
    """
    Фикстура создаёт тестовый клиент Flask для проверки маршрутов.
    """
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Ислам" in response.get_data(as_text=True)

def test_projects_page(client):
    response = client.get("/projects")
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert "GitHub" in html or "Репозиторий" in html

def test_about_page(client):
    response = client.get("/about")
    assert response.status_code == 200

def test_contacts_page(client):
    response = client.get("/contacts")
    assert response.status_code == 200
