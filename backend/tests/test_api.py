import os
import sys
import json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, ROOT)

from backend.app import app

def test_flashcards_endpoint():
    client = app.test_client()
    rv = client.get('/flashcards')
    assert rv.status_code == 200
    data = json.loads(rv.data)
    assert any(card['term'] == 'cursor' for card in data)
