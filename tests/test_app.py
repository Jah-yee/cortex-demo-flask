from app import create_app

def test_create_and_list_note():
    app = create_app()
    client = app.test_client()
    r = client.post("/notes", json={"body": "hello"})
    assert r.status_code == 201
    r = client.get("/notes")
    assert r.status_code == 200
    assert len(r.get_json()) == 1
