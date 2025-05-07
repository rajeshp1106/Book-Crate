# Book-Crate
A book recommender website with GUI
# Book Recommendation System

## Features
- 📚 **Top 50 Popular Books** - Discover trending books based on ratings
- 🔍 **Search & Filter** - Find books by title, author, or publisher
- 🤖 **Smart Recommendations** - Get personalized book suggestions
- 📱 **Responsive Design** - Works on desktop and mobile devices
- 📊 **Pagination** - Browse through 200,000+ books efficiently

## Demo
[Live Demo](#) (Add your deployment link here)

![image](https://github.com/user-attachments/assets/6ff3fce8-67e4-4ff7-90ce-de312912804d)
![image](https://github.com/user-attachments/assets/0cdec609-5912-4f52-af6d-2a60c5856956)
![image](https://github.com/user-attachments/assets/5c7e6667-e4d7-4d85-9587-eb537b2a0a17)



## Installation

### Prerequisites
- Python 3.8+
- pip
- virtualenv (recommended)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/book-recommendation-system.git
   cd book-recommendation-system
2. python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. pip install -r requirements.txt
4. Download dataset files:
   Place popular.pkl, pt.pkl, books.pkl, similarity_scores.pkl, and all_books.pkl in the project root
5. For running the application python
   python app.py
   The application will be available at http://localhost:5000

###Project Structure
book-recommendation-system/
├── app.py                # Main Flask application
├── templates/            # HTML templates
│   ├── index.html        # Home page with top books
│   ├── all_books.html    # Browse all books
│   └── recommend.html    # Recommendation page
├── static/               # Static files (CSS, JS, images)
├── data/                 # Dataset files
│   ├── popular.pkl       # Popular books data
│   ├── pt.pkl            # Pivot table data
│   ├── books.pkl         # Books metadata
│   ├── similarity_scores.pkl  # Precomputed similarity scores
│   └── all_books.pkl     # Complete books dataset
├── requirements.txt      # Python dependencies
└── README.md            # This file

Technologies Used
Backend
Python 3

Flask (Web Framework)

Pandas (Data Processing)

NumPy (Numerical Computing)

Scikit-learn (Machine Learning)

Frontend
HTML5, CSS3

Bootstrap 5

JavaScript (for interactive features)

Data Processing
Collaborative Filtering (Recommendation Algorithm)

Pickle (Data Serialization)

API Endpoints
Endpoint	Method	Description
/	GET	Home page with top 50 books
/all	GET	Browse all books with pagination
/recommend	GET	Book recommendation page
/recommend_books	GET	Get recommendations for specific book
