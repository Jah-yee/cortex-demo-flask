from flask import Flask, jsonify, request

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

    return app
