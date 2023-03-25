import urllib.request 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.manifold import MDS


url = 'https://www.gutenberg.org/cache/epub/1155/pg1155.txt'
with urllib.request.urlopen(url) as f:
    book1 = f.read().decode('utf-8')

f = open('text/Book2.txt', 'r', encoding='utf-8-sig')
book2 = f.read()

f = open('text/Book3.txt', 'r', encoding='utf-8-sig')
book3 = f.read()

texts = [book1, book2, book3]

#generate similarity matrix
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(texts)
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

print(cosine_sim) 

# these are the similarities computed above
S = np.asarray([cosine_sim[0, :], cosine_sim[1, :], cosine_sim[2, :]])

# dissimilarity is 1 minus similarity
dissimilarities = 1 - S

# compute the embedding
coord = MDS(dissimilarity='precomputed').fit_transform(dissimilarities)

plt.scatter(coord[:, 0], coord[:, 1])

# Label the points
for i in range(coord.shape[0]):
    plt.annotate(str(i), (coord[i, :]))

plt.show()

