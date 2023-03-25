import urllib.request
from fuzzywuzzy import fuzz

url = 'https://www.gutenberg.org/cache/epub/1155/pg1155.txt'
with urllib.request.urlopen(url) as f:
    book1 = f.read().decode('utf-8')

with open('text/Book2.txt', 'r', encoding='utf-8-sig') as f:
    book2 = f.read()

with open('text/Book3.txt', 'r', encoding='utf-8-sig') as f:
    book3 = f.read()

print("Similarity between Book1 and Book2 is: ") 
print(fuzz.token_sort_ratio(book1, book2))
print("Similarity between Book1 and Book3 is: ") 
print(fuzz.token_sort_ratio(book1, book3))
print("Similarity between Book2 and Book 3 is: ") 
print(fuzz.token_sort_ratio(book2, book3))

#generate pairwise similarity matrix
import numpy as np
from sklearn.manifold import MDS
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
import seaborn as sns

# Create a list of the three books
books = [book1, book2, book3]

# Create a TfidfVectorizer object
vectorizer = TfidfVectorizer(stop_words='english')

# Generate the tf-idf matrix
tfidf_matrix = vectorizer.fit_transform(books)

# Compute the cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Generate a list of book titles
titles = ['Book1', 'Book2', 'Book3']

# Create a mapping from book title to index
indices = pd.Series(titles)

# Function that takes in book title as input and outputs most similar books
def get_recommendations(title, cosine_sim=cosine_sim):
    # Get the index of the book that matches the title
    idx = indices[indices == title].index[0]

    # Get the pairwsie similarity scores of all books with that book
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the books based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar books
    sim_scores = sim_scores[1:11]

    # Get the book indices
    book_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar books
    return titles.iloc[book_indices]

# Print the list of books most similar to Book1
print(get_recommendations('Book1'))

# Print the list of books most similar to Book2
print(get_recommendations('Book2'))

# Print the list of books most similar to Book3
print(get_recommendations('Book3'))
