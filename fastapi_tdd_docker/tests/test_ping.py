from fastapi_tdd_docker.app import main


def test_ping(test_app):
    # given test app

    # when response
    response = test_app.get("/ping")

    # then we expect
    assert response.status_code == 200
    assert response.json() == {"environment": "dev", "ping": "pong", "testing": True}
