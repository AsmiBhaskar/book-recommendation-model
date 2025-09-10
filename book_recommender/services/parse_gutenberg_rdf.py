import os
import sys
import glob
import pandas as pd
from lxml import etree

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DATA_DIR, METADATA_PATH

rdf_dir = os.path.join(DATA_DIR, 'cache', 'epub')
fields = ['title', 'author', 'subjects', 'genre']

books = []
# Get all numbered directories
for book_dir in glob.glob(os.path.join(rdf_dir, '*')):
    if os.path.isdir(book_dir):
        book_id = os.path.basename(book_dir)
        rdf_file = os.path.join(book_dir, f'pg{book_id}.rdf')
        if os.path.exists(rdf_file):
            try:
                tree = etree.parse(rdf_file)
                root = tree.getroot()
                ns = {'dcterms': 'http://purl.org/dc/terms/',
                      'pgterms': 'http://www.gutenberg.org/2009/pgterms/',
                      'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'}
                
                title = root.find('.//dcterms:title', ns)
                title = title.text if title is not None else ''
                
                author = root.find('.//pgterms:agent//pgterms:name', ns)
                author = author.text if author is not None else ''
                
                subjects = [s.text for s in root.findall('.//dcterms:subject//rdf:value', ns)]
                
                genre = ''
                # Bookshelf/genre is in dcterms:bookshelf
                genre_tag = root.find('.//pgterms:bookshelf//rdf:value', ns)
                genre = genre_tag.text if genre_tag is not None else ''
                
                books.append({
                    'title': title,
                    'author': author,
                    'subjects': '; '.join(subjects),
                    'genre': genre
                })
            except Exception as e:
                print(f"Error parsing {rdf_file}: {e}")
                continue

# Save to CSV
pd.DataFrame(books, columns=fields).to_csv(METADATA_PATH, index=False)
print(f"Saved {len(books)} books to {METADATA_PATH}")
