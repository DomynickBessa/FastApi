from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_read_item():
    response = client.get("/items/99")
    assert response.status_code == 200
    assert response.json() == {"item_id": 99, "q": None}


def test_update_item():
    response = client.put(
        "/items/99",
        json={"name": "Máquina de Combate", "price": 2.5})
    assert response.status_code == 200
    assert response.json() == {
        "item_name": "Máquina de Combate",
        "item_id": 99}


def test_add_item():
    response = client.post(
        "/items/999",
        json={"name": "Martelo do Thor", "price": 2.5, "is_offer": True})
    assert response.status_code == 200
    assert response.json() == {
        "item_id": 999,
        "item_name": "Martelo do Thor",
        "item_price": 2.5,
        "item_is_offer": True}


def test_delete_item():
    response = client.delete("/items/99")
    assert response.status_code == 200
    assert response.json() == {"item_id": 99}
