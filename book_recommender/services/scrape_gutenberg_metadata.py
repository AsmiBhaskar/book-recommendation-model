import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from config import METADATA_PATH

def scrape_gutenberg_metadata(num_books=10):
    base_url = "https://www.gutenberg.org/ebooks/search/?sort_order=downloads&start_index="
    books = []
    for start in range(1, num_books+1, 25):
        url = base_url + str(start)
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        for book_item in soup.select('.booklink'):
            title = book_item.select_one('.title').text.strip() if book_item.select_one('.title') else ''
            author = book_item.select_one('.subtitle').text.strip() if book_item.select_one('.subtitle') else ''
            subjects = []
            genre = ''
            # Try to get subjects/genre from the book's detail page
            detail_link = book_item.get('href')
            if detail_link:
                detail_url = f"https://www.gutenberg.org{detail_link}"
                detail_resp = requests.get(detail_url)
                detail_soup = BeautifulSoup(detail_resp.text, 'html.parser')
                subjects_tags = detail_soup.select('th:contains("Subject") + td a')
                subjects = [tag.text for tag in subjects_tags]
                genre_tag = detail_soup.select_one('th:contains("Bookshelf") + td a')
                genre = genre_tag.text if genre_tag else ''
                time.sleep(0.5)  # Be polite to the server
            books.append({
                'title': title,
                'author': author,
                'subjects': '; '.join(subjects),
                'genre': genre
            })
            if len(books) >= num_books:
                break
        if len(books) >= num_books:
            break
    df = pd.DataFrame(books)
    df.to_csv(METADATA_PATH, index=False)
    print(f"Saved {len(df)} books to {METADATA_PATH}")

if __name__ == "__main__":
    scrape_gutenberg_metadata(num_books=10)
