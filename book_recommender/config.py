import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
BOOKS_DIR = os.path.join(DATA_DIR, 'gutenberg_books')
METADATA_PATH = os.path.join(DATA_DIR, 'gutenberg_metadata.csv')
