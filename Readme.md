I want to build a Flask-based web app called "Book Recommender" that recommends books from Project Gutenberg using scikit-learn.

📂 Project Structure:
book_recommender/
│── app.py                  # Flask entry point
│── requirements.txt        # Dependencies
│── config.py               # Configs (paths, settings)
│
├── data/
│   ├── gutenberg_metadata.csv  # Metadata with title, author, subjects
│   └── gutenberg_books/        # Downloaded text files
│
├── models/
│   ├── recommender.py      # Recommendation engine
│   └── __init__.py
│
├── services/
│   ├── data_loader.py      # Load Gutenberg metadata
│   ├── preprocess.py       # Clean + vectorize book text
│   └── __init__.py
│
├── templates/
│   └── index.html          # Frontend form + results
│
└── static/
    └── style.css           # Simple CSS

⚙️ Requirements:
- Use `gutenbergpy` or a local CSV for Gutenberg metadata.
- Use `scikit-learn` (TF-IDF + cosine similarity) to recommend top-N similar books.
- Implement `models/recommender.py` with a function `recommend_books(title: str, n: int = 5)` that returns a list of recommended book titles & authors.
- Flask routes:
  - `/` → Render `index.html` (input form)
  - `/recommend` → Take a book title as input and return top-N recommendations in JSON.
- Frontend: `index.html` should have a simple form where users enter a book title, submit, and display recommendations.
- Add CSS in `static/style.css` for basic styling.

💡 Goal:
Generate all the boilerplate code for each file so I can run `flask run` and test recommendations locally.
