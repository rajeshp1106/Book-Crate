from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
import pandas as pd
from math import ceil

app = Flask(__name__)

# Load data
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))
all_books_df = pickle.load(open('all_books.pkl','rb'))

# Constants
BOOKS_PER_PAGE = 50

@app.route('/')
def index():
    return render_template('index.html',
                           name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_ratings'].values),
                           )

@app.route('/recommend')
def recommend_ui():
    book_name = request.args.get('book')
    if book_name:
        return redirect(url_for('recommend_books', book=book_name))
    return render_template('recommend.html')

@app.route('/recommend_books')
def recommend_books():
    book_name = request.args.get('book')
    if not book_name:
        return redirect(url_for('recommend_ui'))
    
    try:
        # Find the index of the book
        index = np.where(pt.index == book_name)[0][0]
        # Get similar items
        similar_items = sorted(list(enumerate(similarity_scores[index])), 
                              key=lambda x: x[1], 
                              reverse=True)[1:6]
        
        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
            data.append(item)
        
        return render_template('recommend.html', 
                             recommendations=data, 
                             book_name=book_name,
                             search_made=True)
    except IndexError:
        return render_template('recommend.html', 
                             error="Book not found in our database",
                             search_made=True)

@app.route('/all')
def all_books():
    page = request.args.get('page', 1, type=int)
    search_query = request.args.get('search', '').lower()
    
    # Filter books based on search query
    if search_query:
        mask = (all_books_df['Book-Title'].str.lower().str.contains(search_query) | 
               all_books_df['Book-Author'].str.lower().str.contains(search_query) 
            )
        filtered_books = all_books_df[mask]
    else:
        filtered_books = all_books_df
    
    # Pagination
    total_books = len(filtered_books)
    total_pages = ceil(total_books / BOOKS_PER_PAGE)
    
    # Handle invalid page numbers
    if page < 1:
        page = 1
    elif page > total_pages and total_pages > 0:
        page = total_pages
    
    start_idx = (page - 1) * BOOKS_PER_PAGE
    end_idx = start_idx + BOOKS_PER_PAGE
    books_page = filtered_books.iloc[start_idx:end_idx]
    
    return render_template('all_books.html',
                         name=list(books_page['Book-Title'].values),
                         author=list(books_page['Book-Author'].values),
                         image=list(books_page['Image-URL-M'].values),
                         votes=list(books_page['num_ratings'].values),
                         rating=list(books_page['avg_ratings'].values),
                         year=list(books_page['Year-Of-Publication'].values),
                         page=page,
                         total_pages=total_pages,
                         search_query=search_query)

if __name__ == '__main__':
    app.run(debug=True)