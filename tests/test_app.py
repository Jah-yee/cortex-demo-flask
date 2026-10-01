from app import create_app

def test_create_and_list_note():
    app = create_app()
    client = app.test_client()
    r = client.post("/notes", json={"body": "hello"})
    assert r.status_code == 201
    r = client.get("/notes")
    assert r.status_code == 200
    assert len(r.get_json()) == 1

def test_list_items_unfiltered():
    app = create_app()
    client = app.test_client()
    r = client.get("/api/items")
    assert r.status_code == 200
    assert len(r.get_json()) == 5

def test_list_items_ignores_unknown_query_params():
    app = create_app()
    client = app.test_client()
    r = client.get("/api/items?sort=name")
    assert r.status_code == 200
    assert len(r.get_json()) == 5

def test_crash_route_returns_500():
    app = create_app()
    client = app.test_client()
    r = client.get("/crash")
    assert r.status_code == 500