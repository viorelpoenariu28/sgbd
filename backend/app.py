from flask import Flask, jsonify
from .flashcards import generate_flashcards

app = Flask(__name__)

@app.route('/flashcards')
def flashcards_endpoint():
    cards = generate_flashcards()
    return jsonify(cards)

if __name__ == '__main__':
    app.run(debug=True)
