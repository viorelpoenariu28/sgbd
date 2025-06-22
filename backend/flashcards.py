import re
from pathlib import Path
import PyPDF2

PDF_PATH = Path(__file__).resolve().parent.parent / 'SGBD CURS DIACONITA COMPLET.pdf'

PHRASES = {
    'cursor': 'A cursor is a pointer',
    'PL/SQL block': 'Anonymous blocks:',
    'VARRAY': 'A varray has a maximum size'
}


def _extract_text():
    with open(PDF_PATH, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        return "\n".join(page.extract_text() for page in reader.pages)


def generate_flashcards():
    text = _extract_text()
    cards = []
    for key, phrase in PHRASES.items():
        idx = text.lower().find(phrase.lower())
        if idx != -1:
            snippet = text[idx:idx+160].replace('\n', ' ').strip()
            cards.append({'term': key, 'definition': snippet})
    return cards
