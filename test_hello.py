from main import app


def test_main():
    response = app.test_client().get("/")

    assert response.data == b"Hello World!"
