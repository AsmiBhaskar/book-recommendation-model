from flask import Flask, render_template, request, jsonify
from models.recommender import recommend_books, books_by_author

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    title = data.get('title', '')
    n = int(data.get('n', 3))
    recommendations = recommend_books(title, n)
    return jsonify(recommendations)

@app.route('/author', methods=['POST'])
def author_books():
    data = request.get_json()
    author = data.get('author', '')
    books = books_by_author(author)
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)
