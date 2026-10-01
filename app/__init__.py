from flask import Flask, jsonify, request

ITEMS = [
    {"id": "1", "name": "Claw hammer", "category": "tools"},
    {"id": "2", "name": "Screwdriver set", "category": "tools"},
    {"id": "3", "name": "M4 hex bolt", "category": "parts"},
    {"id": "4", "name": "Hydraulic hose", "category": "parts"},
    {"id": "5", "name": "Work gloves", "category": "consumables"},
]


def create_app():
    app = Flask(__name__)
    notes = {}

    @app.get("/notes")
    def list_notes():
        return jsonify(list(notes.values()))

    @app.post("/notes")
    def create_note():
        body = request.get_json()
        nid = str(len(notes) + 1)
        notes[nid] = {"id": nid, "body": body.get("body", "")}
        return jsonify(notes[nid]), 201

    @app.get("/api/items")
    def list_items():
        return jsonify(ITEMS)

    return app