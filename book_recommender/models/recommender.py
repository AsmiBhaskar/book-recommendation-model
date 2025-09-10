import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from services.data_loader import load_metadata

class BookRecommender:
    def __init__(self):
        self.metadata = load_metadata()
        self.titles = self.metadata['title'].tolist()
        self.authors = self.metadata['author'].tolist()
        self.subjects = self.metadata['subjects'].tolist()
        self.genres = self.metadata['genre'].tolist()
        
        # Create combined text for TF-IDF from metadata
        self.combined_texts = []
        for i in range(len(self.metadata)):
            combined = f"{self.titles[i]} {self.authors[i]} {self.subjects[i]} {self.genres[i]}"
            self.combined_texts.append(combined)
        
        # Vectorize using combined metadata
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
        self.tfidf_matrix = self.vectorizer.fit_transform(self.combined_texts)

    def recommend_books(self, title: str, n: int = 3):
        # Partial title match
        matches = self.metadata[self.metadata['title'].str.contains(title, case=False, na=False)]
        if matches.empty:
            return []
        
        idx = matches.index[0]
        query_vec = self.tfidf_matrix[idx]
        cosine_sim = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        sim_indices = cosine_sim.argsort()[-(n+1):][::-1]
        
        recommendations = []
        for i in sim_indices:
            if i != idx:
                recommendations.append({
                    'title': self.titles[i],
                    'author': self.authors[i],
                    'subjects': self.subjects[i],
                    'genre': self.genres[i]
                })
                if len(recommendations) == n:
                    break
        return recommendations

    def books_by_author(self, author: str):
        matches = self.metadata[self.metadata['author'].str.contains(author, case=False, na=False)]
        return matches[['title', 'author', 'subjects', 'genre']].to_dict(orient='records')

recommender = BookRecommender()

def recommend_books(title: str, n: int = 3):
    return recommender.recommend_books(title, n)

def books_by_author(author: str):
    return recommender.books_by_author(author)
