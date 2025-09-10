import pandas as pd
import os
from config import METADATA_PATH, BOOKS_DIR

def load_metadata():
    return pd.read_csv(METADATA_PATH)

def get_book_text(title):
    filename = f"{title.replace(' ', '_')}.txt"
    path = os.path.join(BOOKS_DIR, filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""
