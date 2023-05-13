from fastapi import FastAPI
from fastapi.testclient import TestClient
from src.api.hello_world import app


class TestApiRoot:

    def setup_method(self):
        self.client = TestClient(app)

    def test_read_root(self):
        response = self.client.get("/")
        assert response.status_code == 200
        assert response.json() == {"Hello": "World"}


class TestApiItem:

    def setup_method(self):
        self.client = TestClient(app)

    def test_read_item(self):
        response = self.client.get("/items/1")
        assert response.status_code == 200
        assert response.json()["q"] == "Foo"

    def test_read_item_not_found(self):
        response = self.client.get("/items/999")
        assert response.status_code == 404

