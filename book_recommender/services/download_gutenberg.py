import os
import pandas as pd
from gutenbergpy.gutenbergcache import GutenbergCache
from gutenbergpy.textget import get_text_by_id
from config import DATA_DIR, BOOKS_DIR, METADATA_PATH

def download_metadata():
    # This is a placeholder for actual metadata download
    # For real use, parse Project Gutenberg's RDF or use gutenbergpy
    df = pd.DataFrame([
        {'title': 'Sample Book 1', 'author': 'Author A', 'subjects': 'Fiction; Adventure', 'genre': 'Novel'},
        {'title': 'Sample Book 2', 'author': 'Author B', 'subjects': 'Science; Nonfiction', 'genre': 'Essay'},
        {'title': 'Sample Book 3', 'author': 'Author A', 'subjects': 'Mystery; Crime', 'genre': 'Novel'}
    ])
    df.to_csv(METADATA_PATH, index=False)

def download_books():
    # Example: Download books by Gutenberg ID (replace with real IDs)
    ids = [1342, 84, 1661]  # Pride and Prejudice, Frankenstein, Sherlock Holmes
    cache = GutenbergCache.get_cache()
    for i, book_id in enumerate(ids):
        text = get_text_by_id(book_id)
        title = f"Sample Book {i+1}"
        path = os.path.join(BOOKS_DIR, f"{title.replace(' ', '_')}.txt")
        with open(path, 'wb') as f:
            f.write(text)

if __name__ == "__main__":
    os.makedirs(BOOKS_DIR, exist_ok=True)
    download_metadata()
    download_books()
